# /usr/bin/python3
# -*- conding:utf-8 -*-
# -*-author:zhouboxin -*-
import time
import pygame
def mu(dict1):
    dict1 = {}
    pygame.mixer.init()
    path = r"D:/我的资料库/Music/chuanqi.mp3"
    pygame.mixer.music.load(path)
    m = n.splitlines()  # 行切片
    # print(m)
    for e in m:
        e = e.split("]")  # 以"]"切片
        # print(e)
        for index in range(len(e) - 1):
            # print(index)
            time1 = e[index][1:]  # 获取时间轴
            # print(time1)
            time1 = time1.split(":")  # 以:切片
            # print(time1)
            #print(time1[0])
            #time1 = ''.join(time1)  # 去掉''
            time1 = float(time1[0])*60+float(time1[1])##转成浮点数
            dict1[time1] = e[-1]  # 转成字典
    return dict1
def mo(dict1):
    keylist = []
    for key in dict1:
        keylist.append(key)
        keylist.sort()
    #print(keylist)
    pygame.mixer.music.play()
    for n in range(len(keylist)):
        if keylist[n]==3.5:
            time.sleep(3.5)
        else:
            time.sleep(keylist[n+1]-keylist[n])
        print(dict1[keylist[n]])
n = '''
[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]    
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
'''
er=mu(n)
mo(er)


# 初始化音频模块
