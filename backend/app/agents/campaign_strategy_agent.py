from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest

class CampaignStrategyAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest, research_data: str, ad_copies: list, creative_data: dict) -> str:
        prompt = f"""
        أنت مدير استراتيجي للحملات الرقمية (Digital Campaign Strategist). مهمتك هي دمج كل المخرجات السابقة في خطة عمل متكاملة قابلة للتنفيذ.

        البيانات المتاحة:
        - أبحاث السوق: {research_data}
        - النصوص الإعلانية: {ad_copies}
        - المفاهيم الإبداعية: {creative_data}
        
        المطلوب منك هو بناء خطة حملة شاملة تتضمن:
        1. **الأهداف الاستراتيجية**: ما الذي نسعى لتحقيقه (وعي، مبيعات، تفاعل)؟
        2. **مزيج المنصات (Platform Mix)**: حدد المنصات الأنسب (Meta, Google, TikTok, Snapchat) ولماذا؟
        3. **تكتيكات الاستهداف (Targeting Tactics)**: حدد الاهتمامات، السلوكيات، والكلمات المفتاحية المقترحة.
        4. **هيكل الحملة (Campaign Structure)**: كيف سيتم تقسيم المجموعات الإعلانية؟
        5. **توصيات الميزانية**: كيف يتم توزيع الميزانية بين المنصات والمراحل (اختبار، توسع)؟
        6. **خارطة الطريق (Roadmap)**: جدول زمني لمدة 4 أسابيع لإطلاق وتحسين الحملة.
        7. **التحليل والقياس (KPIs)**: ما هي الأرقام التي سنراقبها لضمان النجاح؟

        اكتب الخطة باللغة العربية بأسلوب استراتيجي وعملي. استخدم تنسيق Markdown.
        """
        return await self.llm.get_response(prompt)
