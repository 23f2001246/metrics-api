from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import time
import uuid
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dash-triih0.example.com"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.perf_counter()

        response = await call_next(request)

        process_time = time.perf_counter() - start

        response.headers["X-Request-ID"] = str(uuid.uuid4())
        response.headers["X-Process-Time"] = f"{process_time:.6f}"

        return response
app.add_middleware(MetricsMiddleware)
@app.get("/")
def home():
    return {"message": "Hello World"}
@app.get("/stats")

@app.get("/stats")
@app.get("/stats")

@app.get("/stats")
def stats(values: str):

    numbers = [int(x) for x in values.split(",")]

    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = total / count

    return {
        "email": "23f2001246@ds.study.iitm.ac.in",
        "count": count,
        "sum": total,
        "min": minimum,
        "max": maximum,
        "mean": mean
    }