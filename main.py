import youtube_dl

yt_url = 'https://www.youtube.com/playlist?list=PLQTuMPSsuyeMcKc5Tu7gxyj9aCmPRLDWy'

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
video = ""

with ydl:
    result = ydl.extract_info(yt_url, download=False)

    if 'entries' in result:
        for video in result['entries']:
            print(video['title'], video['webpage_url'])
    else:
        print('No entries found in request')
