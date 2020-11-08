
import cv2

path = "./SR_testset/test_spongebob.mp4"
vidcap = cv2.VideoCapture(path)
print(vidcap)

count = 0

print(vidcap.isOpened())

while(vidcap.isOpened()):
    print(1)
    ret, image = vidcap.read()

    cv2.imwrite("/workspace/HY/BasicSR/SR_testset/animation/frame%d.jpg" % count, image)

    print('Saved frame%d.jpg' % count)
    count += 1

vidcap.release()
