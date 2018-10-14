import cv2
import sys

print "Video Frame Reduce... ",
sys.stdout.flush()

video_name = sys.argv[1]

#video_name = 'test3'

vidcap = cv2.VideoCapture("videos/"+video_name+".mp4")

success, image = vidcap.read()
count = 0
seconds = 0
while success:
    if count%30 == 0:
        cv2.imwrite("video_frames/"+video_name+"_second_%d.png" % seconds, image)     # save frame as JPEG file
        seconds += 1

    success, image = vidcap.read()
    count += 1

print("complete!")
sys.stdout.flush()
