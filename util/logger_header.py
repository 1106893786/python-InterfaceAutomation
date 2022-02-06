import logging

#定义一个日志收集器
logger = logging.getLogger('Itester')

#设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
logger.setLevel('DEBUG')

#设置日志格式
fmt = logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')

#设置日志处理器，输出到文件
file_headler = logging.FileHandler(r'C:\untitled2\log\log.txt')

#设置日志处理器级别
file_headler.setLevel('DEBUG')

#处理器按指定格式输出到日志
file_headler.setFormatter(fmt)

#输出到控制台
ch = logging.StreamHandler()
#设置日志处理器级别
ch.setLevel('DEBUG')
#处理器按指定格式输出日志
ch.setFormatter(fmt)

#收集器和处理器对接，指定输出渠道
#日志输出到文件
logger.addHandler(file_headler)
#日志输出到控制台
logger.addHandler(ch)

if __name__ == '__main__':
    str(logger.debug('这个深思啊u的活塞i大海u很嗲')).encode(encoding='utf-8')
