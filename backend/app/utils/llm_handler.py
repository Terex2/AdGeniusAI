import logging
import json
import uuid
import httpx
import asyncio
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMHandler:
    def __init__(self, model_name: str = None, temperature: float = 0.7):
        self.model_name = model_name or "gpt-5"
        self.temperature = temperature
        self.base_url = "https://android.chat.openai.com/backend-api/f/conversation"
        self.prepare_url = f"{self.base_url}/prepare"

    def _get_headers(self):
        return {
            'User-Agent': 'ChatGPT/1.2027.000 (Android 15; RMX3834; build 2700000)',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'oai-client-type': 'android',
            'oai-device-id': str(uuid.uuid4())
        }

    async def _get_conduit_token(self, client, headers):
        try:
            payload = {"action": "next", "model": self.model_name}
            response = await client.post(self.prepare_url, json=payload, headers=headers, timeout=5)
            if response.status_code == 200:
                return response.json().get('conduit_token', '')
        except Exception as e:
            logger.error(f"Error getting conduit token: {e}")
        return ""

    async def get_response(self, prompt: str, system_prompt: str = "") -> str:
        headers = self._get_headers()
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            token = await self._get_conduit_token(client, headers)
            if token:
                headers['Conduit-Token'] = token
            
            headers['x-oai-convo-session-id'] = str(uuid.uuid4())
            
            messages = []
            if system_prompt:
                messages.append({
                    'id': str(uuid.uuid4()),
                    'author': {'role': 'user'},
                    'content': {'content_type': 'text', 'parts': [system_prompt]}
                })
            
            messages.append({
                'id': str(uuid.uuid4()),
                'author': {'role': 'user'},
                'content': {'content_type': 'text', 'parts': [prompt]}
            })

            payload = {
                'action': 'next',
                'messages': messages,
                'model': self.model_name,
                'parent_message_id': str(uuid.uuid4()),
                'stream': True
            }

            try:
                full_response = ""
                async with client.stream("POST", self.base_url, headers=headers, json=payload) as response:
                    async for line in response.aiter_lines():
                        if line and line.startswith('data: '):
                            data_str = line[6:]
                            if data_str == '[DONE]':
                                break
                            try:
                                data_json = json.loads(data_str)
                                if 'message' in data_json and data_json['message'].get('author', {}).get('role') == 'assistant':
                                    parts = data_json['message']['content'].get('parts', [])
                                    if parts and parts[0]:
                                        new_text = parts[0]
                                        # المحرك يرسل النص كاملاً في كل مرة، نحتاج لآخر جزء فقط
                                        full_response = new_text
                            except:
                                continue
                
                if not full_response:
                    logger.warning("Empty response from Mr Dark Engine, falling back to basic info.")
                    return "خطأ في الاتصال بمحرك الذكاء الاصطناعي. يرجى المحاولة لاحقاً."
                
                return full_response

            except Exception as e:
                logger.error(f"Error calling Mr Dark Engine: {e}")
                return f"Error: Unable to get response. Details: {str(e)}"
