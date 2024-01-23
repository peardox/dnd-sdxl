import sys
import os
import time
import math
import json
import torch
from diffusers import DiffusionPipeline

# List of pip imports for CUDA (from PyTorch site)
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# pip install onnx transformers diffusers accelerate

# List of pip imports if not using CUDA
# pip install torch onnx transformers diffusers accelerate

# Configuration
input_name_file = "monsters.json"
output_image_dir = "dnd"
image_height = 512
image_width = 512
image_type = "jpg"
# use_cuda is mainly for Linux with NVIDIA cards. 
# Probably irrelevant for Windows but included 'just in case'
use_cuda = False 
# Tell it we're on a Apple Mac with ARM CPU
use_macm1 = False 
image_style = "from Dungeons and Dragons"


append_to_name = ["Black Pudding", "Roper", "Rug of Smothering", "Vrock"]
appended_text = "monster"

# Get start time
start_time = time.time()

# If input_name_file doesn't exist we can't run
if not os.path.isfile(input_name_file):
    print("Can't find", input_name_file, "so bailing out")
    sys.exit()

try:
    image_style
except NameError:
    print("No image_style set so bailing out")
    sys.exit()

# If output_image_dir doesn't exists create it
if not os.path.isdir(output_image_dir):
    os.makedirs(output_image_dir);

# Load SDXL Turbo model
if use_cuda: # CUDA
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("cuda")
elif use_macm1: #Mac ARM
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("mps")
else: # Something else
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo")

# Load monster list
data = json.load(open(input_name_file))

# Iterate through the json monster list
for mname in data['monsters']:
    if mname in append_to_name:
        image_of = mname + " " + appended_text
    else:
        image_of = mname
    results = pipe(
        prompt = "A " + image_of + " " + image_style,
        height=image_height, 
        width=image_width,
        num_inference_steps=1,
        guidance_scale=0.0,
    )
    imga = results.images[0]
    imga.save(output_image_dir + "/" + mname.replace(" ", "_") + "." + image_type)

# Get elapsed time
elapsed_time = round(time.time()-start_time)

print("Runtime =", math.floor(elapsed_time / 3600), "hours", math.floor((elapsed_time / 60) % 60), "mins", math.floor(elapsed_time % 60), "secs")

