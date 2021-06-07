import pandas as pd


# 数据预处理 和 去重
def clear_data():

    df = pd.read_csv('user_csv/job_info1.csv')
    # 异步爬虫爬取数据时  datas.to_csv('job_info.csv', mode='a+', index=False, header=True)  删除多的列名
    df1 = df[df['salary'] != 'salary']
    # 查看前1行
    print(df1.head())


    # city那一列数据  处理为城市
    # 按 - 分割   expand=True  0那一列重新赋值给df['city']
    # pandas 解决 A value is trying to be set on a copy of a slice from a DataFrame的问题
    # 对那一列重新赋值
    df2 = df1.copy()
    df2.loc[:,'city'] = df1['city'].str.split('-', expand=True)
    df2.head()


    # 经验要求  学历要求   有的话是在attribute_text列里
    df1['attribute_text'].str.split('|', expand=True)

    df2['experience'] = df1['attribute_text'].str.split('|', expand=True)[1]
    df2['education'] = df1['attribute_text'].str.split('|', expand=True)[2]
    df2['need_people'] = df1['attribute_text'].str.split('|', expand=True)[3]
    str='name'
    df2.to_csv('user_csv/已清洗数据.csv', index=False)

    #显示
    #df3 = pd.read_csv('已清洗数据.csv')
    #df3.info()
def main():
    clear_data()

if __name__ == "__main__":
    main()




