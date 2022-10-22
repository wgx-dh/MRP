import os


test_img_path = 'E:/Download/UIE-dataset/UIEBD/train/image'
is_faster = 0
files = os.listdir(test_img_path)



for file in files:
    cmd = f'NighttimeDehazeMRP.exe {test_img_path}/{file} {is_faster}'
    print(cmd)
    os.system(cmd)