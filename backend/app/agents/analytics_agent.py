from app.utils.llm_handler import LLMHandler

class AnalyticsAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, campaign_data: dict) -> str:
        prompt = f"""
        أنت محلل بيانات تسويقية. قم بتحليل البيانات التالية واقترح تحسينات:
        {campaign_data}
        
        المطلوب:
        1. تحديد نقاط القوة والضعف.
        2. اقتراح تحسينات فورية.
        3. توقعات الأداء المستقبلية.
        """
        return await self.llm.get_response(prompt)
