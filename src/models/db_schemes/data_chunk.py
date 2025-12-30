from pydantic import BaseModel, Field ,validator
from bson import ObjectID
from typing import Optional

class Data_Chunk(BaseModel):
    _id: Optional[ObjectID] 
    chunk_text : str = Field(...,min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectID
    
    
    class config:
        arbitrary_types_allowed = True
