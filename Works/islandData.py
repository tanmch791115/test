# coding=utf-8
__author__ = 'tanmch791115'


# _*_ coding: utf-8 _*_
import re
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import Queue
import os
import time
import wx
from matplotlib.figure import Figure
import matplotlib.font_manager as font_manager
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class MyException(Exception):
    '''
    自定义错误类型
    '''

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


class IslandDataUtil:
    """
    用来读取二进制文件内容的通用工具类
    """

    def readBytes(self, f, stp, n):
        """
        从文件f的第stp个字节开始读取n个字节，f为打开的文件或文件路径
        """

        if isinstance(f, file):
            f.seek(stp, 0)
            return f.read(n)
        elif isinstance(f, str):
            myFile = open(f, 'rb')
            myFile.seek(stp, 0)
            return myFile.read(n)
        else:
            return None

    def bytes2int(self, bytes):
        """
        将读取的字节转换为整型
        """
        hexstr = bytes.encode('hex')
        return int(hexstr, 16)

    def readIntFromBinFile(self, f, stp, n):
        """
        从二进制文件中读取整型变量,f为打开的文件或文件路径,从文件f的第stp个字节开始读取n个字节
        """
        bytesReaded = self.readBytes(f, stp, n)
        if bytesReaded != None and bytesReaded != '':
            return self.bytes2int(bytesReaded)
        else:
            return None


