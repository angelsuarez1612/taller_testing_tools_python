from pydantic import BaseModel


class Operation(BaseModel):
    op1: int
    op2: int
    operation: str
