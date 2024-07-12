import Mulu
if __name__ == '__main__':
    url = input("请输入要扫描的网址(不含协议)：")
    mulu=Mulu.Mulu(url)
    mulu.shibie()
