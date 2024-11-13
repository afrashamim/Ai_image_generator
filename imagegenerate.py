import os
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from accelerate import init_empty_weights

SDV5_MODEL_PATH = os.getenv('SDV5_MODEL_PATH')
SAVE_PATH = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'SD_OUTPUT')

if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + ' (' + str(counter) + ')' + extension
        counter += 1
    return path

prompt = "a dog riding a bike"
print(f"Characters in prompt: {len(prompt)}, limit: 200")

# Load model without torch.float16 for CPU compatibility
with init_empty_weights():
    pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH)

pipe = pipe.to("cpu")

# Generate the image
with autocast("cpu"):
    image = pipe(prompt).images[0]

# Save the generated image
image_path = uniquify(os.path.join(SAVE_PATH, (prompt[:25] + '...') if len(prompt) > 25 else prompt) + '.png')
print(image_path)
image.save(image_path)
