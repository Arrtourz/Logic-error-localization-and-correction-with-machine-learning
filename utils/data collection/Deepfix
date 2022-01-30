import os
file_dir = ".."#deepfix root, output of Drrepair
errorlist=[]
errorfold=[]
temp=[]
for root, dirs, files in os.walk(file_dir, topdown=True):
    print("root",root)     # 当前目录路径
    # print("dir", dirs)     # 当前目录下所有子目录
    print("file", files)
    print('')# 当前路径下所有非目录子文件
    if "passed_public.txt" and "error_localize_edit.txt" not in files and files!=[]:#ter all folder containing .txt file. Return index,root..
        for j in files:
            errorlist.append(j)
res=list(set(errorlist))
res.sort()
# res.remove('error_localize_edit.txt')
# res.remove('passed_public.txt')
print(len(res))
print(res)

