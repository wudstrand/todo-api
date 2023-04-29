from typing import Optional

from src.main.model.dto.abstract import Base
from src.main.model.dto.state import State


class ItemRequest(Base):
    name: str
    description: Optional[str]
    state: State
