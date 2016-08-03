import os
cmd4='ffmpeg -framerate 12 -i image-%5d.png -i rawaudio.wav -c:v libx264 -pix_fmt yuv420p myMovie.mov'
os.system(cmd)