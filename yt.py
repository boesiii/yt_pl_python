from pytube import YouTube
import subprocess

# YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()
# url = 'https://www.youtube.com/watch?v=9XaS93WMRQQ'# bad wolves zombiea
# url = 'https://www.youtube.com/watch?v=nfWlot6h_JM' #shake
# url = 'https://www.youtube.com/watch?v=ru0K8uYEZWw' #cant stop
url = 'https://www.youtube.com/watch?v=Ur0sn9abzN8' #cant stop
YouTube(url).streams.first().download()
input_filename = YouTube(url).streams.first().default_filename
output_filename = input_filename + '.mp3'

# ffmpeg -i "Lil Pump - Gucci Gang.mp4" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "Lil Pump - Gucci Gang.mp3"
command = 'ffmpeg -i ' + '\"' + input_filename + '\"' + ' -ab 160k -ac 2 -ar 44100 -vn ' + '\"' + output_filename + '\"'
subprocess.call(command, shell=True)