class HYZData:
    """
    用来读取海洋站数据的专用类
    """

    def __init__(self, fileName):
        self.myFile = open(fileName, 'rb')
        self.util = IslandDataUtil()

    def __close__(self):
        self.myFile.close()

    def isHYZData(self):
        """
        判断是否是海洋站数据
       """
        if self.getSysCode() == 2:
            return True
        else:
            return False
        pass

    def getStartCode(self):
        """
       获得起始码
       """
        return self.util.readIntFromBinFile(self.myFile, 0, 1)

    def getSysCode(self):
        """
       获得系统代码
       """
        return self.util.readIntFromBinFile(self.myFile, 1, 1)

    def getStationCode(self):
        """
       获得站代码
       """
        return self.util.readIntFromBinFile(self.myFile, 2, 2)

    def getPackageSum(self):
        """
       获得总包数
       """
        return self.util.readIntFromBinFile(self.myFile, 4, 1)

    def getPackageNum(self):
        """
       获得包序号
       """
        return self.util.readIntFromBinFile(self.myFile, 5, 1)

    def getYear(self):
        """
        获得观测日期的年份
        :return:str
        """
        return time.strftime("%Y", time.localtime(time.time()))[:2] + (
            '%02d' % self.util.readIntFromBinFile(self.myFile, 6, 1))

    def getMonth(self):
        """
        获得观测日期的月份
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 7, 1)

    def getDay(self):
        """
        获得观测日期的日份
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 8, 1)

    def getHour(self):
        """
        获得观测日期的小时
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 9, 1)

    def getMinute(self):
        """
        获得观测日期的分钟
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 10, 1)

    def getTimeStamp(self):
        '''
        获得年月日时分组成的时间戳
        :return:str
        '''
        # return self.getYear() + self.getMonth() + self.getDay() + self.getHour() + self.getMinute()
        return self.myFile.name.split('\\')[-1].split('.')[0][3:]

    def getAirTemperature(self):
        """
        获得气温
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 11, 2)

    def getHumidity(self):
        """
        获得湿度
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13, 2)

    def getAirPressure(self):
        """
        获得气压
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 15, 2)

    def getVisibility(self):
        """
        获得能见度
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 17, 2)

    def getWindSpeed(self):
        """
        获得10分钟平均风速
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 19, 2)

    def getWindDirection(self):
        """
        获得10分钟平均风向
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 21, 2)

    def getRain(self):
        """
        获得降水量
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 23, 3)

    def getWaterTemperature(self):
        """
        获得水温
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 26, 2)

    def getSalinity(self):
        """
        获得盐度
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 28, 3)

    def getWaterLevel(self):
        """
        获得水位
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 31, 2)

    def getVoltage(self):
        """
        获得采集器电压
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 33, 2)

    def getResetNum(self):
        """
        获得复位次数
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 35, 1)

    def getSamplingInterval(self):
        """
        获得采样间隔
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 36, 1)

    items2fuction = {'StartCode': getStartCode, 'SysCode': getSysCode, 'StationCode': getStationCode,
                     'PackageSum': getPackageSum,
                     'PackageNum': getPackageNum, 'Year': getYear, 'Month': getMonth, 'Day': getDay, 'Hour': getHour,
                     'Minute': getMinute, 'TimeStamp': getTimeStamp,
                     'AirTemperature': getAirTemperature, 'Humidity': getHumidity, 'AirPressure': getAirPressure,
                     'Visibility': getVisibility, 'WindSpeed': getWindSpeed, 'WindDirection': getWindDirection,
                     'Rain': getRain,
                     'WaterTemperature': getWaterTemperature, 'Salinity': getSalinity, 'WaterLevel': getWaterLevel,
                     'Voltage': getVoltage, 'ResetNum': getResetNum, 'SamplingInterval': getSamplingInterval}

    def get(self, item):
        '''
        根据要素名称调用相应函数，返回获得的要素值
        :param item:要素名称
        :return:
        '''
        return self.items2fuction[item](self)


class BDZData:
    """
    用来读取波导站数据的专用类
    """

    def __init__(self, fileName):
        self.myFile = open(fileName, 'rb')
        self.util = IslandDataUtil()

    def __close__(self):
        self.myFile.close()

    def isDBZData(self):
        """
        判断是否是波导站数据
       """
        if self.getSysCode() == 1:
            return True
        else:
            return False
        pass

    def getStartCode(self):
        """
       获得起始码
       """
        return self.util.readIntFromBinFile(self.myFile, 0, 1)

    def getSysCode(self):
        """
       获得系统代码
       """
        return self.util.readIntFromBinFile(self.myFile, 1, 1)

    def getStationCode(self):
        """
       获得站代码
       """
        return self.util.readIntFromBinFile(self.myFile, 2, 2)

    def getPackageSum(self):
        """
       获得总包数
       """
        return self.util.readIntFromBinFile(self.myFile, 4, 1)

    def getPackageNum(self):
        """
       获得包序号
       """
        return self.util.readIntFromBinFile(self.myFile, 5, 1)

    def getYear(self):
        """
        获得观测日期的年份
        :return:str
        """
        return time.strftime("%Y", time.localtime(time.time()))[:2] + (
            '%02d' % self.util.readIntFromBinFile(self.myFile, 6, 1))

    def getMonth(self):
        """
        获得观测日期的月份
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 7, 1)

    def getDay(self):
        """
        获得观测日期的日份
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 8, 1)

    def getHour(self):
        """
        获得观测日期的小时
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 9, 1)

    def getMinute(self):
        """
        获得观测日期的分钟
        :return:str
        """
        return '%02d' % self.util.readIntFromBinFile(self.myFile, 10, 1)

    def getTimeStamp(self):
        '''
        获得年月日时分组成的时间戳
        :return:str
        '''
        # return self.getYear() + self.getMonth() + self.getDay() + self.getHour() + self.getMinute()
        return self.myFile.name.split('\\')[-1].split('.')[0][3:]

    def getSubSysCode(self):
        """
        获得子系统代码
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 11, 1)

    def getGrads(self):
        """
        获得梯度
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 12, 1)

    def getAirTemperature(self):
        """
        获得气温
        :return:int
        """
        temps = []
        for layer in range(self.getGrads()):
            temps.append(self.util.readIntFromBinFile(self.myFile, 13 + layer * 8, 2))
        return temps

    def getHumidity(self):
        """
        获得湿度
        :return:int
        """
        humds = []
        for layer in range(self.getGrads()):
            humds.append(self.util.readIntFromBinFile(self.myFile, 15 + layer * 8, 2))
        return humds

    def getAirPressure(self):
        """
        获得气压
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8, 2)

    def getWindSpeed(self):
        """
        获得10分钟平均风速
        :return:int
        """
        wspds = []
        for layer in range(self.getGrads()):
            wspds.append(self.util.readIntFromBinFile(self.myFile, 17 + layer * 8, 2))
        return wspds

    def getWindDirection(self):
        """
        获得10分钟平均风向
        :return:int
        """
        wds = []
        for layer in range(self.getGrads()):
            wds.append(self.util.readIntFromBinFile(self.myFile, 19 + layer * 8, 2))
        return wds

    def getWaterTemperature(self):
        """
        获得水温
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8 + 2, 2)

    def getSalinity(self):
        """
        获得盐度
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8 + 4, 3)

    def getWaterLevel(self):
        """
        获得水位
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8 + 7, 2)

    def getVoltage(self):
        """
        获得采集器电压
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8 + 9, 2)

    def getCollectorTemp(self):
        """
        获得采集器温度
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8 + 11, 1)

    def getSamplingInterval(self):
        """
        获得采样间隔
        :return:int
        """
        return self.util.readIntFromBinFile(self.myFile, 13 + self.getGrads() * 8 + 13, 1)

    items2fuction = {'StartCode': getStartCode, 'SysCode': getSysCode, 'StationCode': getStationCode,
                     'PackageSum': getPackageSum,
                     'PackageNum': getPackageNum, 'Year': getYear, 'Month': getMonth, 'Day': getDay, 'Hour': getHour,
                     'Minute': getMinute,
                     'SubSysCode': getSubSysCode, 'Grads': getGrads, 'AirTemperature': getAirTemperature,
                     'Humidity': getHumidity, 'AirPressure': getAirPressure,
                     'WindSpeed': getWindSpeed, 'WindDirection': getWindDirection,
                     'WaterTemperature': getWaterTemperature, 'Salinity': getSalinity, 'WaterLevel': getWaterLevel,
                     'Voltage': getVoltage, 'CollectorTemp': getCollectorTemp, 'SamplingInterval': getSamplingInterval}

    def get(self, item):
        '''
        根据要素名称调用相应函数，返回获得的要素值
        :param item:要素名称
        :return:
        '''
        return self.items2fuction[item](self)


