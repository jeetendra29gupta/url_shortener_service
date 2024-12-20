from pydantic import BaseModel


class URLItem(BaseModel):
    url: str
