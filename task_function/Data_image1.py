#coding=utf-8
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys


#from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
#mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

# 城市岗位数排名
def Data_image1():
    #sys.path.append('E:/pycharm/Recruitment_information_recommendation_platform')
    df = pd.read_csv(r'E:/pycharm/Recruitment_information_recommendation_platform/task_function/user_csv/已清洗数据.csv',engine='python',encoding="UTF-8")

    # 有些是异地招聘   过滤掉
    data = df[df['city'] != '异地招聘']['city'].value_counts()
    city = list(data.index)[:10]    # 城市
    nums = list(data.values)[:10]   # 岗位数
    #print(data)
    print(city)
    print(nums)

    colors = ['#FF0000', '#0000CD', '#00BFFF', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970', '#9932CC']
    random.shuffle(colors)

    # 设置大小   像素
    plt.figure(figsize=(9, 6), dpi=100)
    # 设置中文显示
    mpl.rcParams['font.family'] = 'SimHei'
    # 绘制柱形图  设置柱条的宽度和颜色
    # color参数  每根柱条配置不同颜色
    plt.bar(city, nums, width=0.5, color=colors)

    # 添加描述信息
    plt.title('招聘岗位数最多的城市Top10', fontsize=16)
    plt.xlabel('城市', fontsize=12)
    plt.ylabel('岗位数', fontsize=12)
    # 展示图片
    #plt.show()



def main():
    Data_image1()

if __name__ == "__main__":
    main()
