# dnd-sdxl
<img src="images\roper.jpg" alt="roper" style="zoom:50%;" />

A Python Script to automate the creation of DND artwork from SRD-OGL-CC-BY-4.0 using SDXL Turbo

This Python script takes a list of things to draw (monsters.json) then uses SDXL Turbo to create all the images by running python dnd.py

The alternative script manyjobs.py extends dnd.py to also take input from jobs.json to run the same set of image generations with slightly differing qualifiers. The supplied jobs.json does 12 different syles placing each set of outputs in a new sub-directory - edit jobs.json to alter if you so desire - it's fairly self-evident what's needed. One obvious use alternate use for jobs.json is to run the same set multiple times to obtain many variations in the same style.

Both scripts have configuration sections near the top. The only option that really needs explaining is "append_to_name" - this one is a simple list of things in monsters.json that don't quite work as desired, e.g. Black Pudding creates an image of a [Black Pudding](https://en.wikipedia.org/wiki/Black_pudding) rather than the DnD monster [Black Pudding](https://www.dndbeyond.com/monsters/16808-black-pudding) so the text in "appended_text" just below is added to the SDXL request - it's still far from perfect but not nearly as bad.

Works on Windows, Mac , Linux and Raspberry Pi5 (tested all four - Pi5 is dreadful... needs more RAM which would probably be quite usable - not available when writing this though)

Windows/Linux will work without a GPU but an NVIDIA Cuda-enabled GPU makes things run much faster. Without a supported GPU it will work but 16Gb RAM is really needed (it will work in 8Gb but you won't like it...)

If running Linux with a CUDA card it is important to install the latest driver and set use_cuda to True. A sample setup for an AWS G5 instance is included for reference (the fastest results by a huge margin)

It's worth noting that SDXL doesn't appear to know what many monsters look like. This is best illustrated by running with image_style set to "in the style of a cake". A fair few 'monsters' are rendered just as cakes with no monster in sight. Having said that there are a large number that produce really nice monster cakes :)

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
