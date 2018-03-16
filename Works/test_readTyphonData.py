# _*_ coding: utf-8 _*_

from pandas import Series, DataFrame
from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np
from datetime import datetime
from pandas.tseries.offsets import Day
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.path as pth
from math import *
import os
import requests

import PIL.Image as pimg
import matplotlib.image as mpimg
from io import BytesIO

font_set = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=15)
# 记录开始时间
startTime = datetime.now()

# DataDir为台风数据目录
DataDir = 'D:\\Documents\\PYcharmProjects\\Typhoon'
# columns为台风信息字段名
columns = ['Indicator', 'International number ID', 'Number of data lines', 'Tropical cyclone number ID',
           'Chinese number ID', 'Flag of the last data line', 'Interval time of record', 'Name of the storm',
           'Date of the latest revision']
# pathColums为台风路径字段名
pathColumns = ['Date', 'I', 'LAT', 'LONG', 'PRES', 'WND', 'OWD']

typhoonList = list()  # 台风列表
typhoonPathList = list()  # 台风路径列表
typhoonDict = {}  # 台风信息字典

# 读取台风数据###########################################################################################################
for parent, dirs, fileNames in os.walk(DataDir):  # 遍历文件夹
    for fileName in fileNames:  # 遍历所有文件
        print(fileName)
        currentFileName = fileName  # 当前读取的文件名
        DataFile = open(os.path.join(parent, fileName))
        while True:
            Line = DataFile.readline()
            if not Line:  # 读完最后一行

                typhoonDict['Path'] = DataFrame(typhoonPathList)  # 将当前台风的路径添加到台风字典
                if typhoonList.__len__() == 0:  # 如果是读取的第一个台风，即台风列表为空，建立台风列表
                    typhoonList = [typhoonDict]
                else:  # 如果不是第一个台风，向台风列表中追加
                    typhoonList.append(typhoonDict)
                typhoonDict = {}  # 清空台风信息字典
                break

            if Line.startswith('66666'):  # 如果该行以66666开头，该行为台风信息

                if typhoonDict.__len__() == 0:  # 前面没有另一个台风，构建当前台风信息的字典
                    typhoonDict = dict(zip(columns, Line.split()))
                else:  # 如果前面有一个台风，说明已经读取了前一个台风的所有路径信息，首先把前一个台风的路径添加到台风字典，并把加入台风列表
                    typhoonDict['Path'] = DataFrame(typhoonPathList)
                    if typhoonList.__len__() == 0:
                        typhoonList = [typhoonDict]
                    else:
                        typhoonList.append(typhoonDict)
                    typhoonDict = dict(zip(columns, Line.split()))  # 构建当前台风信息的字典

                typhoonPathList = list()  # 清空当前台风的路径列表
            else:  # 如果该行不是以66666开头，则该行是台风路径信息
                if Line.split().__len__() == 6:  # 路径信息为6个字段

                    # tmp=[int(x) for x in Line.split()]
                    # tmp[0]=str(tmp[0])

                    # typhoonPathSeries = pd.Series(tmp, index=pathColumns[:6])
                    typhoonPathSeries = pd.Series(Line.split(), index=pathColumns[:6])
                elif Line.split().__len__() == 7:  # 路径信息为7个字段

                    # tmp=[int(x) for x in Line.split()]
                    # tmp[0]=str(tmp[0])

                    typhoonPathSeries = pd.Series(Line.split(), index=pathColumns)
                # 构建台风路径列表
                if typhoonPathList.__len__() == 0:
                    typhoonPathList = [typhoonPathSeries]
                else:
                    typhoonPathList.append(typhoonPathSeries)
        DataFile.close()
typhoonDF = DataFrame(typhoonList)  # 构建台风DataFrame


# 利用Basemap画台风路径##################################################################################################
# 在ax指定的坐标中绘制地图
def draw_Map(ax=None):
    map = Basemap(llcrnrlon=0, llcrnrlat=0, urcrnrlon=360, urcrnrlat=90, ax=ax, projection='cyl', lat_0=0, lon_0=120,
                  resolution='l',width=3600,height=900)
    # 画海岸线和国家边界
    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)
    # 画投影区域边界
    map.drawmapboundary(fill_color='#689CD2')
    # 画经纬度网格
    map.drawmeridians(np.arange(0, 360, 10), labels=[0, 0, 0, 1])
    map.drawparallels(np.arange(-90, 100, 10), labels=[1, 0, 0, 0])
    # 填充大陆海洋颜色
    map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)
    return map


