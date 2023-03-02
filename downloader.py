import requests
import re
import os
import moviepy.editor as editor

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
with open("target.txt", "r") as titlesfile:
    titles = titlesfile.read().split("\n")[:-1]
    baselink = "https://cdn.animatic.fun/PUBLIC/{title}/media/{filename}"
    curdir = os.getcwd()
    try:
        os.mkdir(os.path.join(curdir, "Animation"))
    except OSError as e:
        pass
        
    for title in titles:
        path = os.path.join(curdir, "Animation/" + title) 
        try:
            os.mkdir(path)
        except OSError as e:
            pass

        print("Downloading {} ...".format(title))
        failedReqs = 0
        for x in range(1, 40):
            if(failedReqs > 3):
                break
            print("Downloading {} chunk of {}".format(ordinal(x), title))
            res = requests.get(baselink.format(title=title, filename=f"{x:02d}"+"I.mp4"))
            filename=f"{x:02d}"+"I.mp4"
            if res.status_code == 403:
                res = requests.get(baselink.format(title=title, filename=f"{x:02d}"+"L.mp4"))
                filename=f"{x:02d}"+"L.mp4"
            # if the response code is still 403 then somehow the video id got skipped by them
            if res.status_code == 403:
                failedReqs = failedReqs + 1
                continue
            failedReqs = 0
            fl = open("{}/{}".format(path, filename), "wb")
            fl.write(res.content)

            resAud = requests.get(baselink.format(title=title, filename=f"{x:02d}"+"I.mp3"))
            filename=f"{x:02d}"+"I.mp3"
            if resAud.status_code == 403:
                resAud = requests.get(baselink.format(title=title, filename=f"{x:02d}"+"LA.mp3"))
                filename=f"{x:02d}"+"LA.mp3"
            # if the response code is still 403 then somehow the video id got skipped by them
            if resAud.status_code == 403:
                failedReqs = failedReqs + 1
                continue
            failedReqs = 0
            flAd = open("{}/{}".format(path, filename), "wb")
            flAd.write(resAud.content)
        
        files = os.listdir(path)
        vids = []
        auds = []
        clips = []
        for fl in files:
            if fl.endswith("mp3"):
                auds.append(fl)
            else:
                vids.append(fl)
        vids = sorted(vids, key=lambda x: int(x[:2]))
        auds = sorted(auds, key=lambda x: int(x[:2]))
        offset = 0
        for idx, vid in enumerate(vids):
            clip = editor.VideoFileClip(path+"/"+vid)
            try:
                aclip = editor.AudioFileClip(path+"/"+auds[idx - offset])
                clip = clip.set_audio(aclip)
            except:
                offset = offset + 1

            clips.append(clip)
        final_clip = editor.concatenate_videoclips(clips)
        final_clip.write_videofile("Animation/{}.mp4".format(title))

        

        


            

