from fastapi import FastAPI
from app.routes import namaste, icd, mapping
from app.routes import fuzzy_search

# FastAPI app instance pehle create karo
app = FastAPI(title="NAMASTE ↔ ICD11 FHIR API")

# Fir routers include karo
app.include_router(fuzzy_search.router)
app.include_router(namaste.router)
app.include_router(icd.router)
app.include_router(mapping.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the NAMASTE ↔ ICD11 FHIR API"}