# 在ax指定的坐标中绘制typhoons给定的台风路径
def draw_typhoon_paths(typhoons, map=None, ax=None):
    pointColors = Series(
        ['#FFFFFF', '#00E400', '#065FB8', '#FFFF00', '#FF7E00', '#FF0000', '#750021', '#000000', '#000000'
            , '#FFFFFF'], index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if map == None:
        map = Basemap(llcrnrlon=60, llcrnrlat=0, urcrnrlon=270, urcrnrlat=60, ax=ax, projection='cyl', lat_0=0,
                      lon_0=120, resolution='l')
        # 画海岸线和国家边界
        map.drawcoastlines(linewidth=0.25)
        map.drawcountries(linewidth=0.25)
        # 画投影区域边界
        map.drawmapboundary(fill_color='#689CD2')
        # 画经纬度网格
        map.drawmeridians(np.arange(0, 360, 10), labels=[0, 0, 0, 1])
        map.drawparallels(np.arange(-90, 100, 10), labels=[1, 0, 0, 0])
        # 填充大陆海洋颜色
        map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)

    paths = typhoons['Path']

    for apath in paths:
        lons = [float(i) / 10 for i in apath['LONG']]
        lats = [float(i) / 10 for i in apath['LAT']]
        I = apath['I'].values
        # 计算投影后要绘制的点的经纬度坐标
        x, y = map(lons, lats)
        map.plot(x, y, color='#000000')
        # 标记台风生成时间
        plt.text(x[0], y[0], apath.ix[0]['Date'])
        for x1, y1, I1 in zip(x, y, I):
            map.scatter(x1, y1, s=50, marker='.', color=pointColors[I1])


# 在ax指定的坐标中绘制指定年份years和月份months的台风路径
def draw_typhoon_paths_by_time(years={}, months={}, map=None, ax=None):
    if map == None:
        map = Basemap(llcrnrlon=60, llcrnrlat=0, urcrnrlon=210, urcrnrlat=60, ax=ax, projection='cyl', lat_0=0,
                      lon_0=120, resolution='l')
        # 画海岸线和国家边界
        map.drawcoastlines(linewidth=0.25)
        map.drawcountries(linewidth=0.25)
        # 画投影区域边界
        map.drawmapboundary(fill_color='#689CD2')
        # 画经纬度网格
        map.drawmeridians(np.arange(0, 360, 30), labels=[0, 0, 0, 1])
        map.drawparallels(np.arange(-90, 100, 30), labels=[1, 0, 0, 0])
        # 填充大陆海洋颜色
        map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)
    typhoons = typhoonDF[
        [(len(months.intersection(
            set((datetime.strptime(date, '%Y%m%d%H%M').month) for date in path['Date'][0:1]))) > 0) &
         (len(years.intersection(set((datetime.strptime(date, '%Y%m%d%H%M').year) for date in path['Date'][0:1]))) > 0)
         for path
         in typhoonDF['Path']]]  # {1950}指定年份{1,12}指定月份生成的台风
    draw_typhoon_paths(typhoons, map=map)


