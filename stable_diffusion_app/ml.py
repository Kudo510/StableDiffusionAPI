from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline
from PIL.Image import Image

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


# get your token at https://huggingface.co/settings/tokens
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)


def obtain_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5,
) -> Image:
    generator = None if seed is None else torch.Generator("cuda").manual_seed(seed)
    print(f"Using device: {pipe.device}")
    image: Image = pipe(
        prompt,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        generator=generator,
    ).images[0]
    return image


# image = obtain_image(prompt, num_inference_steps=5, seed=1024)
