from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest
from typing import List
import json

class CopywritingAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest, research_data: str) -> List[str]:
        prompt = f"""
        أنت كاتب إعلانات (Copywriter) محترف. بناءً على أبحاث التسويق التالية:
        {research_data}
        
        وعلى بيانات المنتج:
        الاسم: {request.product_name}
        الوصف: {request.product_description}
        
        المطلوب:
        إنشاء 5 نسخ إعلانية مختلفة (عناوين ووصف وCTA) تتناسب مع منصات التواصل الاجتماعي.
        
        قم بالرد بتنسيق JSON فقط كقائمة من النصوص:
        ["نسخة 1", "نسخة 2", ...]
        """
        response = await self.llm.get_response(prompt)
        try:
            # محاولة تنظيف الرد إذا كان يحتوي على markdown
            cleaned_response = response.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_response)
        except:
            return [response]