# 在ax指定的坐标中绘制指定年份years和指定月份months台风的起始位置
def draw_typhoon_startpoints_by_time(years={}, months={}, ax=None, map=None):
    # 不同的台风级别用不同的颜色标记
    pointColors = Series(
        ['#FFFFFF', '#00E400', '#065FB8', '#FFFF00', '#FF7E00', '#FF0000', '#750021', '#000000', '#000000'
            , '#FFFFFF'], index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if map == None:
        map = Basemap(llcrnrlon=60, llcrnrlat=0, urcrnrlon=210, urcrnrlat=60, ax=ax, projection='cyl', lat_0=0,
                      lon_0=120, resolution='l')
    # # 画海岸线和国家边界
    # map.drawcoastlines(linewidth=0.25)
    # map.drawcountries(linewidth=0.25)
    # # 画投影区域边界
    # map.drawmapboundary(fill_color='#689CD2')
    # # 画经纬度网格
    # map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,0,1])
    # map.drawparallels(np.arange(-90, 100, 30),labels=[1,0,0,0])
    # # 填充大陆海洋颜色
    # map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)
    typhoons = typhoonDF[
        [(len(months.intersection(
            set((datetime.strptime(date, '%Y%m%d%H%M').month) for date in path['Date'][0:1]))) > 0) &
         (len(years.intersection(set((datetime.strptime(date, '%Y%m%d%H%M').year) for date in path['Date'][0:1]))) > 0)
         for path in typhoonDF['Path']]]  # {1950}指定年份{1,12}指定月份生成的台风
    paths = typhoons['Path']
    for apath in paths:
        lons = [float(i) / 10 for i in apath['LONG'][0:1]]
        lats = [float(i) / 10 for i in apath['LAT'][0:1]]
        I = apath['I'][0:1].values
        # 计算投影后要绘制的点的经纬度坐标
        x, y = map(lons, lats)
        for x1, y1, I1 in zip(x, y, I):
            map.scatter(x1, y1, s=50, marker='.', color=pointColors[I1])


# 在map指定的地图上以point_Lat,point_Long为圆心，画半径为k公里的圆
def draw_circle(point_Lat, point_Long, k, map=None):
    angles_circle = [i * pi / 180 for i in range(0, 360)]
    x = [cos(angle) for angle in angles_circle]
    y = [sin(angle) for angle in angles_circle]
    lat = (np.array(y) * float(k) / 111.31955 + point_Lat).tolist()
    lng = [(xx * float(k) / (111.31955 * cos(lat1 * pi / 180)) + point_Long) for xx, lat1 in zip(x, lat)]
    lng, lat = map(lng, lat)
    plt.plot(lng, lat, 'r')


# 在map指定的地图上以point_Lat,point_Long为左上角绘制文本text
def draw_text(point_Lat, point_Long, text, map=None):
    long, lat = map(point_Long, point_Lat)
    plt.text(long, lat, text)


# 在map指定的地图上以Lat_A,Long_A为起点，Lat_B，Long_B为终点绘制颜色为c的矩形
def draw_rectangel(Lat_A, Long_A, Lat_B, Long_B, color, alpha, map=None):
    pA_long, pA_lat = map((Long_A), (Lat_A))
    pB_long, pB_lat = map((Long_B), (Lat_B))
    rctg = plt.Rectangle((pA_long, pA_lat), pB_long - pA_long, pB_lat - pA_lat, alpha=alpha, facecolor='none',
                         edgecolor='red')
    # rctg=plt.Rectangle((pA_long,pA_lat),pB_long-pA_long,pB_lat-pA_lat,color=color,alpha=alpha,facecolor='none')
    ax = plt.subplot(1, 1, 1)
    ax.add_patch(rctg)

def draw_rectangel2(Lat_A, Long_A, Lat_B, Long_B, color, alpha, map=None):
    pA_long, pA_lat = map((Long_A), (Lat_A))
    pB_long, pB_lat = map((Long_B), (Lat_B))
    rctg = plt.Rectangle((pA_long, pA_lat), pB_long - pA_long, pB_lat - pA_lat, alpha=alpha, facecolor=color,
                         edgecolor=color)
    # rctg=plt.Rectangle((pA_long,pA_lat),pB_long-pA_long,pB_lat-pA_lat,color=color,alpha=alpha,facecolor='none')
    ax = plt.subplot(1, 1, 1)
    ax.add_patch(rctg)


# 计算给定的两个坐标点(Lat_A,Long_A）,（Lat_B,Long_B)之间的距离#########################################################
def calcDistance(Lat_A, Long_A, Lat_B, Long_B):  # 给经纬度算距离
    ra = 6378.140  # 赤道半径(km）
    rb = 6356.755  # 极半径(km)
    flatten = (ra - rb) / ra  # 地球偏率
    rad_lat_A = radians(Lat_A)
    rad_lat_B = radians(Lat_B)
    rad_long_A = radians(Long_A)
    rad_long_B = radians(Long_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_long_A - rad_long_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance


def calcDistance2(Lat_A, Long_A, Lat_B, Long_B):  # 给经纬度算距离
    a = radians(Lat_A) - radians(Lat_B)
    b = radians(Long_A) - radians(Long_B)
    s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(radians(Lat_A)) * cos(radians(Lat_B)) * pow(sin(b / 2), 2)))
    earth_radius = 6378.137
    s = s * earth_radius
    if s < 0:
        return -s
    else:
        return s


def calcDistance3(Lat_A, Long_A, Lat_B, Long_B):  # 给定经纬度坐标，按照平面直角坐标系计算距离
    s = sqrt((Long_B - Long_A) ** 2 + (Lat_B - Lat_A) ** 2)
    return s


def calcDistance4(Lat_A, Long_A, Lat_B, Long_B, Lat_C, Long_C):  # 计算点C到由点A、B确定的直线的距离
    A = float(Lat_B - Lat_A)
    B = float(Long_B - Long_A)
    if B == 0:
        return abs(A)
    else:
        k = A / B
        s = abs(k * (Long_C - Long_B) - (Lat_C - Lat_B)) / sqrt(1 + k ** 2)
        return s


# 计算某一坐标点Lat_A,Long_A距离某条台风路径Path上所有节点的最近距离###############################################################
def calcMinDistance(Lat_A, Long_A, Path):
    path_points = [(float(lat) / 10, float(lon) / 10) for lat, lon in zip(Path['LAT'], Path['LONG'])]
    minDist = min([calcDistance2(Lat_A, Long_A, Lat_B, Long_B) for Lat_B, Long_B in path_points])
    return minDist


