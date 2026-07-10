from app.utils.llm_handler import LLMHandler
from app.schemas.ad_request import AdRequest
from typing import Dict, List
import json

class CreativeAgent:
    def __init__(self):
        self.llm = LLMHandler()

    async def process(self, request: AdRequest, research_data: str) -> Dict[str, List[str]]:
        prompt = f"""
        أنت مدير إبداعي (Creative Director) في وكالة إعلانات عالمية. مهمتك هي تحويل الاستراتيجية إلى مفاهيم بصرية مذهلة.

        بناءً على أبحاث التسويق التالية:
        {research_data}
        
        المطلوب منك هو تقديم أفكار إبداعية خارج الصندوق:
        1. **أفكار تصاميم صور (Image Concepts)**: قدم 3 مفاهيم بصرية مفصلة. اشرح العناصر البصرية، الألوان، الإضاءة، والرسالة التي ينقلها التصميم.
        2. **سيناريوهات فيديو قصيرة (Short Video Scripts)**: قدم سيناريوهين لفيديوهات Reels أو TikTok. لكل سيناريو حدد:
           - المشهد الافتتاحي (The Hook).
           - المحتوى (The Value).
           - الخاتمة (The Call to Action).
           - المؤثرات الصوتية المقترحة.

        قم بالرد بتنسيق JSON فقط بالهيكل التالي:
        {{
            "image_ideas": [
                {{"title": "...", "description": "..."}},
                ...
            ],
            "video_scripts": [
                {{"title": "...", "hook": "...", "content": "...", "cta": "...", "audio": "..."}},
                ...
            ]
        }}
        """
        response = await self.llm.get_response(prompt)
        try:
            cleaned_response = response.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_response)
        except:
            return {{"image_ideas": [response], "video_scripts": []}}
