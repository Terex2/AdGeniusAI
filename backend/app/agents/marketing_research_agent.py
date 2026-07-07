from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest

class MarketingResearchAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest) -> str:
        prompt = f"""
        أنت خبير في أبحاث التسويق. قم بتحليل المنتج التالي:
        الاسم: {request.product_name}
        الوصف: {request.product_description}
        السعر: {request.price}
        الجمهور المستهدف: {request.target_audience}
        
        المطلوب:
        1. تحليل السوق والمنافسين.
        2. فهم عميق للجمهور المستهدف.
        3. استخراج نقاط البيع الفريدة (USPs).
        4. تحديد التحديات والفرص.
        
        اكتب التقرير باللغة العربية بشكل احترافي.
        """
        return await self.llm.get_response(prompt)
