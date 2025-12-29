from pydantic import BaseModel
from typing import Optional


class processRequest(BaseModel):
    file_id : str
    chunk_size: Optional[int] =  100
    overlap_size: Optional[int] =  100 
    do_reset : Optional[int] = 0
    
    