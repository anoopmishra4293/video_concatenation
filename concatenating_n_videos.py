from pytube import YouTube

from moviepy.editor import VideoFileClip, concatenate_videoclips

n =int(input("How many videos you want to concatenate in one: "))

urls = ['']*n

for i in range(n):
    urls[i] = input("Enter url number: "+str(i+1)+" ")

clips=[]

for i in range(n):
    file_name = "video_"+str(i)
    YouTube(urls[i]).streams.first().download(filename=file_name)
    clips.append(VideoFileClip(file_name+".mp4"))

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("my_video_concatenation.mp4")