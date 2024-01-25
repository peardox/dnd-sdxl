#########################################
#                                       #
# Global Configuration                  #
#                                       #
#########################################

# The json file containing the list of monsters (or whatever)
input_name_file = "monsters.json"
# Height of each output image
image_height = 512
# Width of each output image
image_width = 512
# Type of image to save as (jpg or png)
image_type = "jpg"
# use_cuda is mainly for servers with NVIDIA cards. Probably irrelevant for Windows 10/11 but included 'just in case'
# If you get an out of memory error with this set to True just change it to False - this happens if your GPU don't have enough RAM
use_cuda = False
# big_mac enables Mac-ARM to use more memory. If you've got an e.g. an M1 with 8G RAM or an x86 Mac then this should be false
big_mac = False

# append_to_name is a list of names that don't quite work so need something adding
append_to_name = ["Black Pudding", "Roper", "Rug of Smothering", "Vrock"]

# appended_text is added after any names (above) to provide better results
appended_text = "monster"

#########################################
#                                       #
# Configuration specific to dnd.py      #
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
