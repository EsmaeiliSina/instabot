import json
import time
import random
from instagrapi import Client

cl = Client()
cl.login('USERNAME','PASSWORD')
json.dump(
    cl.get_settings(),
    open('session.json', 'w')
)

#cl = Client(json.load(open('session.json')))

media = cl.hashtag_medias_recent('python', amount=20) 

c = 0
for m in media:
    c += 1
    try:
        cl.media_like(m.id)
        cl.media_comment(m.id , '😍😍')
        print(str(c) + ': ' + m.code + '\t\tTime: ' + str(m.taken_at) + '\t\tLike: ' + str(m.like_count) + '\t\tComment: ' + str(m.comment_count))
        time.sleep(random.randint(40,60))
    except Exception as e:
        print(e.args)
print('Done')
