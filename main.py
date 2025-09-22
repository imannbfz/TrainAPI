from fastapi import FastAPI, Query
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/sum")
def sum_numbers(a: float = Query(...), b: float = Query(...)):
    return {"result": a + b}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
