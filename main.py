from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models.document
import models.node
import models.test_case

from database.database import Base, engine

from routes.document_routes import router as document_router
from routes.generation_routes import router as generation_router
from routes.node_routes import router as node_router
from routes.selection_routes import router as selection_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CT200 Document Management API",
    description="API for Document Parsing, Version Comparison and Test Case Generation",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "CT200 Project is Running Successfully!"
    }


app.include_router(document_router)
app.include_router(generation_router)
app.include_router(node_router)
app.include_router(selection_router)