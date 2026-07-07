from fastapi import APIRouter, Depends, HTTPException
from app.schemas.ad_request import AdRequest, AdResponse
from app.services.agent_orchestrator import AgentOrchestrator

router = APIRouter()

@router.post("/generate", response_model=AdResponse)
async def generate_ad(request: AdRequest):
    orchestrator = AgentOrchestrator()
    try:
        result = await orchestrator.run_workflow(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
