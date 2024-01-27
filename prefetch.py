#########################################
#                                       #
# Prefetch.py                           #
#                                       #
# For users with SLOWER BroadBand       #
#                                       #
# This script performs an initial       #
# fetch of the DiffusionPipeline        #
# used by Diffusers                     #
#                                       #
# This is COMPLETELY optional as the    #
# other scripts will do the same thing  #
# if required                           #
#                                       #
# If you use this it only needs running #
# ONCE, repeat runs wont do anything    #
# useful                                #
#                                       #
# The main envisaged use for this       #
# script is to do the time-consuming    #
# DiffusionPipeline request by itself   #
# for users with SLOWER BroadBand       #
#                                       #
# Basically run this then go watch a    #
# film, go to bed or whatever while     #
# this runs then you can run dnd.py     #
# or manyjobs.py without a very long    #
# wait (possibly several hours)         #
#                                       #
# Sample Timings                        #
#   20 Mbps = 1 hours 35 mins 07 secs   #
#   40 Mbps = 0 hours 45 mins 56 secs   #
# 1400 Mbps = 0 hours 01 mins 09 secs   #
#                                       #
#########################################

# General system imports
import time
import math
# import Configuration
import config
# import SDXL Turbo model
from diffusers import DiffusionPipeline

# List of pip imports for CUDA (from PyTorch site - Check https://pytorch.org/get-started/locally/)
# pip install torch --index-url https://download.pytorch.org/whl/cu121
# pip install onnx transformers diffusers accelerate

# List of pip imports if not using CUDA
# pip install torch onnx transformers diffusers accelerate

# Get start time
start_time = time.time()

# Load SDXL Turbo model
if config.use_cuda: # CUDA
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("cuda")
elif config.big_mac: # Mac ARM with > 16G RAM
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo").to("mps")
else: # Something else
    pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo")

# Get elapsed time
elapsed_time = round(time.time()-start_time)

# Print stats - add some blank lines before message as the display gets messy
print("\n\n\n\nRuntime =", math.floor(elapsed_time / 3600), "hours", math.floor((elapsed_time / 60) % 60), "mins", math.floor(elapsed_time % 60), "secs")

