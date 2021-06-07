import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# 职位经验统计图
def Data_image4():
    df = pd.read_csv(r'E:/pycharm/Recruitment_information_recommendation_platform/task_function/user_csv/已清洗数据.csv',engine='python',encoding="UTF-8")['experience']
    # 查看统计情况
    data = df.value_counts()
    print(data)

    labels = ['无需经验', '1年经验', '2年经验', '3-4年经验', '5-7年经验', '8-9年经验', '10年以上经验']
    # nums = [data[i] for i in labels]
    try:
        num1 = data[labels[0]]
    except BaseException:
        num1 = 0
        print('职位中没有“无需经验"职位')

    num2 = data[labels[1]]
    num3 = data[labels[2]]
    num4 = data[labels[3]]

    try:
        num5 = data[labels[4]]
    except BaseException:
        num5 = 0
        print('职位中没有“5-7年经验"职位')


    try:
        num6 = data[labels[5]]
    except BaseException:
        num6 = 0
        print('职位中没有“8-9年经验"职位')

    try:
        num7 = data[labels[6]]
    except BaseException:
        num7 = 0
        print('职位中没有“10年以上经验"职位')

    nums = [num1,num2,num3,num4,num5,num6,num7]
    # 要求是在校生\应届生、本科 处理为无需经验  硕士处理为1年经验  博士处理为3-4年经验
    nums[0] = nums[0] + 661 + 182
    nums[1] = nums[1] + 59
    nums[3] = nums[3] + 11
    print(labels)
    print(nums)

    colors = ['#0000CD', '#FF0000', '#FFD700', '#7FFF00', '#FF1493', '#9400D3', '#87CEFA']
    # 设置中文显示
    mpl.rcParams['font.family'] = 'SimHei'
    # 设置显示风格
    plt.style.use('ggplot')
    # 设置大小  像素
    plt.figure(figsize=(9, 6), dpi=100)
    # 绘制水平柱状图
    plt.barh(labels, nums, height=0.5, color=colors)
    plt.title('招聘岗位对工作经验的要求', fontsize=16)
    plt.xlabel('岗位数量', fontsize=12)
    #plt.show()


def main():
    Data_image4()


if __name__ == "__main__":
    main()
