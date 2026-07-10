from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest

class MarketingResearchAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest) -> str:
        prompt = f"""
        أنت خبير استراتيجي في أبحاث التسويق وبناء العلامات التجارية. مهمتك هي إجراء تحليل معمق للمنتج التالي لتزويد فريق التسويق ببيانات دقيقة:

        بيانات المنتج:
        - الاسم: {request.product_name}
        - الوصف: {request.product_description}
        - السعر: {request.price}
        - الجمهور المستهدف الأولي: {request.target_audience}

        المطلوب منك هو تقديم تقرير مفصل يتضمن:
        1. **تحليل السوق والمنافسة**: من هم المنافسون المحتملون؟ وكيف يتموضع هذا المنتج مقارنة بهم؟
        2. **تحليل الجمهور المستهدف (Personas)**: قم بتفصيل شخصيات المشترين المحتملين، احتياجاتهم، نقاط الألم لديهم (Pain Points)، وما الذي يحفزهم للشراء.
        3. **نقاط البيع الفريدة (USPs)**: استخرج على الأقل 5 نقاط قوة تجعل هذا المنتج متميزاً.
        4. **تحليل SWOT**: (نقاط القوة، نقاط الضعف، الفرص، التهديدات).
        5. **الرسالة الجوهرية (Core Message)**: ما هي الرسالة الواحدة التي يجب أن تصل للجمهور؟

        اكتب التقرير باللغة العربية بأسلوب مهني، تحليلي، وجذاب. استخدم تنسيق Markdown لتنظيم التقرير.
        """
        return await self.llm.get_response(prompt)
