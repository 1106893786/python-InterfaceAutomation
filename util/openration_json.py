import json

class OnpreaJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = r"C:\untitled2\data_config\indexjson.json"
        else:
            self.file_path = file_path
        self.data = self.read_json()

    def get_data(self,id=None):
        if id !=None:
            return self.data[id]
        else:
            return self.data

    def read_json(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
        return data

    def get_cookie(self):
        pass


if __name__ == '__main__':
    # opjson = OnpreaJson(file_path=r'D:\25自动化套餐\17.【项目实战】Python接口自动化从设计到开发，测试框架实战与自动化进阶视频课程\project\p22naf\dataconfig\user.json')
    opjson = OnpreaJson()
    print(opjson.read_json())
    print(opjson.get_data())