# 计算路径Path_A到路径Path_B的平均Hausdorff距离##########################################################################
def calcAverageHausdorfDist(Path_A=None, Path_B=None):
    path_points_A = [(float(lat) / 10, float(lon) / 10) for lat, lon in zip(Path_A['LAT'], Path_A['LONG'])]
    # path_points_B=[(float(lat)/10,float(lon)/10) for lat,lon in zip(Path_B['LAT'],Path_B['LONG'])]
    avHsdfDist = np.average([calcMinDistance(lat_A, lon_A, Path_B) for lat_A, lon_A in path_points_A])
    pass
    return avHsdfDist


# 判断台风路径Path是否经过Lat_A,Lon_A,Lat_B,Lon_B确定的矩形区域
def ifPassRectangle(Lat_A, Lon_A, Lat_B, Lon_B, path):
    for indx in path.index:
        point_Lat = float(path.ix[indx]["LAT"]) / 10
        point_Lon = float(path.ix[indx]["LONG"]) / 10
        if (point_Lat >= min(Lat_A, Lat_B)) & (point_Lat <= max(Lat_A, Lat_B)) & (point_Lon >= min(Lon_A, Lon_B)) & (
                    point_Lon <= max(Lon_A, Lon_B)):
            return True
        else:
            pass
    return False

# 判断台风路径Path是否经过Lat_A,Lon_A,Lat_B,Lon_B确定的矩形区域,且在该区域内达到级别I
def ifReachIntensityInRectangel(Lat_A, Lon_A, Lat_B, Lon_B,I, path):
    for indx in path.index:
        point_Lat = float(path.ix[indx]["LAT"]) / 10
        point_Lon = float(path.ix[indx]["LONG"]) / 10
        Intensity=int(path.ix[indx]['I'])
        if (point_Lat >= min(Lat_A, Lat_B)) & (point_Lat <= max(Lat_A, Lat_B)) & (point_Lon >= min(Lon_A, Lon_B)) & (
                    point_Lon <= max(Lon_A, Lon_B)):
            if Intensity>=I:
                return True
        else:
            pass
    return False


# 判断台风路径Path是否起始于Lat_A,Lon_A,Lat_B,Lon_B确定的矩形区域
def ifStartFromRectangle(Lat_A, Lon_A, Lat_B, Lon_B, path):
    startPoint_Lat = float(path.ix[path.index[0]]['LAT']) / 10
    startPoint_Long = float(path.ix[path.index[0]]['LONG']) / 10
    if (startPoint_Lat >= min(Lat_A, Lat_B)) & (startPoint_Lat <= max(Lat_A, Lat_B)) & (
                startPoint_Long >= min(Lon_A, Lon_B)) & (startPoint_Long <= max(Lon_A, Lon_B)):
        return True
    else:
        return False


# 判断台风路径Path是否经过以点Lat，Long为中心，半径为R公里的圆形缓冲区域
def ifPassBufferCycle(Lat, Long, R, Path):
    dist = calcMinDistance(Lat, Long, Path)
    if dist > R:
        return False
    else:
        return True


# 判断台风路径Path是否起始于以点Lat，Long为中心，半径R公里的圆形区域内
def ifStartFromCycle(Lat, Long, R, Path):
    startPoint_Lat = float(Path.ix[Path.index[0]]['LAT']) / 10
    startPoint_Long = float(Path.ix[Path.index[0]]['LONG']) / 10
    dist = calcDistance(Lat, Long, startPoint_Lat, startPoint_Long)
    if dist > R:
        return False
    else:
        return True


# 判断台风路径path生成时间是否在时间Date的前后k天
def ifTyphoonInPeriod(path, Date, k):
    date = datetime.strptime(path.ix[0]['Date'], '%Y%m%d%H%M')
    if (date <= (Date + k * Day())) & (date >= (Date - k * Day())):
        return True
    else:
        return False


# 判断台风路径path生成时间是否在Mon_First月Day_First日到Mon_Second月Day_Second日之间
def ifTyphoonInPeriod2(path, Mon_First, Day_First, Mon_Second, Day_Second):
    date = datetime.strptime(path.ix[0]['Date'], '%Y%m%d%H%M')
    c = (date.month == Mon_First) & (date.day >= Day_First)
    d = (date.month == Mon_Second) & (date.day <= Day_Second)
    if (((date.month == Mon_First) & (date.day >= Day_First)) | (
                (date.month == Mon_Second) & (date.day <= Day_Second))):
        return True
    else:
        return False


# 判断台风typhoon是否达到等级I(路径上至少有一个点的等级等于或大于I)
def ifTyphoonReachIntensity(typhoon, I):
    path = typhoon['Path']
    for i in np.arange(len(path)):
        point = path.ix[path.index[i]]
        if int(point['I']) >= I:
            return True
    return False


