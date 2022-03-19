import cv2
import time
import dropbox


startTime = time.time()
print(startTime)
def takeSnap():
    capture = cv2.VideoCapture(0)
    result = True 
    while (result):
        ret, frame = capture.read()
        cv2.imwrite('myPhoto.png', frame)
        print(ret)
        result = False
    
    capture.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
     access_token = "HbkdMxYuulsAAAAAAAAAAUKKno2kLNr7kq1V5Co3NdhoEjxTbtUeCseaxow5QM9t" 
     file =img_name 
     file_from = file 
     file_to="/testFolder/"+(img_name) 
     dbx = dropbox.Dropbox(access_token) 
     with open(file_from, 'rb') as f: 
         dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
     print("file uploaded")

def main():
        while (True):
         currentTime = time.time() - startTime
         print(currentTime)
         if (currentTime >= 0):
            takeSnap()
            upload_file('myPhoto.png')
            

main()