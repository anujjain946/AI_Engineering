from pydantic import BaseModel, Field
from typing import List, Dict, Annotated, Optional

class MongoDBSchema(BaseModel):
    user_id: int
    bio: Annotated[str, Field(examples=["AI Engineer"])]
    interests: Annotated[List[str], Field(examples=[["AI", "Machine Learning"]])]
    social_links: Annotated[Dict[str, str], Field(examples=[{"LinkedIn": "https://linkedin.com/in/username"}])]


class UpdateMongoDBSchema(BaseModel):
    bio: Optional[str] = None
    interests: Optional[List[str]] = None
    social_links: Optional[Dict[str, str]] = None