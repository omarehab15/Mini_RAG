from pydantic import BaseModel, Field ,validator ,ConfigDict
from bson.objectid import ObjectId
from typing import Optional

class Data_Chunk(BaseModel):
    _id: ObjectId

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )
    
    # id: Optional[ObjectId] = Field(None , alias= "_id") 
    chunk_text : str = Field(...,min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    
    
    class config:
        arbitrary_types_allowed = True
