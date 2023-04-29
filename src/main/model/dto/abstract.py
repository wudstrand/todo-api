from abc import ABC
from pydantic import BaseModel


class Base(ABC, BaseModel):
    class Config:
        use_enum_values = True
