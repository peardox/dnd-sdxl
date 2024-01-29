import sys # Needed For final error check 
#########################################
#                                       #
# Global Configuration                  #
#                                       #
#########################################

# The json file containing the list of monsters (or whatever)
input_name_file = "monsters.json"
# Note that Larger images = more memory...
# Width of each output image - must be divisible by 8.
image_width = 512
# Height of each output image - must be divisible by 8
image_height = 512
# Type of image to save as (jpg or png)
image_type = "jpg"
# use_cuda is for machines with LARGE NVIDIA cards (16G or better).
# If you get an out of memory error with this set to True just
# change it to False - this happens if your GPU don't have enough RAM
use_cuda = False
# big_mac enables Mac-ARM to use more memory (i.e. 16G = True).
# If you get an out of memory error with this set to True just
# change it to False
big_mac = False

# append_to_name is a list of names that don't quite work so need something adding
append_to_name = ["Black Pudding", "Roper", "Rug of Smothering", "Vrock"]

# appended_text is added after any names (above) to provide better results
appended_text = "monster"

# repeat_count = how many versions of the monster to create
# If 1 then output file is <monster>.<image_type> 
# If >1 then output file is <monster>_<nnn>.<image_type> 

repeat_count = 1

#########################################
#                                       #
# Configuration specific to sdxl.py     #
#                                       #
#########################################

dnd_image_dir = "monsters"
dnd_image_style = "from Dungeons and Dragons"

#########################################
#                                       #
# Configuration specific to manyjobs.py #
#                                       #
#########################################

jobs_file = "jobs.json"
jobs_image_dir = "jobs"

#########################################
#                                       #
# Check image_width and image_height    #
# are both divisible by 8 (or SDXL will #
# throw an error)                       #
#                                       #
#########################################

# Check image_width is divisible by 8
if (image_width % 8) != 0:
    print("image_width must be divisible by 8 in config.py so bailing out")
    sys.exit()
    
# Check image_height is divisible by 8
if (image_height % 8) != 0:
    print("image_height must be divisible by 8 in config.py so bailing out")
    sys.exit()

if repeat_count < 1:
    print("repeat_count must be at least 1 in config.py so bailing out")
    sys.exit()

if repeat_count > 999:
    print("repeat_count must be at most 999 in config.py so bailing out")
    sys.exit()

if type(repeat_count) != int:
    print("repeat_count must be a whole number in config.py so bailing out")
    sys.exit()
