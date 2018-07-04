import os, shutil


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, dstfile)  # 移动文件
        print("move %s -> %s" % (srcfile, dstfile))


def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


def listdir(srcfile, dstfile):
    print("copy %s -> %s" % (srcfile, dstfile))
    list = os.listdir(srcfile)  # 列出目录下的所有文件和目录
    for line in list:
        print(line)
        filepath = os.path.join(srcfile, line)
        if os.path.isdir(filepath):  # 如果filepath是目录，则再列出该目录下的所有文件
            listdir(filepath, dstfile)

        elif os.path:  # 如果filepath是文件，直接列出文件名
            print(os.path.isfile(filepath))
            if os.path.isfile(filepath) and filepath[-4:] == '.zip':
                mycopyfile(filepath, dstfile + line)


srcfile = 'F:/迅雷下载/somebody@草榴社区@66部无码汉化漫画'
# srcfile = 'D:/360极速浏览器下载'
dstfile = 'H:/漫画/'

listdir(srcfile, dstfile)
