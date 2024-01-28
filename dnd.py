#########################################
#                                       #
# DnD.py                                #
#                                       #
# This script takes the list of         #
# monsters in monsters.json and         #
# creates an image for each one         #
#                                       #
# Confugure this script in config.py    #
# to alter any of the presets           #
#                                       #
#########################################

# General system imports
import sys
import os
import time
import math
import json
# import Configuration
import config
# import SDXL Turbo model
from diffusers import DiffusionPipeline

# List of pip imports for CUDA (from PyTorch site - Check https://pytorch.org/get-started/locally/)
# pip install torch --index-url https://download.pytorch.org/whl/cu121
# pip install onnx transformers diffusers accelerate

# List of pip imports if not using CUDA
# pip install torch onnx transformers diffusers accelerate


# If input_name_file doesn't exist we can't run
if not os.path.isfile(config.input_name_file):
    print("Can't find", config.input_name_file, "so bailing out")
    sys.exit()

try:
    config.dnd_image_style
except NameError:
    print("No dnd_image_style set so bailing out")
    sys.exit()

# If dnd_image_dir doesn't exists create it
if not os.path.isdir(config.dnd_image_dir):
    os.makedirs(config.dnd_image_dir);

# Load SDXL Turbo model
if config.use_cuda: # CUDA
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("cuda")
elif config.big_mac: # Mac ARM with > 16G RAM
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("mps")
else: # Something else
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo")

# Load monster list
data = json.load(open(config.input_name_file))

# Get start time
start_time = time.time()

# Keep a look out for Ctl-C
try:
    # Iterate through the json monster list
    for mname in data['monsters']:
        if mname in config.append_to_name:
            image_of = mname + " " + config.appended_text
        else:
            image_of = mname
        # Generate image based on constructed prompt
        results = pipe(
            prompt = "A " + image_of + " " + config.dnd_image_style,
            height=config.image_height, 
            width=config.image_width,
            num_inference_steps=1,
            guidance_scale=0.0,
        )
        imga = results.images[0]
        # Save image then do the next one
        imga.save(config.dnd_image_dir + "/" + mname.replace(" ", "_") + "." + config.image_type)

# User hit Ctl-C so perform a clean exit
except KeyboardInterrupt:
    pass

# Get elapsed time
elapsed_time = round(time.time()-start_time)

# Print stats
print("Runtime =", math.floor(elapsed_time / 3600), "hours", math.floor((elapsed_time / 60) % 60), "mins", math.floor(elapsed_time % 60), "secs")

