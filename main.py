from fastapi import FastAPI, Response

from routes.student_routes import StudentRouter

app = FastAPI()

app.include_router(StudentRouter)

#pip install -r requirements.txt
#uvicorn main:app --reload