import logging

logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
#添加formatter日志输出格式

fmt = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')
# logging.basicConfig()

#添加streamHandler，并设置级别为warning

stream_hdl = logging.StreamHandler()
stream_hdl.setLevel(logging.WARNING)
stream_hdl.setFormatter(stream_hdl)
logger.addHandler(stream_hdl)
#将日志打印在指定文件中test.log
file_hdl = logging.FileHandler('test.log')
file_hdl.setLevel(logging.DEBUG)
file_hdl.setFormatter(fmt)
logger.addHandler(file_hdl)


logger.info('I am <info> message.')
logger.debug('I am <debug> message.')