# 检索台风集合typhoons中等级达到等级I的台风
def getTyphoonsReachIntensity(typhoons, I):
    myfilter = []
    for i in np.arange(len(typhoons)):
        if (ifTyphoonReachIntensity(typhoons.ix[typhoons.index[i]], I)):
            myfilter.append(True)
        else:
            myfilter.append(False)
    return typhoons[myfilter]


# 判断台风typhoon在点C（经纬度）为中心R（公里）为半径的区域内是否达到等级I
def ifTyphoonReachIntensityInCycle(typhoon, I, C_LAT, C_LONG, R):
    path = typhoon['Path']
    for i in np.arange(len(path)):
        point = path.ix[path.index[i]]
        if (int(point['I']) >= I) & (
                    calcDistance2(float(point['LAT']) / 10, float(point['LONG']) / 10, C_LAT, C_LONG) <= R):
            return True
    return False


# 判断台风路径path是否达到等级I
def ifTyphoonReachIntensity(path, I):
    for idx in path.index:
        a = path.ix[idx]['I']
        if (int(path.ix[idx]['I']) >= I) & (int(path.ix[idx]['I']) != 9):
            return True
        else:
            pass
    return False


# 检索台风集合typhoons中在点C（经纬度）为中心R（公里）为半径的区域内达到等级I的台风
def getTyphoonsReachIntensityInCycle(typhoons, I, C_LAT, C_LONG, R):
    myfilter = []
    for i in np.arange(len(typhoons)):
        if (ifTyphoonReachIntensityInCycle(typhoons.ix[typhoons.index[i]], I, C_LAT, C_LONG, R)):
            myfilter.append(True)
        else:
            myfilter.append(False)
    return typhoons[myfilter]


# 判断台风typhoon的中心最低气压是否小于等于P（hPa）(路径上至少有一个点的中心气压<=P)
def ifTyphoonReachPressure(typhoon, P):
    path = typhoon['Path']
    for i in np.arange(len(path)):
        point = path.ix[path.index[i]]
        if float(point['PRES']) <= P:
            return True
    return False


# 检索台风集合typhoons中的中心最低气压小于等于P（hPa）(路径上至少有一个点的中心气压<=P)的台风
def getTyphoonsReachPressure(typhoons, P):
    myfilter = []
    for i in np.arange(len(typhoons)):
        if (ifTyphoonReachPressure(typhoons.ix[typhoons.index[i]], P)):
            myfilter.append(True)
        else:
            myfilter.append(False)
    return typhoons[myfilter]


# 判断台风typhoon在点C（经纬度）为中心R（公里）为半径的区域内中心最低气压是否小于等于P（hPa）
def ifTyphoonReachPressureInCycle(typhoon, P, C_LAT, C_LONG, R):
    path = typhoon['Path']
    for i in np.arange(len(path)):
        point = path.ix[path.index[i]]
        if (float(point['PRES']) <= P) & (
                    calcDistance2(float(point['LAT']) / 10, float(point['LONG']) / 10, C_LAT, C_LONG) <= R):
            return True
    return False


# 检索台风集合typhoons中在点C（经纬度）为中心R（公里）为半径的区域内中心最低气压小于等于P（hPa）的台风
def getTyphoonsReachPressureInCycle(typhoons, P, C_LAT, C_LONG, R):
    myfilter = []
    for i in np.arange(len(typhoons)):
        if (ifTyphoonReachPressureInCycle(typhoons.ix[typhoons.index[i]], P, C_LAT, C_LONG, R)):
            myfilter.append(True)
        else:
            myfilter.append(False)
    return typhoons[myfilter]


# 判断台风typhoon的2分钟近中心最大风速是否大于等于W（m/s）(路径上至少有一个点的2分钟近中心最大风速》=W)
def ifTyphoonReachWindSpeed(typhoon, W):
    path = typhoon['Path']
    for i in np.arange(len(path)):
        point = path.ix[path.index[i]]
        if float(point['WND']) >= W:
            return True
    return False


# 检索台风集合typhoons中2分钟近中心最大风速大于等于W（m/s）(路径上至少有一个点的2分钟近中心最大风速》=W)的台风
def getTyphoonsReachWindSpeed(typhoons, W):
    myfilter = []
    for i in np.arange(len(typhoons)):
        if (ifTyphoonReachWindSpeed(typhoons.ix[typhoons.index[i]], W)):
            myfilter.append(True)
        else:
            myfilter.append(False)
    return typhoons[myfilter]


