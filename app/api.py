import math
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://192.168.100.14:3000"pi
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/calculate/", tags=["calculator"], description="Calculate expression result")
async def calculate(value: str = '') -> dict:
    result = eval(unquote(value.replace('^', '**')))
    return {"result": str(result)}


@app.get("/percentage/", tags=["calculator"], description="Convert number into % ")
async def calculate(value: float = '') -> dict:
    return {"result": str(value/100)}


@app.get("/pi/", tags=["calculator"], description="Multiply number by pi ")
async def calculate(value: float = '') -> dict:
    return {"result": str(value * math.pi)}


@app.get("/square/", tags=["calculator"], description="Square Number ")
async def calculate(value: float = '') -> dict:
    return {"result": str(value*value)}


@app.get("/square-root/", tags=["calculator"], description="Square root of number")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.sqrt(value))}


@app.get("/sin/", tags=["calculator"], description="Sin of number")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.sin(value))}


@app.get("/cos/", tags=["calculator"], description="Cos of Number ")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.cos(value))}


@app.get("/tan/", tags=["calculator"], description="Tan of Number  ")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.tan(value))}


@app.get("/log/", tags=["calculator"], description="Log of Number ")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.log10(value))}


@app.get("/ln/", tags=["calculator"], description="Ln of Number  ")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.log(value))}


@app.get("/factorial/", tags=["calculator"], description="Factorial of Number ")
async def calculate(value: int = '') -> dict:

    return {"result": str(math.factorial(value))} if value > 0 else {"result": 'undefined'}


@app.get("/e/", tags=["calculator"], description="e * Number ")
async def calculate(value: float = '') -> dict:
    return {"result": str(math.exp(value))}


@app.get("/degree/", tags=["calculator"], description="Convert into degrees ")
async def calculate(value: int = '') -> dict:
    return {"result": str(math.degrees(value))}


@app.get("/radian/", tags=["calculator"], description="Convert into radians")
async def calculate(value: int = '') -> dict:
    return {"result": str(math.radians(value))}
