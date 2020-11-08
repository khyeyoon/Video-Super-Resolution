import numpy as np
import cv2

cap1 = cv2.VideoCapture('./src/LR_video_HD_2.mp4')
cap2 = cv2.VideoCapture('./src/video_HD_2.mp4')

frame_count = cap2.get(cv2.CAP_PROP_FRAME_COUNT)

border_size = 2
moving_size = 10

min_moving_size = 50
max_moving_size = 1280-50

flag = 0
position = 1280//2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_4.mp4', fourcc, 10.0, (1280,720))
ret1, frame1 = cap1.read() # (540, 960, 3)
ret2, frame2 = cap2.read() # (2160, 3840, 3)

while(((ret1)!=0) and ((ret2)!=0)):

    i += 1
    print('frame',i)

    w = frame2.shape[1]
    h = frame2.shape[0]

    resized_frame1 = cv2.resize(frame1, (w, h))

    resized_frame1 = cv2.putText(resized_frame1, 'Original', (1280//2 - 200, 720//2 - 20), cv2.FONT_HERSHEY_SIMPLEX,  
        4, (0, 0, 255), 5, cv2.LINE_AA) 

    frame2 = cv2.putText(frame2, 'Ours', (1280//2 - 120, 720//2 -20), cv2.FONT_HERSHEY_SIMPLEX,  
        4, (0, 255, 0), 5, cv2.LINE_AA) 


    output_video = resized_frame1.copy()

    border = np.zeros((h, border_size*2, 3))

    output_video[:, position-border_size:position+border_size, :] = border[:,:,:]
    output_video[:, position+border_size:] = frame2[:, position+border_size:]

    # cv2.imshow('frame', output_video)

    out.write(output_video)


    ret1, frame1 = cap1.read() # (540, 960, 3)
    ret2, frame2 = cap2.read() # (2160, 3840, 3)
    
    if flag == 0:
        if position <= min_moving_size: 
            flag = 1
            continue
        position -= moving_size
    else:
        if position >= max_moving_size: 
            flag = 0
            continue
        position += moving_size
 

# When everything done, release the capture
out.release()
cap1.release()
cap2.release()
cv2.destroyAllWindows()