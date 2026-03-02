import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hostname")
def get_hostname():
    return {"hostname": socket.gethostname()}
