from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Server(BaseModel):
    name: str
    instance_type: str
    status: str = "Stopped"

servers = []

@app.get("/")
def home():
    return {"message":"Welcome to my API"}

@app.get("/servers")
def get_servers():
    return servers

@app.get("/servers/{server_name}")
def get_server(server_name):
    for server in servers:
        if server.name == server_name:
            return server

    raise HTTPException(status_code=404, detail="Server not found")

@app.get("/search")
def search_server(status):
    return {"status": status}
'''
@app.post("/servers")
def create_server(server: Server):
    servers.append(server)
    return server
'''
@app.delete("/servers/{server_name}")
def delete_server(server_name):
    for server in servers:
        if server.name == server_name:
            servers.remove(server)
            return servers

    raise HTTPException(status_code=404, detail="Server not found")


@app.put("/servers/{server_name}")
def update_server(server_name, updated_server: Server):
    for server in servers:
        if server.name == server_name:
            server.instance_type = updated_server.instance_type
            server.status = updated_server.status
            return server


    raise HTTPException(status_code=404, detail="Server not found")


@app.post("/servers", status_code=201)
def create_server(server: Server):

    for existing_server in servers:
        if existing_server.name == server.name:
            raise HTTPException(
                status_code=400,
                detail="Server already exists"
            )

    servers.append(server)
    return server