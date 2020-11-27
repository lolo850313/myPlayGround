#将test文件中的B改为-B
def b(file):
    import os
    arr = os.listdir(file)
    for doc in arr:
        if "B" in doc:
            arr2 = doc.split("B")
            res = arr2[0] + "-B" + arr2[1]
            os.rename(file + doc,file + res)

dir = "D:/测试/s1000d/s1000d_fim/split_From/"
b(dir)