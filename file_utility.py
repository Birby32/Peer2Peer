import os
PATH = 'C:\\Users\\odoma\\OneDrive\\Documents\\GitHub\\Peer2Peer'

def list_files():
    files = os.listdir(PATH)
    for f in files:
        print(f)

def getDirectory():
    files = os.listdir(PATH)
    return files
