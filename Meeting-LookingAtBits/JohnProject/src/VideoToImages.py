import subprocess

p2 = subprocess.call('ffmpeg.exe -i out.MP4 -qscale:v 1 -r 30.0 outimage-%012d.jpg')
