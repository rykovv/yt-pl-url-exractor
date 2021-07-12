import youtube_dl
import re
import json

PL_MONTHS = ['https://www.youtube.com/playlist?list=PLQTuMPSsuyeOEQ6tR8K8q1o8UDek4N8u0', # january
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeOGLSkdVHTL4VY2_Auv7AVs', # february
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeM1b2wmx1zVI30sPyIgidMh', # march
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyePHjDIFNovcPOnACQB5qujT', # april
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyePEWdxCbpwM749lKXsKqsDB', # may
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeMcKc5Tu7gxyj9aCmPRLDWy', # june
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeMPF7-7XVGqt7bnyqV9T5Es', # july
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeN16rjTDKsyoaBODGkv2dbi', # august
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeO3-CKS2lMyoxrGX5LK6rbN', # september
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyePCSvLVQ35SYprYPwn_7W2V', # october
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeMd1cziUfiJtf0ig9JSvLP8', # november
            'https://www.youtube.com/playlist?list=PLQTuMPSsuyeO0pSbJJkH7yfmJn7g1vQ5t'] # december lacks 8-22

MONTHS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})

links = {}

with ydl:
    idx = 1
    for m in PL_MONTHS:
        result = ydl.extract_info(m, download=False)

        if 'entries' in result:
            for video in result['entries']:
                links[str(idx)] = {}
                links[str(idx)]['title'] = video['title'].rsplit('-', 1)[1].strip()
                links[str(idx)]['url'] = video['webpage_url']
                links[str(idx)]['month'] = str(MONTHS.index(video['title'].rsplit('-', 1)[0].split(' ')[4].strip()[:-1].lower())+1)
                day = re.findall(r'\d+', video['title'].rsplit('-', 1)[0])
                day = ''.join(day)
                links[str(idx)]['day'] = day
                idx += 1

            print(video['title'])
        else:
            print('No entries found in request')
    
    with open('links.json', 'rb+') as fp:
        fp.write(json.dumps(links, ensure_ascii=False, indent = 2, separators=(',', ': ')).encode('utf-8'))