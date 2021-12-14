from gtts import gTTS 

# i used this to make mp3 from words.txt
# استعملتها عشان احول الكلمات الى اصوات

n = 0
with open('words.txt','r',encoding='utf-8') as f:
    for l in f.readlines():
        n +=1
        eng = l.split(',')[0]
        mytext = eng
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(f"mp3/{eng}.mp3")
        print('done',n)