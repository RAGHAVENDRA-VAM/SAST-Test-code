from fastapi import FastAPI
import os
import pickle  # ❌ insecure
from db import get_db_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Insurance Portal Running"}

# ❌ Command Injection (Semgrep)
@app.get("/run")
def run(cmd: str):
    os.system("echo " + cmd)
    return {"status": "executed"}

# ❌ Insecure deserialization
@app.post("/load")
def load_data(data: bytes):
    return pickle.loads(data)

# ❌ Debug enabled
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)