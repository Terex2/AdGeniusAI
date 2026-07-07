from langchain_openai import ChatOpenAI
from app.core.config import settings

class LLMHandler:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_base=settings.LLM_API_BASE,
            openai_api_key=settings.LLM_API_KEY,
            model_name=settings.LLM_MODEL,
            temperature=0.7
        )

    async def get_response(self, prompt: str) -> str:
        response = await self.llm.ainvoke(prompt)
        return response.content
