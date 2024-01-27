# dnd-sdxl
A Python Script to automate the creation of DND artwork from SRD-OGL-CC-BY-4.0 using SDXL Turbo

<p align="center">
	<img src="images\roper.jpg" alt="roper" style="zoom:50%;" />
    <br />It even makes cakes :)
</p>
This Python script takes a list of things to draw (monsters.json) then uses SDXL Turbo to create all the images by running python dnd.py

The alternative script manyjobs.py extends dnd.py to also take input from jobs.json to run the same set of image generations with slightly differing qualifiers. The supplied jobs.json does 12 different syles (plus the obligatory 'playing a guitar on the moon') placing each set of outputs in a new sub-directory - edit jobs.json to alter if you so desire - it's fairly self-evident what's needed. One obvious use alternate use for jobs.json is to run the same set multiple times to obtain many variations in the same style.

An NVIDIA GPU with 16G or more RAM is required for the best performance.

Configuration is altered via config.py. The only option that really needs explaining is "append_to_name" - this one is a simple list of things in monsters.json that don't quite work as desired, e.g. Black Pudding creates an image of a [Black Pudding](https://en.wikipedia.org/wiki/Black_pudding) rather than the DnD monster [Black Pudding](https://www.dndbeyond.com/monsters/16808-black-pudding) so the text in "appended_text" just below is added to the SDXL request - it's still far from perfect but not nearly as bad.

config.py has default values set for the least powerful machines (so it'll at least run). If you have a NVIDIA GPU with 16G or more or an Arm-based Mac with 16G RAM you will need to alter this file (it'll be a lot faster as a result)

preftech.py is intended to allow users with SLOWER Broadband to do the model download required by SDXL before running the main scripts (it can take a long time)    

The SetupSamples directory has some notes on setup for specific platforms

Works on Windows, Mac , Linux and Raspberry Pi5 (tested all four - Pi5 is dreadful... needs more RAM which would probably be quite usable - not available when writing this though)

Windows/Linux will work without a GPU but a NVIDIA GPU with 16G (or more) makes things run extremely fast.

Without a supported GPU it will work but 16G of system RAM is really needed (it will work in 8G but you won't like it...)

If running Linux with a NVIDIA card with 16G or better RAM it is important to install the latest driver and set use_cuda to True. Sample setups for AWS G5 (A10/24) and Scaleway Render-S (P100/16) instances is included for reference (the fastest results by a huge margin)

It's worth noting that SDXL doesn't appear to know what many monsters look like. This is best illustrated by running with image_style set to "in the style of a cake". A fair few 'monsters' are rendered just as cakes with no monster in sight. Having said that there are a large number that produce really nice monster cakes :)

Macs will run out of memory if they have 8G RAM while 16G works well. To get around this issue there's a big_mac option in config.py that should be set to True if you have 16G or more or leave it set to False if you have 8G - it'll be slower but at least it'll run.

Some other ideas for alternate styles can be found in jobs.json and the style can be manually changes in monsters.json (which is quicker if you don't wanna run them all) - the "Plush Toy" version is one of my favourite variants.

Sample outputs from manyjobs.py

=== Fill Me In ===

Credits

https://github.com/Tabyltop/CC-SRD for [Monsters-SRD5.1-CCBY4.0License-TT.json](https://github.com/Tabyltop/CC-SRD/blob/main/Monsters-SRD5.1-CCBY4.0License-TT.json) as a source of Monster names

References, Additional Licenses etc...

https://huggingface.co/stabilityai/sdxl-turbo

https://huggingface.co/stabilityai/sdxl-turbo/raw/main/LICENSE.TXT

https://www.dndbeyond.com/attachments/39j2li89/SRD5.1-CCBY4.0License.pdf

This script itself is a do what you want though
