import requests
from lxml import etree

url = "https://www.bqg70.com/book/511/1.html"
# 测试网址https://www.bqg70.com/book/511/1811.html下载结束后是否正常退出


# 获取网页内容
res = requests.get(url)
# neirong = res.content.decode()
# 解析网页内容
tree = etree.HTML(res.content.decode())

dd = tree.xpath('//div[@class="Readpage pagedown"]/a[@id="pb_next"]/@href')

# 写自动下载下一章函数
def xiazai(zj):
    url = "https://www.bqg70.com/{hi}".format(hi=zj)
    print(url)
    xres = requests.get(url)
    xtree = etree.HTML(xres.content.decode())
    # 获取章节内容下载
    cc = xtree.xpath('//div[@id="chaptercontent"]/text()')
    i1 = "请收藏本站：https://www.bqg70.com。笔趣阁手机版：https://m.bqg70.com "
    i2 = "==============微信rmshou收集整理===================="
    for i in cc:
        with open("遮天.txt", 'a', encoding="utf-8") as f:
            a = i.replace(i1, i2)
            f.write(a)
            f.write("\n\n")
    # 获取章节提示
    hh = xtree.xpath('//h1[@class="wap_none"]/text()')
    print(hh[0]+"--下载完成")
    # 获取下一章href
    ee = xtree.xpath('//div[@class="Readpage pagedown"]/a[@id="pb_next"]/@href')
    if ee[0] == "/book/511/":
        return
    else:
        xiazai(ee[0])
# 运行函数
xiazai(dd[0])
print("全书下载完毕，祝您阅读愉快~\n\n\n")

# "其实还可以更加优化，dd[0]部分可以不用，让函数部分直接输入网址在内部拼接完整"