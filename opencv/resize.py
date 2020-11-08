import cv2


for i in range(0, 1000): 
    
    print(i)
    
    name = '/workspace/HY/BasicSR/SR_testset/landscape/frame' + str(i) + '.jpg'
    
    src = cv2.imread(name, cv2.IMREAD_COLOR)
    print(src.shape)

    dst = cv2.resize(src, dsize=(2880, 1440), interpolation=cv2.INTER_AREA)
    
    resize_path = '/workspace/HY/BasicSR/SR_testset_gt/landscape/frame' + str(i) + '.jpg'
    
    cv2.imwrite(resize_path, dst)

    
    
    

