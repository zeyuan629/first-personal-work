import requests
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',
}
cursor='0'
source='1613549142009'
n=12688//10
for i in range(0,n):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+source
    html = requests.get(url, headers=headers).content.decode()
    commentlist = re.compile(r'"content":"(.*?)"', re.S)
    list= re.findall(commentlist, html)
    with open('comment.txt', 'a+', encoding='utf-8') as f:
        for i in list:
            i = i.replace("\n", "")
            f.write(i)
            f.write("\n")
    cursor=re.findall('"last":"(.*?)"',html,re.S)[0].replace("\n","").replace(" ","")
    source=str(int(source)+1)
print("爬取完成")