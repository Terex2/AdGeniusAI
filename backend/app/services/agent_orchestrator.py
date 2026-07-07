from app.schemas.ad_request import AdRequest, AdResponse
from app.agents.marketing_research_agent import MarketingResearchAgent
from app.agents.copywriting_agent import CopywritingAgent
from app.agents.creative_agent import CreativeAgent
from app.agents.campaign_strategy_agent import CampaignStrategyAgent

class AgentOrchestrator:
    def __init__(self):
        self.research_agent = MarketingResearchAgent()
        self.copywriting_agent = CopywritingAgent()
        self.creative_agent = CreativeAgent()
        self.strategy_agent = CampaignStrategyAgent()

    async def run_workflow(self, request: AdRequest) -> AdResponse:
        # 1. Marketing Research
        research_data = await self.research_agent.process(request)
        
        # 2. Copywriting
        ad_copies = await self.copywriting_agent.process(request, research_data)
        
        # 3. Creative Ideas
        creative_data = await self.creative_agent.process(request, research_data)
        
        # 4. Campaign Strategy
        strategy_data = await self.strategy_agent.process(request, research_data, ad_copies, creative_data)
        
        return AdResponse(
            marketing_plan=research_data,
            ad_copies=ad_copies,
            creative_ideas=creative_data.get("image_ideas", []),
            video_scripts=creative_data.get("video_scripts", []),
            marketing_strategy=strategy_data
        )
