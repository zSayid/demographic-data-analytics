from fastapi import FastAPI
from app.routes import population, visualization
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Demographic API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# registering endpoints
app.include_router(population.router)
app.include_router(visualization.router)

# Root endpoint
@app.get("/")
async def read_root():
     return {"message": "Dunyo Aholisi Demografik Tahlili API ishlamoqda!"}