import pyonr

file = pyonr.Read('first.pyon')
fileData = file.readfile

fileData['khayal'] = {
    "name": "Khayal",
    "age": 14
}

file.write(fileData)