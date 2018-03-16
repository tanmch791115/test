__author__ = 'tanmch791115'
# coding=utf-8
# _*_ coding: utf-8 _*_
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np



# 每次产生一个新的坐标点

def data_gen():
    t = 0
    cnt = 0
    while t<100:
        cnt+=1
        t += 0.1
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)

data_gen.t = 0

# for data in data_gen():
#     print data


# 绘图
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 50)
ax.grid()
xdata, ydata = [], []

# 因为run的参数是调用函数data_gen,所以第一个参数可以不是framenum:设置line的数据,返回line
def run(data):
    # update the data
    t,y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmax-5, (xmax+45))
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    plt.title(str(data))
    ax.figure.canvas.draw()
    return line,

# 每隔10秒调用函数run,run的参数为函数data_gen,
# 表示图形只更新需要绘制的元素
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10, repeat=False)
plt.show()






"""
通过定时器Timer触发事件，定时更新绘图，可以形成动态更新图片。
"""
import wx
from matplotlib.figure import Figure
import matplotlib.font_manager as font_manager
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# wxWidgets object ID for the timer
TIMER_ID = wx.NewId()
# number of data points
POINTS = 300

class PlotFigure(wx.Frame):
    """Matplotlib wxFrame with animation effect"""
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="CPU Usage Monitor", size=(600, 400))
        # Matplotlib Figure
        self.fig = Figure((6, 4), 100)
        # bind the Figure to the backend specific canvas
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.fig)
        # add a subplot
        self.ax = self.fig.add_subplot(111)
        # limit the X and Y axes dimensions
        self.ax.set_ylim([0, 100])
        self.ax.set_xlim([0, POINTS])

        self.ax.set_autoscale_on(False)
        self.ax.set_xticks([])
        # we want a tick every 10 point on Y (101 is to have 10
        self.ax.set_yticks(range(0, 101, 10))
        # disable autoscale, since we don't want the Axes to ad
        # draw a grid (it will be only for Y)
        self.ax.grid(True)
        # generates first "empty" plots
        self.user = [None] * POINTS
        self.l_user,=self.ax.plot(range(POINTS),self.user,label='User %')

        # add the legend
        self.ax.legend(loc='upper center',
                           ncol=4,
                           prop=font_manager.FontProperties(size=10))
        # force a draw on the canvas()
        # trick to show the grid and the legend
        self.canvas.draw()
        # save the clean background - everything but the line
        # is drawn and saved in the pixel buffer background
        self.bg = self.canvas.copy_from_bbox(self.ax.bbox)
        # bind events coming from timer with id = TIMER_ID
        # to the onTimer callback function
        wx.EVT_TIMER(self, TIMER_ID, self.onTimer)

    def onTimer(self, evt):
        """callback function for timer events"""
        # restore the clean background, saved at the beginning
        self.canvas.restore_region(self.bg)
                # update the data
        temp =np.random.randint(10,80)
        self.user = self.user[1:] + [temp]
        # update the plot
        self.l_user.set_ydata(self.user)
        # just draw the "animated" objects
        self.ax.draw_artist(self.l_user)# It is used to efficiently update Axes data (axis ticks, labels, etc are not updated)
        self.canvas.blit(self.ax.bbox)
    def __del__( self ):
        t.Stop()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = PlotFigure()
    t = wx.Timer(frame, TIMER_ID)
    t.Start(50)
    frame.Show()
    app.MainLoop()