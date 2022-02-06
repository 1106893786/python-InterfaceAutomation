import json
import unicodecsv
import operator
class CommonUtil:

    #判断一个字符串是否在另一个字符串中
    def is_contain(self,str_one,str_two):
        '''
        :param str_one: 查找的字符串
        :param str_two:被查找的字符串
        :return:
        '''
        flag = None
        # isinstance(str_one,unicode)
        # if isinstance(str_one, unicode):
        #     str_one = str_one.encode('unicode-escape').decode('string_escape')
        # return cmp(str_one, str_two)
        # for str_one in str_two:
        #     if (str_one in str_two):
        #         flag = True
        #     else:
        #         flag = False
        #     return flag
        count = str(str_two).find(str(str_one))
        if count != -1:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
            # print('dict_one',dict_one)
            # print('dict_onetype',type(dict_one))
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
            # print('dict_two', dict_two)
            # print('dict_twotype', type(dict_two))
        return operator.eq(dict_one, dict_two)