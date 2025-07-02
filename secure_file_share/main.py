from fastapi import FastAPI
from app.routes import ops_routes, client_routes
from app.database import init_db

app = FastAPI(title="Secure File Sharing API")

# Initialize database
init_db()

# Include routers
app.include_router(ops_routes.router, prefix="/ops", tags=["Ops User"])
app.include_router(client_routes.router, prefix="/client", tags=["Client User"])

@app.get("/")
def root():
    return {"message": "Welcome to the Secure File Sharing System"}
