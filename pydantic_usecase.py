from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum
import time


class Language(Enum):
    PY = 'python'
    JAVA = 'java'
    GO = 'go'


class Comments(BaseModel):
    text: Optional[str]


class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool
    created_at: datetime = Field(default_factory=datetime.now)
    language: Language = list[Language.PY]
    comments: list[Comments] = []


b1 = Blog(title='Hi Everyone!', is_active=True, comments=[{'text': 'Heelllo'}])
print(b1)
time.sleep(5)
b2 = Blog(title='Need to file Tax', is_active=True, language=Language.JAVA)
print(b2)