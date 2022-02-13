from typing import Optional
from pycpfcnpj import cpf
from pydantic import BaseModel, validator


class Solicitation(BaseModel):
    name: str
    cpf: str
    income: float
    ocupation: str
    score: Optional[int] = None
    limit: Optional[float] = None
    approval: Optional[str] = None

    @validator('cpf')
    def cpf_validator(cls, value):
        if not cpf.validate(value):
            raise ValueError("Invalid CPF used, please, try again")
        return value

    @validator('income')
    def income_validator(cls, value):
        if not value > 0:
            raise ValueError("Invalid income, income should be positive")
        return value
