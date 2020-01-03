# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *


auto_setup(__file__)

num=0
while True:
    stop_app("air.jp.co.cygames.worldflipper")#结束游戏
    start_app("air.jp.co.cygames.worldflipper")#启动游戏
    wait(Template(r"tpl1576511540085.png", record_pos=(0.006, -0.564), resolution=(1080, 2400)))#等待游戏启动
    sleep(1.0)#等待加载
    touch(Template(r"tpl1576511540085.png", record_pos=(0.006, -0.564), resolution=(1080, 2400)))#进入游戏
    sleep(3.0)#等待加载
    while True:
        if exists(Template(r"tpl1576594274736.png", record_pos=(-0.004, 0.252), resolution=(1080, 2400))):#判断是否有弹窗
            touch(Template(r"tpl1576594274736.png", record_pos=(-0.004, 0.252), resolution=(1080, 2400)))#有弹窗点击弹窗
            sleep(2.0)#等待加载
            continue
        if exists(Template(r"tpl1576511540085.png", record_pos=(0.006, -0.564), resolution=(1080, 2400))):#判断是否返回主页
            touch(Template(r"tpl1576511540085.png", record_pos=(0.006, -0.564), resolution=(1080, 2400)))#再次进入游戏
            sleep(2.0)#等待加载
            continue
        if exists(Template(r"tpl1576640511025.png", record_pos=(-0.003, 0.678), resolution=(1080, 2400))):#确认进入主界面
            break            
    try:
        wait(Template(r"tpl1576503717553.png", threshold=0.85, record_pos=(-0.433, -0.941), resolution=(1080.0, 2400.0)),timeout=(300),interval=1)#守铃,电脑好的小伙汁可以提高频率嗷
    except:
        continue#5分钟未找到铃铛重启
    touch(Template(r"tpl1576503717553.png", threshold=0.9, record_pos=(-0.433, -0.941), resolution=(1080.0, 2400.0)))#发现铃铛！
    touch(Template(r"tpl1576503722130.png", threshold=0.9, record_pos=(0.206, 0.591), resolution=(1080.0, 2400.0)))#点击参加
    sleep(3.0)#等待加载
    if not exists(Template(r"tpl1576503728525.png", record_pos=(-0.062, 0.26), resolution=(1080.0, 2400.0))):#判断是否进入房间
        continue
    touch(Template(r"tpl1576503728525.png", record_pos=(-0.062, 0.26), resolution=(1080.0, 2400.0)))#点击准备
    sleep(10.0)#等待战斗
    while True:
        if exists(Template(r"tpl1576639744838.png", record_pos=(-0.001, 0.255), resolution=(1080, 2400))):#判断是否掉线
            touch(Template(r"tpl1576639744838.png", record_pos=(-0.001, 0.255), resolution=(1080, 2400)))#点击OK返回主页
            print('掉线 '+time.strftime("%H:%M:%S", time.localtime()))
            break
        if exists(Template(r"tpl1577463522206.png", record_pos=(-0.4, -0.417), resolution=(1440, 3120))):#判断是否失败
            print('战斗失败 '+time.strftime("%H:%M:%S", time.localtime()))
            break
        if exists(Template(r"tpl1576503806345.png", record_pos=(-0.01, 0.799), resolution=(1080.0, 2400.0))):#判断是否结算
            num+=1
            print('成功摸铃铛 %d 次'%num+'  '+time.strftime("%H:%M:%S", time.localtime()))
            break
    sleep(4.0)#喘口气


