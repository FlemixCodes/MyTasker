from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TaskModel(BaseModel):
    title: str = Field(..., example="Купить молоко")
    description: Optional[str] = Field(None, example="Нужно купить молоко в магазине")
    tags: List[str] = Field(default_factory=list, example=["покупки", "еда"])
    priority: int = Field(default=1, ge=1, le=5, example=3)
    created_at: datetime = Field(default_factory=datetime.now())
