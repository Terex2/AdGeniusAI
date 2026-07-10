from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    product_description = Column(Text, nullable=False)
    price = Column(String(100))
    target_audience = Column(String(255))
    
    marketing_plan = Column(Text)
    ad_copies = Column(JSON)
    creative_ideas = Column(JSON)
    video_scripts = Column(JSON)
    marketing_strategy = Column(Text)
    
    created_at = Column(DateTime, default=datetime.utcnow)
