#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# 薪资分布饼状图
def Data_image2():
    df = pd.read_csv(r'E:/pycharm/Recruitment_information_recommendation_platform/task_function/user_csv/已清洗数据.csv',engine='python',encoding="UTF-8")['salary']
    part_interval = ["5K-10K", "10K-15K", "15K-20K", "20K-25K", "25K-30K", "30K-35K", "35-50K", "50K以上"]
    level1, level2, level3, level4, level5, level6, level7, level8 = 0, 0, 0, 0, 0, 0, 0, 0
    #salary = None
    print(df)

    for i in df.values:

        if str(i) == 'nan':
            pass
        elif i[-3:] == '万/月':
            i = i.replace('万/月', '-万/月')
            x = i.split('-')
            salary = (float(x[0]) + float(x[1])) * 10 / 2
        elif i[-3:] == '千/月':
            i = i.replace('千/月', '-千/月')
            x = i.split('-')
            salary = (float(x[0]) + float(x[1])) / 2
        elif i[-3:] == '万/年':
            i = i.replace('万/年', '-万/年')
            x = i.split('-')
            salary = (float(x[0]) + float(x[1])) / 2 * 10 / 12
        else:
            continue

        if 5 < salary <= 10:
            level1 += 1
        elif 10 < salary <= 15:
            level2 += 1
        elif 15 < salary <= 20:
            level3 += 1
        elif 20 < salary <= 25:
            level4 += 1
        elif 25 < salary <= 30:
            level5 += 1
        elif 30 < salary <= 35:
            level6 += 1
        elif 35 < salary <= 50:
            level7 += 1
        else:
            level8 += 1

    nums = [level1, level2, level3, level4, level5, level6, level7, level8]
    colors = ['#0000CD', '#FF0000', '#FFD700', '#7FFF00', '#FF1493', '#9400D3', '#FF8C00', '#87CEFA']

    # 设置中文显示
    mpl.rcParams['font.family'] = 'SimHei'
    # 设置大小  像素
    plt.figure(figsize=(9, 6), dpi=100)
    plt.axes(aspect='equal')   # 保证饼图是个正圆
    explodes = [0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
    plt.pie(nums, pctdistance=0.75, shadow=True,
            colors=colors, autopct='%.2f%%', explode=explodes,
            startangle=15, labeldistance=1.1,
            )

    # 设置图例   调节图例位置
    plt.legend(part_interval, bbox_to_anchor=(1.0, 1.0))
    plt.title('招聘岗位的薪酬分布', fontsize=15)
    #plt.show()


def main():
    Data_image2()


if __name__ == "__main__":
    main()
