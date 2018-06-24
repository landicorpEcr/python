#!/usr/bin/python
# coding:utf-8

import re
import urllib.request
# bs4模块为第三方模块需要单独安装 pip install bs4
import bs4


# 从代理网站获取代理IP
def get_ip(n):
    # 定义http请求地址
    # url = "http://www.xicidaili.com/nn/" + str(n)
    url = "http://www.xicidaili.com/wn/" + str(n)
    # 定义http请求头
    headers = {"Accecpt": "text/html,application/xhtml+xml,application/xml",
               "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
               "Referer": "http://www.xicidaili.com",
               "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
               }
    # 用urllib库的request模块的Request创建一个链接
    request = urllib.request.Request(url=url, headers=headers)
    # 打开这个链接并读取数据
    data = urllib.request.urlopen(request).read()
    # 解析上面获取的被utf-8格式编码的数据,处理成html格式
    page_data = data.decode("utf-8")
    # 将HTML处理成bs4库能识别的状态
    soup = bs4.BeautifulSoup(page_data, 'html.parser')
    # 分析html代码后可发现ip地址都存在于td标签之间，故取出所有td标签
    data = soup.table.find_all("td")
    # 定义一个匹配ip的规则
    ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
    # 定义一个匹配port的规则
    port_compile = re.compile(r"<td>(\d+)</td>")
    # 利用定义好的ip_compile规则找出所有符合正则的ip
    ip = re.findall(ip_compile, str(data))
    # 利用定义好的port_compile规则找出所有符合正则的port
    port = re.findall(port_compile, str(data))
    # 返回找到的结果
    return [":".join(i) for i in zip(ip, port)]


# 打印代理IP，这是console打印，并不是写文件（不是论文代码要求）。
def printIP(ip):
    myip = ip
    for ips in myip:
        print(ips)
    print('end')


# 保存数据到txt文本
def text_save(content, filename, mode='w'):
    # 首先创建并打开一个空文件
    file = open(filename, mode)
    # 循环解析数据内容
    for i in range(len(content)):
        # 写入字符串型文件内容
        file.write(str(content[i]) + '\n')
    # 关闭文件
    file.close()


def getAll(num):
    # 定义一个空的list
    allText = []
    # 循环将各页得到的list数据累加起来
    for i in range(num):
        allText = allText + get_ip(i + 1)
    # 将数据用txt写出来
    text_save(allText, 'ip地址集合.txt')


# 执行获取多少页以内数据的函数
getAll(20)
