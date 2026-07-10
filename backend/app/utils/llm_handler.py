import logging
from langchain_openai import ChatOpenAI
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMHandler:
    def __init__(self, model_name: str = None, temperature: float = 0.7):
        self.model_name = model_name or settings.LLM_MODEL
        self.temperature = temperature
        self.llm = ChatOpenAI(
            openai_api_base=settings.LLM_API_BASE,
            openai_api_key=settings.LLM_API_KEY,
            model_name=self.model_name,
            temperature=self.temperature
        )

    async def get_response(self, prompt: str) -> str:
        try:
            logger.info(f"Calling LLM ({self.model_name}) with prompt length: {len(prompt)}")
            response = await self.llm.ainvoke(prompt)
            return response.content
        except Exception as e:
            logger.error(f"Error calling LLM: {e}")
            return f"Error: Unable to get response from AI model. Details: {str(e)}"
