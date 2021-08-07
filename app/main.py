import uvicorn
from fastapi import FastAPI

from app.calculator import Calculator
from app.serializers.operation import Operation

app = FastAPI()


@app.post('/maths/calculate')
def calculate(op: Operation) -> int:
    calculator = Calculator()

    result = calculator.calculate(op.op1, op.op2, operation=op.operation)

    return result


@app.post('/maths/expression')
def expression(op: Operation) -> str:
    calculator = Calculator()

    result = calculator.get_expression(op.op1, op.op2, operation=op.operation)

    return result


if __name__ == '__main__':
    uvicorn.run('app.main:app', reload=True)