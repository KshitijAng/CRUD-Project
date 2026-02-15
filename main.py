from fastapi import FastAPI, Request
import time

# Import router
from routers.item_router import router as item_router

# Import ORM Base and engine
from repositories.Orm import engine, ORMBase
from repositories.models.item_model import ItemModel  

# Create FastAPI app
app = FastAPI(title="CRUD Service", version="1.0.0")


# Create tables on startup
ORMBase.metadata.create_all(bind=engine)


# Include routers
app.include_router(item_router)


# Health / root endpoint
@app.get("/")
async def health_check():
    return {"status": "Service is running"}


# --- Bonus: Logging Middleware ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    print(f"{request.method} {request.url.path} completed in {duration:.4f}s")

    return response
