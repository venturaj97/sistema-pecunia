from pydantic import BaseModel

class TransferRequest(BaseModel):
    value: float
    payer: int
    payee: int