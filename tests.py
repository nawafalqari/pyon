import pyonr

f = pyonr.Read('tests.pyon')
fd = f.readfile
fd.append('مرحباً')

f.write(fd)