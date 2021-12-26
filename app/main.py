from fastapi import FastAPI
from strawberry.asgi import GraphQL

from app.db import metadata, engine, database
from app.graphql import schema
from app.views import router

metadata.create_all(engine)

graphql_app = GraphQL(schema)
app = FastAPI()


@app.on_event('startup')
async def start():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(router)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
