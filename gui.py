# Python默认的GUI开发模块是tkinter（在Python 3以前的版本中名为Tkinter）
# 事实上，开发GUI应用并不是Python最擅长的工作，如果真的需要使用Python开发GUI应用，
# wxPython、PyQt、PyGTK等模块都是不错的选择。
"""
基本上使用tkinter来开发GUI应用需要以下5个步骤：

1\ 导入tkinter模块中我们需要的东西。
2\ 创建一个顶层窗口对象并用它来承载整个GUI应用。
3\ 在顶层窗口对象上添加GUI组件。
4\ 通过代码将这些GUI组件的功能组织起来。
5\ 进入主事件循环(main loop)。
"""
"""
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', '小犇犇蠢蠢蠢！') if flag else ('blue', '小哼哼好好看')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    # tk.geometry（）
    # 一般接受的参数为"400x400+20+20"类的参数，注意这里x为小写字母x，不是乘号，
    # 使用大写X或者*都会报错：bad geometry specifier "400*400+200+200"。
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='小犇犇蠢蠢蠢!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
"""
"""
Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，
其中包含对图像、声音、视频、事件、碰撞等的支持。Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，
其中包含对图像、声音、视频、事件、碰撞等的支持。
游戏的名字叫“大球吃小球”
"""
"""
import pygame


# pygame中draw模块的函数在窗口上绘图，可以绘制的图形包括：线条、矩形、多边形、圆、椭圆、圆弧等。需要说明的是，
# 屏幕坐标系是将屏幕左上角设置为坐标原点(0, 0)，向右是x轴的正向，向下是y轴的正向，在表示位置或者设置尺寸的时候，
# 我们默认的单位都是像素。所谓像素就是屏幕上的一个点，你可以用浏览图片的软件试着将一张图片放大若干倍，就可以看到这些点。
# pygame中表示颜色用的是色光三原色表示法，即通过一个元组或列表来指定颜色的RGB值，每个值都在0~255之间，
# 因为是每种原色都用一个8位（bit）的值来表示，三种颜色相当于一共由24位构成，这也就是常说的“24位颜色表示法”
def main():
    # 初始化导入的pygame模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口chicun
    screen = pygame.display.set_mode((1200, 900))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口的背景色（颜色是由红绿蓝三原色构成的元组）
    screen.fill((242, 242, 242))
    # 如果需要直接加载图像到窗口上，可以使用pygame中image模块的函数来加载图像，
    # 再通过之前获得的窗口对象的blit方法渲染图像
    # ball_image = pygame.image.load('C:\lzh\pycharm_code\day10\little_yellow_person.png')
    # 在窗口上渲染图象
    # screen.blit(ball_image,(50,50))
    # 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
    x, y = 50, 50
    # pygame.draw.circle(screen, (255, 0, 0), (50, 50), 30, 0)
    # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
    # pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50ms改变小球的位置再刷新
        pygame.time.delay(50)
        x, y = x + 5, y + 5
        if x == 900:
            x, y = 50, 50


if __name__ == '__main__':
    main()
"""

"""
碰撞检测
通常一个游戏中会有很多对象出现，而这些对象之间的“碰撞”在所难免,
pygame的sprite（动画精灵）模块就提供了对碰撞检测的支持
"""

from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    # 颜色
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        # 获得随机颜色
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    # 球
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        # 初始化方法
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        # 移动
        self.x += self.x
        self.y += self.y
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        # 吃其他球
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        # 在窗口上绘制球
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main():
    # 定义用来装球的容器
    balls = []
    # 初始化导入pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口的大小
    screen = pygame.display.set_mode((800, 1000))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息列队中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球（大小，速度和颜色随机）
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表的容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没有被吃掉就会绘制 被吃掉就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                ball.remove(ball)
        pygame.display.flip()
        # 每隔50ms就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
