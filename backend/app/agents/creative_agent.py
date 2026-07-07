from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest
from typing import Dict, List
import json

class CreativeAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest, research_data: str) -> Dict[str, List[str]]:
        prompt = f"""
        أنت مدير إبداعي (Creative Director). بناءً على أبحاث التسويق:
        {research_data}
        
        المطلوب:
        1. اقتراح 3 أفكار لتصاميم صور إعلانية (وصف بصري).
        2. اقتراح 2 سيناريو لفيديو قصير (Reels/TikTok).
        
        قم بالرد بتنسيق JSON فقط:
        {{
            "image_ideas": ["فكرة 1", "فكرة 2", "فكرة 3"],
            "video_scripts": ["سيناريو 1", "سيناريو 2"]
        }}
        """
        response = await self.llm.get_response(prompt)
        try:
            cleaned_response = response.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_response)
        except:
            return {{"image_ideas": [response], "video_scripts": []}}
