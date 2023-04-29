from typing import Optional
from uuid import UUID

from src.main.model.dto.abstract import Base
from src.main.model.dto.state import State


class ItemResponse(Base):
    id: UUID
    name: str
    description: Optional[str]
    state: State
