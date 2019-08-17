import requests
import interface.config.readConfig as readConfig
from interface.common.log import Mylog as Log
localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, prot, timeout
        self.module = ''
        self.method = ''
        self.paras = ''
        self.baseurl = ''
        self.header = ''
        host = localReadConfig.get_http("baseurl")
        prot = localReadConfig.get_http("prot")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()

    def get_url(self):
        '''
        :param cookie:
        :return:
        '''
        if self.method == "get":
            if self.paras == "":
                actualurl = self.baseurl + self.module
            else:
                actualurl = self.baseurl + self.module +'?' + str(self.paras.encode())
        elif self.method == "post":
            actualurl = self.baseurl + self.module
        elif self.method == "put":
            actualurl = self.baseurl + self.module
        elif self.method == "delete":
            actualurl = self.baseurl +self.module
        else:
            raise ("参数组装异常错误！")
        print(actualurl)
        return actualurl

    def send_with_cookie(self, cookie):
        '''
        :param cookie:
        :return:
        '''

        try:
            print("发送请求")
            if self.module == 'get':
                respone = requests.get(url=self.get_url(), headers=self.header)
            elif self.method == 'post':
                respone = requests.get(url=self.get_url(), data=self.paras.encode(), headers=self.header)
            elif self.method == 'delete':
                respone = requests.get(url=self.get_url(), headers=self.header)
            elif self.method == 'put':
                respone = requests.get(url=self.get_url(), headers=self.header, data=self.paras.encode())
            else:
                raise ('unsupported method!')
            respone.raise_for_status()
            return respone.text
        except requests.RequestException as e:
            print(e)
            return False

    def send_with_cookie(self):
        '''
        :param cookie:
        :return:
        '''

        try:
            print("发送请求")
            if self.module == 'get':
                respone = requests.get(url=self.get_url(), headers=self.header)
            elif self.method == 'post':
                respone = requests.get(url=self.get_url(), data=self.paras.encode(), headers=self.header)
            elif self.method == 'delete':
                respone = requests.get(url=self.get_url(), headers=self.header)
            elif self.method == 'put':
                respone = requests.get(url=self.get_url(), headers=self.header, data=self.paras.encode())
            else:
                raise ('unsupported method!')
            respone.raise_for_status()
            return respone.text
        except requests.RequestException as e:
            print(e)
            return False