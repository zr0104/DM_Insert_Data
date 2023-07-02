# logger.py
import logging
import time
import os
from datetime import datetime
import pytz
import timezone_change


class MyLogging:
    def __init__(self):
        self.time_str = datetime.now()
        self.Mexico_time = timezone_change.timezone_change("{}".format(self.time_str.strftime("%Y-%m-%d %H:%M:%S")),
                                                           src_timezone="Asia/Shanghai", dst_timezone="Asia/Shanghai",
                                                           time_format="%Y-%m-%d %H:%M:%S")

    def mexico_time(self,what):
        date_time_M = pytz.timezone("Asia/Shanghai")
        date_time_MEX = datetime.now(date_time_M)
        return date_time_MEX.timetz()

    logging.Formatter.converter = mexico_time

    def get_log(self,file_name):
        time_str = datetime.now()
        Mexico_time = timezone_change.timezone_change("{}".format(time_str.strftime("%Y-%m-%d %H:%M:%S")),
                                                           src_timezone="Asia/Shanghai",
                                                           dst_timezone="Asia/Shanghai",
                                                           time_format="%Y-%m-%d %H:%M:%S")
        timestr = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'logs'))
        filename = lib_path + '/' + file_name + '.log'  # 日志文件的地址
        self.logger = logging.getLogger()  # 定义对应的程序模块名name，默认为root
        self.logger.setLevel(logging.INFO)  # 必须设置，这里如果不显示设置，默认过滤warning之前的所有级别信息

        sh = logging.StreamHandler()  # 日志输出到屏幕控制台
        sh.setLevel(logging.INFO)  # 设置日志等级

        fh = logging.FileHandler(filename=filename,encoding='UTF-8')  # 向文件filename输出日志信息
        fh.setLevel(logging.INFO)  # 设置日志等级

        # 设置格式对象
        formatter = logging.Formatter(
            "%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s - log message: %(message)s"
        )  # 定义日志输出格式

        # 设置handler的格式对象
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 将handler增加到logger中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
        return self.logger


if __name__ == "__main__":
    # log = MyLogging().logger
    log = MyLogging().get_log("test_")
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
