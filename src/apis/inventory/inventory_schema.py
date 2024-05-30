from pydantic import BaseModel


class IventryRegistration(BaseModel):
    name: str
    category: str
    price: float
    currency: str
    quantity: int
    description : str