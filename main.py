from fastapi import FastAPI

app = FastAPI()
@app.get("/my-profile")
def my_profile():
    return {
        "name": "Juan Diego",           # Cambiar por tu nombre
        "bootcamp": "FastAPI",
        "week": 1,
        "date": "2025",
        "likes_fastapi": True              # ¿Te gustó FastAPI?
    }

