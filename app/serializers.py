from pydantic import BaseModel


class TireIn(BaseModel):
    manufacturer: str
    season: str
    profile: str




