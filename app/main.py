from fastapi import FastAPI 
app=FastAPI()
print("Creating fastAPI application.")
@app.get("/")
def home():
    return {
        "status":"running"
    }
task=