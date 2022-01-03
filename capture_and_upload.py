import cv2 
import dropbox
import time
import random

from b.py.takesnapshot import takesnapshot

start_time = time.time()
def takescreenshot():
    number = random.randint(0,100)
    videotakescreenshot = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videotakescreenshot.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("screenshot taken")
    videotakescreenshot.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = " "
    file = img_name
    file_from = file
    file_to = "/test_folder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = takesnapshot()
            upload_file(name)
main()


