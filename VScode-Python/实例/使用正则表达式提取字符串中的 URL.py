#给定一个字符串，里面包含 URL 地址，需要我们使用正则表达式来获取字符串的 URL。
import re 
  
def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url 
      
 
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))
