import asyncio
import aiohttp
import logging
import datetime
import re
import pandas as pd

a = logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
start = datetime.datetime.now()

#print("时间",a) # 时间 None
#print("开始时间",start) # OK

#解析url
class Spider(object):
    def __init__(self):
        self.semaphore = asyncio.Semaphore(6)
        self.headers = {
            'Connection': 'Keep-Alive',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'search.51job.com',
            'Referer': 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'

        }
        self.static = "未爬取"

    # 重新初始header
    def re_init(self, job_key, page):
        page = str(page)
        print(self.headers['Referer'])
        re_header = self.headers['Referer'].replace('{job_key}', job_key).replace('{page}', page)
        print(re_header)
        self.headers['Referer'] = re_header
        print(self.headers)


    async def scrape(self, url):
        async with self.semaphore:
            session = aiohttp.ClientSession(headers=self.headers)
            response = await session.get(url)
            await asyncio.sleep(1)
            result = await response.text()
            #print("爬取页面转化为文本格式") #OK
            await session.close()
            return result


    # 爬取基本职位信息
    async def parse(self, text):

        # 正则匹配提取数据
        try:
            job_name = re.findall('"job_name":"(.*?)",', text)          # 职位
            job_name = [i.replace('\\', '') for i in job_name]
            company_name = re.findall('"company_name":"(.*?)",', text)  # 公司名称
            salary = re.findall('"providesalary_text":"(.*?)",', text)
            salary = [i.replace('\\', '') for i in salary]              # 薪酬     去掉 \ 符号
            city = re.findall('"workarea_text":"(.*?)",', text)         # 城市
            #print("job_name",job_name)

            job_welfare = re.findall('"jobwelf":"(.*?)",', text)        # 职位福利

            attribute_text1 = re.findall('"attribute_text":(.*?),"companysize_text"', text)
            attribute_text = ['|'.join(eval(i)) for i in attribute_text1]
            #print('attribute_text文本', attribute_text)

            #experience = []  # 经验
            #education = []  # 学历
            #need_people = []  # 招聘人数

            # for i in attribute_text:
            #
            #     # 字符串处理  比较麻烦
            #     # chuli1 = i.replace('[', '')
            #     # chuli2 = chuli1.replace(']', '')
            #     # chuli3 = chuli2.replace('"','')
            #     # chuli4 = chuli3.replace(',', ' ')
            #     # content = chuli4.strip()
            #     # print(type(content))
            #
            #     # 转换列表处理：
            #     content = eval(i)
            #     if content:
            #         region = content[0]
            #     else:
            #         region = ''
            #     exp = content[1]
            #     #print('exp',exp)
            #     #experience = experience.extend(content[1])        # 经验
            #     #print(type(experience))
            #     #education = education.extend(content[2])         # 学历
            #     #need_people = need_people.extend(content[3])       # 招聘人数

            #experience = re.findall('"providesalary_text":"(.*?)",', text)         # 经验
            #education = re.findall('"providesalary_text":"(.*?)",', text)              # 学历
            #need_people = re.findall('"providesalary_text":"(.*?)",', text)            # 招聘人数

            # df1 = [i.str.split('|', expand=True)for i in attribute_text]
            # print('df1',type(df1),df1)
            # experience = df1[1]
            # education = df1[2]
            # need_people = df1[3]

            experience = [eval(i)[1] for i in attribute_text1]      # 经验
            #print('experience', type(experience), experience)
            education = [eval(i)[2] for i in attribute_text1]       # 学历
            need_people = [eval(i)[3] for i in attribute_text1]     # 招聘人数

            job_url = re.findall('"job_href":"(.*?)",', text)  # 职位URL
            job_url = [i.replace('\\', '') for i in job_url]  # 去掉 \ 符号
            cp_url = re.findall('"company_href":"(.*?)",', text)  # 公司URL
            cp_url = [i.replace('\\', '') for i in cp_url]  # 去掉 \ 符号

            #job_data = [company_name,job_name,city,salary,attribute_text,job_welfare,experience,
            #            education,need_people,job_url, cp_url]
            #print(job_data)
            job_db = pd.DataFrame({'job': job_name,
                                  'company': company_name,
                                  'city': city,
                                  'salary': salary,
                                  'welfare': job_welfare,
                                  'exp': experience,
                                  'edu': education,
                                  'job_num': need_people,
                                  'job_url': job_url,
                                  'company_url': cp_url
                                  })

            job_db.to_csv(r'task_function/user_csv/job_db.csv', mode='a+', index=False, header=True)

            datas = pd.DataFrame({'job_name': job_name,
                                  'company_name': company_name,
                                  'city': city,
                                  'salary': salary,
                                  'attribute_text': attribute_text,
                                  'job_welfare': job_welfare,
                                  #'experience': experience,
                                  #'education': education,
                                  #'need_people': need_people,
                                  'job_url': job_url,
                                  'cp_url': cp_url

                                  })
            #print(type(datas)) #<class 'pandas.core.frame.DataFrame'>
            print(datas.head(5)) # 显示前5行结果
            #print("保存数据到job_info1.csv")
            #print(datas)
            #name = r'user_csv/job_info1.csv'
            datas.to_csv(r'task_function/user_csv/job_db.csv', mode='a+', index=False, header=True)

            self.static = '完成'
            #logging.info({'company_name': company_name, 'job_name': job_name, 'city': city, 'salary': salary, 'attribute_text': attribute_text, 'job_welfare': job_welfare})
        except Exception as e:
            print(e)


    # 爬取HTML网页
    async def scrape_index(self,job_key, page):
        url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,{job_key},2,{page}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        #self.re_init(self, job_key, page)

        #print("index_url:",url) # OK
        text = await self.scrape(url)
        # print("准备爬取信息")# OK
        await self.parse(text)
        await asyncio.sleep(1)



    def main(self,job_key,page):

        # print(self.headers) #OK

        # 爬取page页的数据
        scrape_index_tasks = [asyncio.ensure_future(self.scrape_index(job_key,page)) for page in range(1, page+1)]
        loop = asyncio.get_event_loop()
        tasks = asyncio.gather(*scrape_index_tasks)
        loop.run_until_complete(tasks)


if __name__ == '__main__':
    spider = Spider()

# 测试

    spider.main('java',2)
    delta = (datetime.datetime.now() - start).total_seconds()
    print("用时：{:.3f}s".format(delta))
    #s = '{:.3f}s'.format(delta)
    #print(s) #ok
    # .format格式化
    # str.format()，它增强了字符串格式化的功能。
    # 基本语法是通过{}和: 来代替以前的 % 。
    # >>> "{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序
    # 'hello world'
    # >>> "{0} {1}".format("hello", "world")  # 设置指定位置
    # 'hello world'
    # >>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
    # 'world hello world'


