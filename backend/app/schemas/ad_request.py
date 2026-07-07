from pydantic import BaseModel
from typing import List, Optional

class AdRequest(BaseModel):
    product_name: str
    product_description: str
    price: str
    target_audience: str

class AdResponse(BaseModel):
    marketing_plan: str
    ad_copies: List[str]
    creative_ideas: List[str]
    video_scripts: List[str]
    marketing_strategy: str
