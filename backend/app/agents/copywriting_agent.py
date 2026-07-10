from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest
from typing import List
import json

class CopywritingAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest, research_data: str) -> List[str]:
        prompt = f"""
        أنت كاتب إعلانات (Direct Response Copywriter) محترف، خبير في صياغة الإعلانات التي تحقق أعلى معدلات تحويل.

        بناءً على أبحاث التسويق التالية:
        {research_data}
        
        وعلى بيانات المنتج:
        الاسم: {request.product_name}
        الوصف: {request.product_description}
        السعر: {request.price}

        المطلوب منك هو إنشاء 5 نسخ إعلانية متنوعة (Ad Copies) موجهة لمنصات التواصل الاجتماعي (Facebook, Instagram, Twitter, LinkedIn).
        
        يجب أن تتبع كل نسخة الهيكل التالي:
        - **العنوان (Headline)**: جذاب ومثير للفضول.
        - **النص الرئيسي (Body Content)**: يركز على الفوائد (Benefits) وليس فقط الميزات، ويخاطب نقاط الألم لدى الجمهور.
        - **الدعوة لاتخاذ إجراء (CTA)**: قوية وواضحة.

        أنواع النسخ المطلوبة:
        1. نسخة عاطفية (Emotional).
        2. نسخة تعليمية/معلوماتية (Educational).
        3. نسخة تركز على العرض والسعر (Offer-driven).
        4. نسخة تعتمد على الدليل الاجتماعي (Social Proof - افتراضي).
        5. نسخة قصيرة ومباشرة (Short & Direct).

        قم بالرد بتنسيق JSON فقط كقائمة من الكائنات، كل كائن يحتوي على (headline, body, cta):
        [
          {{"headline": "...", "body": "...", "cta": "..."}},
          ...
        ]
        """
        response = await self.llm.get_response(prompt)
        try:
            # محاولة تنظيف الرد إذا كان يحتوي على markdown
            cleaned_response = response.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_response)
        except:
            return [response]
