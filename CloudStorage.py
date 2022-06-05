import dropbox

class FileTransfer(object):
    def __init__(self, accessToken):
       self.accessToken = accessToken  

    def UploadFile(self, fileFrom, fileTo):
        db = dropbox.Dropbox(self.accessToken)
        f= open(fileFrom, 'rb')
        db.files_upload(f.read(),fileTo)
        print("file uploaded")

        
def main():
    accessToken = 'sl.BD1EWu5oJ7EgqjbvQ6s27wjdyk23MdzA6ZSvH4j_s3LyAd3OQkDLM6NESkphFEBByXwj_eYe8KsGHBB5ltbLyWLArHo_UcWf-c136rE0K-TjWS9r91y5ilGCvHOkYUGOnVhx77MKWbDl'
    transferData = FileTransfer(accessToken)   
    fileFrom = input('Enter the file path you want to transfer: ')
    fileTo = input('Enter the destination you want to upload your file to dropbox: ') 
    transferData.UploadFile(fileFrom, fileTo)
   
main()