import requests



class Mulu:
    def __init__(self, origin_url):
        self.origin_url = origin_url

    '''
    获取字典内容
    '''

    def get_txt_contents(self):
        with open('php.txt', "r", encoding="utf-8") as f:
            list_1 = f.read().splitlines()
            return list_1

    '''
    将字典内容与网址拼接
    '''

    def pingjie_website(self):
        list_2 = []
        for value in self.get_txt_contents():
            new_url = 'http://' + self.origin_url + value
            list_2.append(new_url)
        return list_2

    '''
    识别状态码，扫描目录及铭感文件
    '''

    def shibie(self):
        list = []
        for value in self.pingjie_website():
            if requests.get(value).status_code == 200:
                list.append(value + '   状态码：200')
                print(value + '   状态码：200')
            elif requests.get(value).status_code == 403:
                print(value + '   状态码：403')
                list.append(value + '   状态码：403')
            elif requests.get(value).status_code == 302:
                print(value + '   状态码：302')
                list.append(value + '   状态码：302')
        for value in list:
            with open('result.txt', "a", encoding="utf-8") as f:
                f.write(value + '\n')


