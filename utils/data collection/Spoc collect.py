import os
file_dir = "/home/zhenyu/Downloads/DrRepair-master/evaluation/spoc/out_testw/code-compiler--2l-graph--finetune"
errorlist=[]
errorfold=[]
temp=[]
for root, dirs, files in os.walk(file_dir, topdown=True):
    print("root",root)     # 当前目录路径
    # print("dir", dirs)     # 当前目录下所有子目录
    print("file", files)
    print('')# 当前路径下所有非目录子文件
    if "passed_public.txt" and "passed_hidden.txt" not in files and files!=[]:#ter all folder containing .txt file. Return index,root..
        with open(root+'/error_localize_edit.txt') as f:
            f.seek(0)
            lines=f.readlines()
            for i in lines:
                if '"inp_text"' in i and "Error line UNKNOWN:"not in i:
                    for j in files:
                        errorlist.append(j)
res=list(set(errorlist))
res.sort()
# res.remove('error_localize_edit.txt')
# res.remove('passed_public.txt')
print(len(res))
print(res)