# 判断台风typhoon在点C（经纬度）为中心R（公里）为半径的区域内2分钟近中心最大风速是否大于等于W（m/s）
def ifTyphoonReachWindSpeedInCycle(typhoon, W, C_LAT, C_LONG, R):
    path = typhoon['Path']
    for i in np.arange(len(path)):
        point = path.ix[path.index[i]]
        if (float(point['WND']) >= W) & (
                    calcDistance2(float(point['LAT']) / 10, float(point['LONG']) / 10, C_LAT, C_LONG) <= R):
            return True
    return False


# 检索台风集合typhoons在点C（经纬度）为中心R（公里）为半径的区域内2分钟近中心最大风速大于等于W（m/s）的台风
def getTyphoonsReachWindSpeedInCycle(typhoons, W, C_LAT, C_LONG, R):
    myfilter = []
    for i in np.arange(len(typhoons)):
        if (ifTyphoonReachWindSpeedInCycle(typhoons.ix[typhoons.index[i]], W, C_LAT, C_LONG, R)):
            myfilter.append(True)
        else:
            myfilter.append(False)
    return typhoons[myfilter]


# 用DouglasPecker法对给定的一个路径path进行约减(算法貌似有问题，对2014年7月17日的一条路径约减时递归溢出)
def simplifyPath_DougsPeucker(path):
    def DouglasPeucker(points):  # 用Douglaspeucker对给定的一条曲线的节点列表进行约减
        dist = -1
        max_dist_point = (-1, -1)
        for (i, j) in points:
            dist_tmp = calcDistance4(points[0][1], points[0][0], points[-1][1], points[-1][0], j, i)
            if dist_tmp > dist:
                max_dist_point = (i, j)
                dist = dist_tmp
        if dist < 2:  # DouglasPeucker阈值
            for (i, j) in points[1:points.__len__() - 1]:
                points.remove((i, j))
            return points
        else:
            Left_Points = points[0:points.index(max_dist_point) + 1]
            Right_points = points[points.index(max_dist_point):]
            simplifiedLeft = DouglasPeucker(Left_Points)
            simplifiedRight = DouglasPeucker(Right_points)
            pass
            return simplifiedLeft + simplifiedRight[1:]

    X = [float(x) for x in path['LONG']]
    Y = [float(y) for y in path['LAT']]
    points = zip(X, Y)
    simplifiedPoints = DouglasPeucker(points)
    pathFilter = [((i, j) in simplifiedPoints) for (i, j) in zip(X, Y)]
    return path[pathFilter]


# 用DouglasPecker法对给定的台风集合的路径进行约减
def simplifyTyphoons_DougsPeucker(typhoons):
    for i in np.arange(typhoons['Path'].__len__()):
        typhoons.ix[typhoons.index[i]]['Path'] = simplifyPath_DougsPeucker(typhoons.ix[typhoons.index[i]]['Path'])
    return typhoons


# 统计每个经纬度网格内台风数目
def countTyphoonsNumberInEachGrid(typhoons):
    numberGrid = DataFrame(np.zeros((60, 210)), columns=list(str(i) for i in np.arange(60, 270, 1)),
                           index=list(str(j) for j in np.arange(0, 60, 1)))
    for path in typhoons['Path']:
        long = str(int(float(path.ix[0]['LONG']) / 10))
        lat = str(int(float(path.ix[0]['LAT']) / 10))
        numberGrid[long][lat] = numberGrid[long][lat] + 1
    return numberGrid


# 依据每个经纬度网格内的台风数目进行着色，台风数目越多颜色越深
def fillGridByTyphoonsNumberInEachGrid(typhoons, map=None):
    typhoonsNumberGrid = countTyphoonsNumberInEachGrid(typhoons)
    a = max([max(typhoonsNumberGrid[m]) for m in typhoonsNumberGrid.columns])
    for lon in typhoonsNumberGrid.columns:
        for lat in typhoonsNumberGrid.index:
            if typhoonsNumberGrid[str(lon)][str(lat)] > 0:
                draw_rectangel2(float(lat), float(lon), float(lat) + 1, float(lon) + 1, '#FF0000',
                               (float(typhoonsNumberGrid[str(lon)][str(lat)])) / float(
                                   max([max(typhoonsNumberGrid[m]) for m in typhoonsNumberGrid.columns])), map)
    return


