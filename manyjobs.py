import sys
import os
import time
import math
import json
from diffusers import DiffusionPipeline

# List of pip imports for CUDA
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# pip install onnx transformers diffusers accelerate

# List of pip imports if not using CUDA
# pip install torch onnx transformers diffusers accelerate

# SubDirectory for images
jobs_file = "jobs.json"
input_name_file = "monsters.json"
output_image_dir = "styles"
image_height = 512
image_width = 512
image_type = "jpg"
use_cuda = False # use_cuda is mainly for servers with NVIDIA cards. Probably irrelevant for Windows but included 'just in case'
big_mac = False # big_mac enables Mac-ARM to use more memory. If you've got an e.g. an M1 with 8G RAM or an x86 Mac then this should be false


append_to_name = ["Black Pudding", "Roper", "Rug of Smothering", "Vrock"]
appended_text = "monster"

# If input_name_file doesn't exist we can't run
if not os.path.isfile(input_name_file):
    print("Can't find", input_name_file, "so bailing out")
    sys.exit()

# If input_name_file doesn't exist we can't run
if not os.path.isfile(jobs_file):
    print("Can't find", jobs_file, "so bailing out")
    sys.exit()

# If output_image_dir doesn't exists create it
if not os.path.isdir(output_image_dir):
    os.makedirs(image_dir);

# Load SDXL Turbo model
if use_cuda: # CUDA
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("cuda")
elif big_mac: # Mac ARM with > 16G RAM
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("mps")
else: # Something else
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo")

# Load monster list
data = json.load(open(input_name_file))

# Load jobs list
jobs = json.load(open(jobs_file))

# Get start time
start_time = time.time()

# Iterate through the json jobs list
for job in jobs['job']:
    job_image_dir = job["dir"]
    image_style =  job["style"]
    
    # If output_image_dir/job_image_dir doesn't exists create it
    if not os.path.isdir(output_image_dir + "/" + job_image_dir):
        os.makedirs(output_image_dir + "/" + job_image_dir);

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
        imga.save(output_image_dir + "/" + job_image_dir + "/" + mname.replace(" ", "_") + "." + image_type)

# Get elapsed time
elapsed_time = round(time.time()-start_time)

print("Runtime =", math.floor(elapsed_time / 3600), "hours", math.floor((elapsed_time / 60) % 60), "mins", math.floor(elapsed_time % 60), "secs")

