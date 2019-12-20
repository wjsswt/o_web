import os, sys

"""
文件夹信息统计，获取每个文件的路径等信息
"""
# 设置根文件夹路径
file_basedir=r'C:\Users\swt\Desktop'
file_moudledir=r'C:\Users\swt\Desktop\发展部'
file_dir = r'C:\Users\swt\Desktop\发展部\前期工作动态'
print(file_dir.format('',file_moudledir))

# 返回指定文件夹下的所有带完整路径的文件名列表
def get_file(file_dir):
    L = []
    # 遍历指定文件夹
    for root, dirs, files in os.walk(file_dir):
        # print(root)#当前目录路径
        # print(dirs)#当前目录下所有子目录
        # print(files)#当前目录下所有非目录子文件
        if files:
            for file in files:
                L.append(os.path.join(root, file))
    print("总文件数：", len(L))
    return L

# 返回指定文件夹下的所有子目录
def get_son_dir(file_dir):
    L = []
    # 遍历指定文件夹
    for root, dirs, files in os.walk(file_dir):
        # print(root)#当前目录路径
        # print(dirs)#当前目录下所有子目录
        # print(files)#当前目录下所有非目录子文件
        L.append(dirs)
    return L[0]

#从路径中截取文件名
def get_name(file_path):
    t=os.path.basename(file_path)
    return t

# 打印列表
def list_print(L):
    for i in L:
        print(i)


# L = get_file(file_dir)
# for i in L:
#     t=get_name(i)
#     print(t,i)
# print(get_son_dir(file_dir))