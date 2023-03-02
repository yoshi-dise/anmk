import re
import os
import requests
import moviepy.editor as editor
curdir = os.getcwd()
path = os.path.join(curdir, "Animation/BorrowedMount") 
files = os.listdir(path)
vids = []
clips = []
auds = []
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
final_clip.write_videofile("BorrowedMount.mp4")
