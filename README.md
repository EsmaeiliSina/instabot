# Instagram Auto like and comment 😍

## install instagrapi 
```
pip install instagrapi
```

## login

login to Instagram acc and save the session for the next time.
  ```
cl = Client()
cl.login('USERNAME','PASSWORD')
json.dump(
    cl.get_settings(),
    open('session.json', 'w')
)
```
After the first login, comment on this code and login with session file.
> Login may take a while
## login with session file
```
cl = Client(json.load(open('session.json')))
```
## Find posts with hashtags
```
media = cl.hashtag_medias_recent('python', amount=10) # get 10 recent post with python hashtag

c = 0
for m in media:
    c += 1
    try:
        cl.media_like(m.id)  
        cl.media_comment(m.id , 'comment_text') # change comment text
        print(str(c) + ': ' + m.code)           # print post code
        time.sleep(random.randint(30,60))       # sleep to avoid the account ban
    except Exception as e:
        print(e.args)

print('Done')
```
>Returning posts may take as long as the amount number of post
