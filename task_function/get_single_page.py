import re
import copy
import requests
from lxml import etree


# 当个URL处理  str类型
class URLSpider():
    # 初始化基本URL信息
    def __init__(self):
        self.base_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%s,2,%s.html?'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'}

    # 留下常规合法的网址，参数list类型URL数据
    def screen_url(self, url):
        detail_url1 = copy.deepcopy(url)
        # print("正在处理：", url)
        if 'jobs.51job.com' not in url:
            # print("移出", type(url))
            detail_url1.remove(url)
        # print("进行Parse_data")
        # self.parse_data(detail_url2)
        # print('第%d页数据爬取完毕！' % num)
        # time.sleep(2) 延时函数
        # 去除转义字符
        detail_url2 = detail_url1.replace('\\', '')
        print('url数据检查完毕！', detail_url2)
        return detail_url2

    # 爬取招聘信息详情  参数list的URL数据
    def parse_data(self, url):
        """
        position:            职位
        wages:               工资
        region:              地区
        experience:          经验
        education:           学历
        need_people:         招聘人数
        publish_date:        发布时间
        english:             英语要求
        welfare_tags:        福利标签
        job_information:     职位信息
        work_address:        上班地址
        company_name:        公司名称
        company_nature:      公司性质
        company_scale:       公司规模
        company_industry:    公司行业
        company_information: 公司信息
        """
        # print("爬取中。。")
        # print(type(url))# url 为字符串str类型
        # 列表转字符串，使转义字符生效 X（没有\/转义字符）
        # 方法2   去除“\”
        url_str = url.replace('\\', '')
        # print(type(url_str))# 正确的网址 字符串str类型
        # print(url_str)
        response = requests.get(url=url_str, headers=self.headers)
        try:
            text = response.content.decode('gbk')
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
            return
        tree = etree.HTML(text)
        # print(tree)# <Element html at 0x19acbe20748>

        # 提取内容时使用 join 方法将列表转为字符串，而不是直接使用索引取值，
        # 这样做的好处是遇到某些没有的信息直接留空而不会报错

        position = ''.join(tree.xpath("//div[@class='cn']/h1/text()"))
        wages = ''.join(tree.xpath("//div[@class='cn']/strong/text()"))

        # 经验、学历、招聘人数、发布时间等信息都在一个标签里面，逐一使用列表解析式提取
        content1 = tree.xpath("//div[@class='cn']/p[2]/text()")
        contents = ''.join(content1).replace(r'&nbsp;', '')
        content = [i.strip() for i in content1]
        if content:
            region = content[0]
        else:
            region = ''
        experience = ''.join([i for i in content if '经验' in i])
        education = ''.join([i for i in content if i in '本科大专应届生在校生硕士'])
        need_people = ''.join([i for i in content if '招' in i])
        publish_date = ''.join([i for i in content if '发布' in i])
        english = ''.join([i for i in content if '英语' in i])

        welfare_tags = ','.join(tree.xpath("//div[@class='jtag']/div//text()")[1:-2])
        job_information = ''.join(tree.xpath("//div[@class='bmsg job_msg inbox']/p//text()"))
        work_address = ''.join(tree.xpath("//div[@class='bmsg inbox']/p//text()"))
        company_name = ''.join(tree.xpath("//div[@class='tCompany_sidebar']/div[1]/div[1]/a/p/text()"))
        company_nature = ''.join(tree.xpath("//div[@class='tCompany_sidebar']/div[1]/div[2]/p[1]//text()"))
        company_scale = ''.join(tree.xpath("//div[@class='tCompany_sidebar']/div[1]/div[2]/p[2]//text()"))
        company_industry = ''.join(tree.xpath("//div[@class='tCompany_sidebar']/div[1]/div[2]/p[3]/@title"))
        company_info = ''.join(tree.xpath("//div[@class='tmsg inbox']/text()"))
        company_information = company_info.replace(r'\xa0', '')
        # print(position,wages,experience,education,need_people,publish_date)# 抽样查看 OK

        job_data = [contents, english, job_information, publish_date, work_address,
                    company_nature, company_scale, company_industry, company_information]
        #print(job_data)

        # 保存数据

        return job_data


if __name__ == '__main__':
    spider = URLSpider()
