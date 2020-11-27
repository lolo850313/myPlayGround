def filelist(path):
	import os
	fileList=[]
	for i in os.listdir(path):
		fileList.append(path+i)
	return fileList
