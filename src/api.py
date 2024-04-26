from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/square/")
def calculate_square(x: int):
    try:
        if x < 0:
            raise HTTPException(status_code=400, detail="Input must be a positive integer")
        result = x ** 2
        return {"message": f"The square of {x} is {result}", "result": result}
    except Exception as e :
        raise HTTPException(status_code=500, detail=str(e))