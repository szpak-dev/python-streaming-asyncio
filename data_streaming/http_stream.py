from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    with open("static/http_stream.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")


async def event_generator():
    while True:
        await asyncio.sleep(1)
        yield f"data: The current time is {int(asyncio.get_event_loop().time())}\n\n"


@app.get("/events")
async def events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
