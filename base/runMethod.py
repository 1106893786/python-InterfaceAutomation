import requests
from response import Response
import json

class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header !=None:
            res = requests.post(url = url,data=data,headers=header)
        else:
            res = requests.post(url = url,data=data)
        # print(res.encoding)
        # return json.dumps(res,indent=2)
        return res

    def get_main(self,url,data=None,header=None):
        res = None
        if header !=None:
            res = requests.get(url = url,data=data,headers=header)
        elif data!=None:
            res = requests.get(url = url,data=data)
        else:
            res = requests.get(url=url)
        return res

    def run_main(self,method,return_type,url,data,header):
        res = None
        if method == 'post' or method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        if return_type == 'json':
            return res.json()
        else:
            return str(res.status_code)
        # return json.dumps(res,indent=2)
        # print("res_runmain",res)
        # print("res.json",json.loads(res.text))
        # return res

if __name__ == '__main__':
    r = RunMethod()
    # print(r.get_main(url='http://www.baidu.com/',data=None,header=None))
    # s = r.run_main(method="get",return_type='html', url='http://www.baidu.com/s',
    #            data={"wd": "123", "ie": "utf-8", "tn": "SE_PSStatistics_p1d9m0nf"}, header=None)
    # s = r.run_main(method='get',return_type='html',url="http://www.baidu.com",data=None,header=None)
    # print(s.status_code)
    s = requests.request(method='get',url='http://www.baidu.com',data = None,headers = None)
    print(s)
    print(s.cookies)
