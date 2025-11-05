from fastapi import FastAPI

from app.routes.auth_routes import route as authRoute


app = FastAPI()

app.include_router(authRoute )

@app.get("/health")
def health_check():
    return {
        "status" : "OK"
    }