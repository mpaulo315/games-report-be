from pydantic import BaseModel
from typing import Optional
class GameChart(BaseModel):
    title: str
    console: str
    genre: str
    publisher: str
    developer: Optional[str] = None
    critic_score:Optional[float] = None
    total_sales: Optional[float] = None
    na_sales: Optional[float] = None 
    jp_sales: Optional[float] = None
    pal_sales: Optional[float] = None
    other_sales: Optional[float] = None
    release_date: Optional[int] = None