# #台风检索和统计#########################################################################################################
# a = typhoonDF[[12 in set((time.strptime(str(date), '%Y%m%d%H%M').tm_mon) for date in path['Date'][0:1]) for path in
#                typhoonDF['Path']]]  # 历年所有12月份生成的台风
# b = typhoonDF[[12 in set((time.strptime(date, '%Y%m%d%H%M').tm_mon) for date in path['Date']) for path in
#                typhoonDF['Path']]]  # 历年所有12月份存在的台风
# c = typhoonDF[
#     [len({1, 12}.intersection(set((time.strptime(date, '%Y%m%d%H%M').tm_mon) for date in path['Date'][0:1]))) > 0 for path in
#      typhoonDF['Path']]]  # 历年所有{1,12}指定月份生成的台风
# d = typhoonDF[
#     [(len({8}.intersection(set((time.strptime(date, '%Y%m%d%H%M').tm_mon) for date in path['Date'][0:1]))) > 0) &
#      (len({1950}.intersection(set((time.strptime(date, '%Y%m%d%H%M').tm_year) for date in path['Date'][0:1]))) > 0) for path
#      in typhoonDF['Path']]]  # {1950}指定年份{8}指定月份生成的台风
# e = [typhoonDF[[i in set((time.strptime(date, '%Y%m%d%H%M').tm_mon) for date in path['Date'][0:1]) for path in
#                 typhoonDF['Path']]].__len__() for i in np.arange(1, 13)]  # 历年每个月份生成所有台风数目统计
# f = [typhoonDF[
#          [(i in (set((time.strptime(date, '%Y%m%d%H%M').tm_mon) for date in path['Date'][0:1]))) &
#           (len({1950}.intersection(set((time.strptime(date, '%Y%m%d%H%M').tm_year) for date in path['Date'][0:1]))) > 0) for
#           path in typhoonDF['Path']]].__len__() for i in np.arange(1, 13)]  # {1950}指定年份每个月份生成台风数目统计
#
# g=[typhoonDF[
#     [(len({10}.intersection(set((time.strptime(date, '%Y%m%d%H%M').tm_mon) for date in path['Date'][0:1]))) > 0) &
#      (i in (set((time.strptime(date, '%Y%m%d%H%M').tm_year) for date in path['Date'][0:1]))) for path
#      in typhoonDF['Path']]].__len__() for i in np.arange(1949, 2016)] # 1949-2015年每年8月份生成的台风数目统计
#
#
# h=[typhoonDF[
#     [(i in (set((time.strptime(date, '%Y%m%d%H%M').tm_year) for date in path['Date'][0:1]))) for path
#      in typhoonDF['Path']]].__len__() for i in np.arange(1949, 2016)] # 1949-2015年每年生成的台风数目统计





########################################################################################################################
# draw_typhoon_startpoints_by_time(years={2013}, months={9})
# draw_typhoon_startpoints_by_time(years=set(np.arange(2013, 2014)), months=set(np.arange(1, 13)))
#
# fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 10))
# fig.subplots_adjust(hspace=0.2, wspace=0.05)
# for end_month, ax in zip(np.arange(2, 14), axes.flat):
#     draw_typhoon_paths_by_time(years=set(np.arange(1950, 1951)), months=set(np.arange(end_month - 1, end_month)), ax=ax)
#     ax.set_title('%d ' % (end_month - 1))
#
# draw_typhoon_paths_by_time(years={2014},months={1,2,3,4,5,6,7,8,9,10,11,12})

pointA_Lat = 19.1
pointA_Lng = 134.5
pointB_Lat = 20.3
pointB_Lng = 135.0
pointC_Lat = 31.0
pointC_Lng = 142.0
R = 500
months = {7}
years = {2014}
tmp = typhoonDF[
    [(len(months.intersection(
        set((datetime.strptime(date, '%Y%m%d%H%M').month) for date in path['Date'][0:1]))) > 0) &
     (len(years.intersection(set((datetime.strptime(date, '%Y%m%d%H%M').year) for date in path['Date'][0:1]))) > 0) for
     path in typhoonDF['Path']]]  # 指定年份指定月份生成的台风
aaa = np.array([ifPassBufferCycle(pointA_Lat, pointA_Lng, R, path) for path in tmp['Path']])
bbb = np.array([ifPassBufferCycle(pointB_Lat, pointB_Lng, R, path) for path in tmp['Path']])
ccc = np.array([ifPassBufferCycle(pointC_Lat, pointC_Lng, R, path) for path in tmp['Path']])
ddd = np.array([ifTyphoonInPeriod(typhoon, datetime(2014, 7, 15), 15) for typhoon in tmp['Path']])
eee = np.array([ifStartFromCycle(8, 129, R, path) for path in typhoonDF['Path']])
fff = np.array([ifTyphoonInPeriod2(typhoon, 7, 1, 7, 31) for typhoon in typhoonDF['Path']])
ggg = np.array([ifPassRectangle(3, 107, 26, 120, typhoon) for typhoon in tmp['Path']])
hhh = np.array([ifStartFromRectangle(3, 107, 26, 120, typhoon) for typhoon in tmp['Path']])

j = tmp[aaa & bbb & ccc & ddd]  # 获得经过以A，B，C三个点为中心,半径为R公里的缓冲区，且时间在1955.7.15日前后15天的台风
k = tmp[ggg]
# simplifyTyphoons_DougsPeucker(k.ix[k.index[0]])
# simplifyPath_DougsPeucker(k.ix[k.index[0]]['Path'])