def getItemsLists(dir, type, items):
    '''
    获得文件夹中hyz数据文件中指定元素列表组成的字典
    :param dir:  文件路径
    :param type: 要获取的文件类型
    :param items: 要获取的元素list
    :param itemQuesLength: 可选，指定绘图x坐标长度
    :return:dct
    '''
    type2DataClass = {'hyz': HYZData, 'bdz': BDZData}
    dir = dir
    items = items
    type = type
    if not os.path.exists(dir):
        try:
            raise MyException('源文件夹 %s 不存在，忽略拷贝任务。' % dir)
        except MyException, e:
            print e.message
            return None
    # itemsQues = {}
    itemsLists = {}
    for item in items:
        itemsLists[item] = []
    # for item in items:
    #     itemsQues[item] = Queue.Queue(itemQuesLength)
    names = os.listdir(dir)
    for name in names:
        if name.startswith(type):
            fileFullName = os.path.join(dir, name)
            print 'Processing ' + fileFullName
            if os.path.isdir(fileFullName):
                try:
                    raise MyException('%s是文件夹，跳过该文件夹。' % fileFullName)
                except MyException, e:
                    print e.message
                    continue
            myData = type2DataClass[type](fileFullName)
            for item in items:
                itemsLists[item].append(myData.get(item))
                print 'Decoding ' + item
            myData.__close__()
        else:
            pass
    return itemsLists


def getLastItemsLists(dir, type, items, length=10):
    """
    获得文件夹中hyz数据文件中指定元素最近的length=10个值列表组成的字典
    :param dir:
    :param type:
    :param items:
    :return:{‘item1’:[1,2,3,4],‘item2’:[1,2,3,4]}
    """
    itemsLists = getItemsLists(dir, type, items)
    lastItemsLists = {}
    for item in itemsLists.keys():
        lastItemsLists[item] = itemsLists[item] if itemsLists[item].__len__() <= length else itemsLists[item][-length:]
    return lastItemsLists


# wxWidgets object ID for the timer
TIMER_ID = wx.NewId()
# number of data points
POINTS = 10


