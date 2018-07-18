from pytube import YouTube
# YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt = YouTube('https://www.youtube.com/watch?v=Db0f3w_ASw0')
st = yt.streams.filter(only_audio=True).all()
yt.streams.first().download()
print st