from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import inventory, supplier, auth, forecast, agent

app = FastAPI(title="Inventory AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(supplier.router)
app.include_router(forecast.router)
app.include_router(agent.router)

@app.get("/")
def root():
    return {"status": "Inventory AI Agent Running"}