##############某年某月经过南海区域达到某一级别的台风路径########################
months = set(np.arange(1,13))
years = set(np.arange(1966, 1977))
I = 6
tmp = typhoonDF[
    [(len(months.intersection(
        set((datetime.strptime(date, '%Y%m%d%H%M').month) for date in path['Date'][0:1]))) > 0) &
     (len(years.intersection(set((datetime.strptime(date, '%Y%m%d%H%M').year) for date in path['Date'][0:1]))) > 0) for
     path in typhoonDF['Path']]]  # 指定年份指定月份生成的台风
filter1 = np.array([ifPassRectangle(3, 107, 26, 120, typhoon) for typhoon in tmp['Path']])
filter2 = np.array([ifTyphoonReachIntensity(typhoon, I) for typhoon in tmp['Path']])
filter3=np.array([ifReachIntensityInRectangel(3, 107, 26, 120, I,typhoon) for typhoon in tmp['Path']])
k = tmp[filter3]
tmpmap = draw_Map()
draw_typhoon_paths(k, map=tmpmap)
draw_rectangel(3, 107, 26, 120, '#FF0000', 1, tmpmap)
Intensities = Series(['低于热带低压', '热带低压', '热带风暴', '强热带风暴', '台风', '强台风', '超强台风', '变性'], index=[0, 1, 2, 3, 4, 5, 6, 9])
plt.title(
    ((str(min(years)) + '-' + str(max(years))) if years.__len__() > 1 else str(min(years))) + u'年' + (
        (str(min(months)) + '-' + str(max(months))) if months.__len__() > 1 else str(
            min(months))) + u'月' + u'经过南海区域' + str(
        Intensities[I]).decode('utf-8') + u'级别以上台风数量为：' + str(k.__len__()), fontproperties=font_set)

url='http://192.168.1.30:8061/grid/model/GridSingle_edzw/edzw,edzw_temp,850,2018-02-22%2000:00:00,024/HTML/png/0,360,90,0,360,90/color/cache'
response=requests.get(url)
image=pimg.open(BytesIO(response.content))
plt.imshow(image)
tmpmap = draw_Map()
plt.show()


map = Basemap(llcrnrlon=60, llcrnrlat=0, urcrnrlon=270, urcrnrlat=60, projection='cyl', lat_0=0, lon_0=120,
              resolution='l')
draw_circle(pointA_Lat, pointA_Lng, R, map=map)
draw_circle(pointB_Lat, pointB_Lng, R, map=map)
draw_circle(pointC_Lat, pointB_Lng, R, map=map)
draw_circle(8, 129, R, map=map)
draw_rectangel(3, 107, 26, 120, '#FF0000', 1, map)
plt.show()


#
# for year in np.arange(1949,2015):
#     for mon in np.arange(1,13):
#         plt.clf()
#         time.sleep(1)
#         tmpmap=draw_Map()
#         d = typhoonDF[[(len({mon}.intersection(set((datetime.strptime(date, '%Y%m%d%H%M').month) for date in path['Date'][0:1]))) > 0) &
#                  (len({year}.intersection(set((datetime.strptime(date, '%Y%m%d%H%M').year) for date in path['Date'][0:1]))) > 0) for path
#                  in typhoonDF['Path']]]  # {1950}指定年份{8}指定月份生成的台风
#          fillGridByTyphoonsNumberInEachGrid(d,tmpmap)
#         time.sleep(1)
#         plt.savefig('D:\\'+str(year)+str(mon)+'.png',dpi=300)





# typhoonsNumberGrid = countTyphoonsNumberInEachGrid(typhoonDF)
# max([max(m) for m in typhoonsNumberGrid])
# tmpmap = draw_Map()
# for lon in typhoonsNumberGrid.columns:
#     for lat in typhoonsNumberGrid.index:
#         if typhoonsNumberGrid[str(lon)][str(lat)] > 0:
#             draw_rectangel2(float(lat), float(lon), float(lat) + 1, float(lon) + 1, '#FF0000',
#                            (float(typhoonsNumberGrid[str(lon)][str(lat)])) / float(
#                                max([max(m) for m in typhoonsNumberGrid])), tmpmap)



# draw_typhoon_startpoints_by_time(years=set(np.arange(2010, 2015)), months=set(np.arange(1, 13)),map=tmpmap)
# draw_text(float(lat),float(lon),str(typhoonsNumberGrid[str(lon)][str(lat)]),map=map)


plt.show()



#######################################################################################################################
# 记录结束时间，计算运行时间
endTime = datetime.now()
executeTime = endTime - startTime


