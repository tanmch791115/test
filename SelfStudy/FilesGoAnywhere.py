__author__ = 'JSBZS-tanmch'
# _*_ coding: utf-8 _*_

import os
import shutil
import time

"""
自定义异常
"""


class FGAException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


"""
拷贝指定文件到指定位置（指定文件名）,默认情况下覆盖存在的文件，如果指定的文件夹不存在，则创建该文件夹
"""


def singleFileCopy(src, dst, overWrite=True, createDir=True):
    if os.path.exists(dst) == False:  # 如果指定目的位置不存在
        dst_dir, dst_file = os.path.split(dst)
        if os.path.exists(dst_dir):
            pass
        elif (not os.path.exists(dst_dir)) and (createDir is True):
            os.mkdir(dst_dir)
        else:
            try:
                raise FGAException('目的文件夹 %s 不存在，忽略拷贝任务。如果需要创建文件夹，请设置createDir=True' % dst_dir)
            except FGAException, e:
                print e.message
            return
        shutil.copy2(src, dst)
    else:
        if overWrite is True:
            shutil.copy2(src, dst)
        else:
            try:
                raise FGAException('目的文件 %s 已存在，忽略拷贝任务。如果需要覆盖原文件，请设置overWrite=True' % dst)
            except FGAException, e:
                print e.message


"""
拷贝指定文件到指定文件夹,保持文件名不变。默认情况下覆盖存在的文件，如果指定的文件夹不存在，则创建该文件夹
"""


def singleFileCopy2(src, dst_dir, overWrite=True, createDir=True):
    src_dir, src_file = os.path.split(src)
    if not os.path.exists(dst_dir):  # 如果指定目的文件夹不存在，
        if createDir is True:  # 且createDir=True
            os.mkdir(dst_dir)
            shutil.copy2(src, os.path.join(dst_dir, src_file))
        else:  # 且createDir=False
            try:
                raise FGAException('目的文件夹 %s 不存在，忽略拷贝任务。如果需要创建文件夹，请设置createDir=True' % dst_dir)
            except FGAException, e:
                print e.message
            return
    else:  # 如果指定目的文件夹存在，
        if os.path.exists(os.path.join(dst_dir, src_file)):  # 如果目的文件存在
            if overWrite is True:
                shutil.copy2(src, os.path.join(dst_dir, src_file))
            else:
                try:
                    raise FGAException(
                        '目的文件 %s 已存在，忽略拷贝任务。如果需要覆盖原文件，请设置overWrite=True' % os.path.join(dst_dir, src_file))
                except FGAException, e:
                    print e.message
        else:  # 如果目的文件不存在
            shutil.copy2(src, os.path.join(dst_dir, src_file))


"""
拷贝指定文件夹及该文件夹下的文件到指定文件夹,保持文件夹结构、文件位置不变。默认情况下覆盖存在的文件，
如果指定的文件夹不存在，则创建该文件夹
"""


def dirCopy(src_dir, dst_dir, overWrite=True):
    if not os.path.exists(src_dir):
        try:
            raise FGAException('源文件夹 %s 不存在，忽略拷贝任务。' % src_dir)
        except FGAException, e:
            print e.message
            return
    else:
        if not os.path.exists(dst_dir):  # 如果目的文件夹不存在
            shutil.copytree(src_dir, dst_dir)
        else:  # 如果文件夹存在
            names = os.listdir(src_dir)
            for name in names:
                srcname = os.path.join(src_dir, name)
                dstname = os.path.join(dst_dir, name)
                try:
                    if os.path.isdir(srcname):
                        dirCopy(srcname, dstname, overWrite=overWrite)
                    else:
                        if not os.path.exists(dstname):
                            shutil.copy2(srcname, dstname)
                        else:
                            if overWrite is True:
                                shutil.copy2(srcname, dstname)
                            else:
                                try:
                                    raise FGAException('目的文件 %s 已存在，忽略拷贝任务。如果需要覆盖原文件，请设置overWrite=True' % dstname)
                                except FGAException, e:
                                    print e.message
                except (IOError, os.error), e:
                    print e.message


"""
遍历指定源文件夹中的所有文件，并将所有文件拷贝到目的文件夹。默认情况下覆盖存在的文件，
如果指定的文件夹不存在，则创建该文件夹,如果选择重命名，命名格式如“NN=_-rn-_=*****”
"""


def filesCollect(src_dir, dst_dir, overWrite=True, rename=False):
    if overWrite and rename is True:
        try:
            raise FGAException('overWrite 和rename不能同时为True，忽略拷贝任务。')
        except FGAException, e:
            print e.message
            return
    if not os.path.exists(src_dir):
        try:
            raise FGAException('源文件夹 %s 不存在，忽略拷贝任务。' % src_dir)
        except FGAException, e:
            print e.message
            return
    else:
        if not os.path.exists(dst_dir):  # 如果目的文件夹不存在
            os.makedirs(dst_dir)
            filesCollect(src_dir, dst_dir, overWrite=overWrite, rename=rename)
        else:  # 如果文件夹存在
            names = os.listdir(src_dir)
            for name in names:
                srcname = os.path.join(src_dir, name)
                dstname = os.path.join(dst_dir, name)
                try:
                    if os.path.isdir(srcname):
                        filesCollect(srcname, dst_dir, overWrite=overWrite, rename=rename)
                    else:
                        if not os.path.exists(dstname):
                            shutil.copy2(srcname, dstname)
                        else:
                            if overWrite is True:
                                shutil.copy2(srcname, dstname)
                            else:
                                if rename is False:  # 不对重名文件重命名
                                    try:
                                        raise FGAException(
                                            '目的文件 %s 已存在，忽略拷贝任务。如果需要覆盖原文件，请设置overWrite=True,或rename=True' % dstname)
                                    except FGAException, e:
                                        print e.message
                                else:  # 对重名文件重命名
                                    rnNO = 0
                                    while True:
                                        dirname, filename = os.path.split(dstname)
                                        if filename.find('=_-rn-_=') == -1:
                                            dstname = os.path.join(dirname, str(rnNO) + '=_-rn-_=' + '_' + filename)
                                        else:
                                            dstname = os.path.join(dirname, str(rnNO) + filename[filename.find(
                                                '=_-rn-_=') - filename.__len__():])
                                        if not os.path.exists(dstname):
                                            shutil.copy2(srcname, dstname)
                                            break
                                        rnNO = rnNO + 1
                except (IOError, os.error), e:
                    print e.message


"""
遍历指定源文件夹中的所有文件，将所有文件拷贝到目的文件夹，并按照文件日期（YYYYMMDD）创建子文件夹。默认情况下覆盖存在的文件，
如果指定的文件夹不存在，则创建该文件夹,如果选择重命名，命名格式如“NN=_-rn-_=*****”
"""

filesCollect('D:\\test', 'D:\\test2', overWrite=True, rename=True)
import re

filename = 'Z_P_LPD__C_BABJ_20180117171201_2018_01_18.txt'
html = """
  <sdf><h2>多云</h2></sdf>
  """

p = re.compile('<[^>]+>')
mat = re.findall(r'Z_', filename)
print p.sub("", html)
