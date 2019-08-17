import logging
from datetime import datetime
import threading
import interface.config.readConfig
import os

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = interface.config.ReadConfig.proDir
        resultPath = os.path.join(proDir, "result")

        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))

        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()

        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(logPath, "output.log"))

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)


class Mylog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def get_log():
        if Mylog.log is None:
            Mylog.mutex.acquire()
            Mylog.log = Log()
            Mylog.mutex.release()

        return Mylog.log
