import pandas as pd
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 福利云图
def Data_image6():
    df = pd.read_csv(r'E:/pycharm/Recruitment_information_recommendation_platform/task_function/user_csv/已清洗数据.csv',engine='python',encoding="UTF-8")['job_welfare']
    # 去除NaN  就地修改
    df.dropna(axis=0, inplace=True)
    data = list(df.values)

    word_list = []
    for i in data:
        x = i.split(' ')
        for j in x:
            word_list.append(j)


    word_counts = collections.Counter(word_list)
    print(word_counts)
    print(len(word_counts))
    # 绘制词云
    my_cloud = WordCloud(
        background_color='white',  # 设置背景颜色  默认是black
        width=800, height=550,
        font_path='simhei.ttf',    # 设置字体  显示中文
        max_font_size=112,         # 设置字体最大值
        min_font_size=12,          # 设置子图最小值
        random_state=60            # 设置随机生成状态，即多少种配色方案
    ).generate_from_frequencies(word_counts)

    # 显示生成的词云图片
    plt.imshow(my_cloud, interpolation='bilinear')
    # 显示设置词云图中无坐标轴
    plt.axis('off')
    #plt.show()


def main():
    Data_image6()


if __name__ == "__main__":
    main()
