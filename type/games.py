from pydantic import BaseModel
from typing import Optional

# class GameProjection(BaseModel):
#     id: Optional[int] = 0
#     img: Optional[int] = None
#     title: Optional[int] = 1
#     console: Optional[int] = 1
#     genre: Optional[int] = 1
#     publisher: Optional[int] = 1
#     developer: Optional[int] = 1
#     critic_score: Optional[int] = 1
#     total_sales: Optional[int] = 1
#     na_sales: Optional[int] = 1
#     jp_sales: Optional[int] = 1
#     pal_sales: Optional[int] = 1
#     other_sales: Optional[int] = 1
#     release_date: Optional[int] = 1
#     year: Optional[int] = None
#     month: Optional[int] = None
#     day: Optional[int] = None

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