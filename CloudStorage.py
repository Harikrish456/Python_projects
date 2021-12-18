import dropbox

class FileTransfer(object):
    def __init__(self, accessToken):
       self.accessToken = accessToken  

    def UploadFile(self, fileFrom, fileTo):
       db = dropbox.Dropbox(self.accessToken)
       f= open(fileFrom, 'rb')
       db.files_upload(f.read(),fileTo)

def main():
    accessToken = 'sl.A8Zau5-1kpkExDqDDU8nwV5jkuQBpkXFM0Zr5xojvHQDXGRau9GSwWazLqdIR_cUS6aEaNU70sMVK99lcWJzFIhyf7Bg3JYVm_v-KN5u73ScRC6589soVSy-Q5x89wBjF27RkchCWV4'
    transferData = FileTransfer(accessToken)   
    fileFrom = input('Enter the file path you want to transfer: ')
    fileTo = input('Enter the destination you want to upload your file to dropbox: ') 
    transferData.UploadFile(fileFrom, fileTo)
   
main()