from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest

class CampaignStrategyAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest, research_data: str, ad_copies: list, creative_data: dict) -> str:
        prompt = f"""
        أنت مخطط استراتيجي للحملات الإعلانية. بناءً على كل البيانات السابقة:
        الأبحاث: {research_data}
        النصوص: {ad_copies}
        الأفكار الإبداعية: {creative_data}
        
        المطلوب:
        بناء خطة حملة متكاملة تشمل:
        1. اختيار المنصات المناسبة.
        2. استراتيجية الاستهداف.
        3. توزيع الميزانية المقترح.
        4. الجدول الزمني للحملة.
        5. مؤشرات الأداء الرئيسية (KPIs).
        
        اكتب الخطة باللغة العربية بشكل احترافي.
        """
        return await self.llm.get_response(prompt)
