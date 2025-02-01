from pydantic import BaseModel

class GenVideoInput(BaseModel):
    prompt: str