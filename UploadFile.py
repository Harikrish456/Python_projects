import os
import dropbox
from dropbox.files import WriteMode

class TransferFiles(object):
    def __init__(self, accessToken):
        self.accessToken = accessToken 
        print('init')

    def upload_file(self, file_from, file_to):
        print(file_from)
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file_from):
            print('forloop1')
            for fileName in files: 
                local_path = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_path, file_from)  
                print(relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print(dropbox_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accesstoken = 'MxSzu5-OxjwAAAAAAAAAAc6wKxHUb4u2OJAsB4I17WbNkZxFe73ccz6u_TaD3Idr'
    transferData = TransferFiles(accesstoken)
    fileFrom = input('Enter the file you want to transfer: ')
    fileTo = input('Enter the destination you want to upload your file to dropbox: ')
    transferData.upload_file(fileFrom, fileTo)

main()