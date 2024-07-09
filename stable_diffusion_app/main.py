import io

from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import uvicorn

from stable_diffusion_app.ml import obtain_image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    price: float
    tags: list[str] = []

    
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    return item


@app.post("/generate")
def generate_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5
):
    image = obtain_image(
        prompt,
        num_inference_steps=num_inference_steps,
        seed=seed,
        guidance_scale=guidance_scale,
    )
    image.save("image.png")
    return FileResponse("image.png")


@app.get("/generate-memory")
def generate_image_memory(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5
):
    image = obtain_image(
        prompt,
        num_inference_steps=num_inference_steps,
        seed=seed,
        guidance_scale=guidance_scale,
    )
    memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)
    return StreamingResponse(memory_stream, media_type="image/png")


def main():
    # uvicorn.run("service:app", host="0.0.0.0", port=50052)
    uvicorn.run(app, host="0.0.0.0", port=50056) # app cos app = FastAPI() at line 5


if __name__ == '__main__':
    main()