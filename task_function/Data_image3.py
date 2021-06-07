import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 学历统计图
def Data_image3():
    df = pd.read_csv(r'E:/pycharm/Recruitment_information_recommendation_platform/task_function/user_csv/已清洗数据.csv',engine='python',encoding="UTF-8")['education']
    data = df.value_counts()

    labels = ['大专', '本科', '硕士', '博士']
    num2 = data['本科']

    try:
        num1 = data['大专']
    except BaseException:
        num1 = 0
        print('职位中没有“大专"学历')

    try:
        num3 = data['硕士']
    except BaseException:
        num3 = 0
        print('职位中没有“硕士"学历')


    try:
        num4 = data['博士']
    except BaseException:
        num4 = 0
        print('职位中没有“博士"学历')

    #nums = [data[i] for i in labels]
    nums = [num1,num2,num3,num4]
    print(labels)
    print(nums)

    colors = ['cyan', 'red', 'yellow', 'blue']
    # 设置中文显示
    mpl.rcParams['font.family'] = 'SimHei'
    # 设置显示风格
    plt.style.use('ggplot')
    # 设置大小  像素
    plt.figure(figsize=(8, 6), dpi=100)
    # 绘制水平柱状图
    plt.barh(labels, nums, height=0.36, color=colors)
    plt.title('招聘岗位对学历的要求', fontsize=16)
    plt.xlabel('岗位数量', fontsize=12)
    #plt.show()


def main():
    Data_image3()


if __name__ == "__main__":
    main()