class PlotFigure(wx.Frame):
    ItemsLists = {}

    """Matplotlib wxFrame with animation effect"""

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="HYZ Items", size=(800, 600))
        # Matplotlib Figure
        self.fig = Figure((4, 3), 100)
        # bind the Figure to the backend specific canvas
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.fig)
        # add a subplot
        self.ax_Humidity = self.fig.add_subplot(221)
        # limit the X and Y axes dimensions
        self.ax_Humidity.set_ylim([0, 100])
        self.ax_Humidity.set_xlim([0, POINTS])
        self.ax_Humidity.set_autoscale_on(False)
        self.ax_Humidity.set_xticks([])
        # we want a tick every 10 point on Y (101 is to have 10
        self.ax_Humidity.set_yticks(range(0, 101, 10))
        # disable autoscale, since we don't want the Axes to ad
        # draw a grid (it will be only for Y)
        self.ax_Humidity.grid(True)
        # generates first "empty" plots
        self.user_Humidity_Y = [None] * POINTS
        self.user_Humidity_X = [None] * POINTS
        self.l_user_Humidity, = self.ax_Humidity.plot(range(POINTS), self.user_Humidity_Y, label='Humidity')
        # add the legend
        self.ax_Humidity.legend(loc='upper center',
                                ncol=4,
                                prop=font_manager.FontProperties(size=10))

        self.ax_AirPressure = self.fig.add_subplot(222)
        # limit the X and Y axes dimensions
        self.ax_AirPressure.set_ylim([0, 100])
        self.ax_AirPressure.set_xlim([0, POINTS])
        self.ax_AirPressure.set_autoscale_on(False)
        self.ax_AirPressure.set_xticks([])
        # we want a tick every 10 point on Y (101 is to have 10
        self.ax_AirPressure.set_yticks(range(0, 101, 10))
        # disable autoscale, since we don't want the Axes to ad
        # draw a grid (it will be only for Y)
        self.ax_AirPressure.grid(True)
        # generates first "empty" plots
        self.user_AirPressure_Y = [None] * POINTS
        self.user_AirPressure_X = [None] * POINTS
        self.l_user_AirPressure, = self.ax_AirPressure.plot(range(POINTS), self.user_AirPressure_Y, label='AirPressure')
        # add the legend
        self.ax_AirPressure.legend(loc='upper center',
                                   ncol=4,
                                   prop=font_manager.FontProperties(size=10))







        # force a draw on the canvas()
        # trick to show the grid and the legend
        self.canvas.draw()
        # save the clean background - everything but the line
        # is drawn and saved in the pixel buffer background
        self.bg = self.canvas.copy_from_bbox(self.ax_Humidity.bbox)
        # bind events coming from timer with id = TIMER_ID
        # to the onTimer callback function
        wx.EVT_TIMER(self, TIMER_ID, self.onTimer)

    def onTimer(self, evt):
        """callback function for timer events"""
        # restore the clean background, saved at the beginning
        # self.canvas.restore_region(self.bg)
        # update the data
        lastItemsLists = getLastItemsLists(r'D:\PYcharmProjects\Works\islandData', 'hyz',
                                           ['TimeStamp', 'Humidity', 'AirPressure'])
        if (self.ItemsLists.keys() == lastItemsLists.keys()) and self.ItemsLists['TimeStamp'][-1] == \
                lastItemsLists['TimeStamp'][-1]:
            pass
        else:
            self.ItemsLists = lastItemsLists

            self.user_Humidity_Y = self.user_Humidity_Y[:-lastItemsLists['Humidity'].__len__()] + lastItemsLists[
                'Humidity']
            self.user_Humidity_X = self.user_Humidity_X[:-lastItemsLists['TimeStamp'].__len__()] + lastItemsLists[
                'TimeStamp']
            # update the plot
            self.l_user_Humidity.set_ydata(self.user_Humidity_Y)
            self.l_user_Humidity.set_xdata(range(0, POINTS))
            self.ax_Humidity.set_xticks(range(0, POINTS))
            self.ax_Humidity.set_xticklabels(self.user_Humidity_X, rotation=90)
            self.ax_Humidity.set_yticks(range(0,100,10))
            # self.Count = self.Count + 1
            self.ax_Humidity.set_xlim([0, POINTS])
            self.ax_Humidity.set_ylim([min(lastItemsLists['Humidity']), max(lastItemsLists['Humidity'])])
            self.canvas.draw()



            self.user_AirPressure_Y = self.user_AirPressure_Y[:-lastItemsLists['AirPressure'].__len__()] + \
                                      lastItemsLists['AirPressure']
            self.user_AirPressure_X = self.user_AirPressure_X[:-lastItemsLists['TimeStamp'].__len__()] + lastItemsLists[
                'TimeStamp']
            # update the plot
            self.l_user_AirPressure.set_ydata(self.user_AirPressure_Y)
            self.l_user_AirPressure.set_xdata(range(0, POINTS))
            self.ax_AirPressure.set_xticks(range(0, POINTS))
            self.ax_AirPressure.set_xticklabels(self.user_AirPressure_X, rotation=90)
            self.ax_AirPressure.set_yticks(range(0,2000,100))
            # self.Count = self.Count + 1
            self.ax_AirPressure.set_xlim([0, POINTS])
            self.ax_AirPressure.set_ylim([min(lastItemsLists['AirPressure']), max(lastItemsLists['AirPressure'])])
            self.canvas.draw()


            self.canvas.blit(self.ax_Humidity.bbox)

    def __del__(self):
        t.Stop()

        #   def main():
        # print getItemsLists(r'D:\PYcharmProjects\Works\islandData','hyz',['TimeStamp', 'AirTemperature', 'Humidity', 'AirPressure'])


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = PlotFigure()
    t = wx.Timer(frame, TIMER_ID)
    t.Start(1000)
    frame.Show()
    app.MainLoop()
