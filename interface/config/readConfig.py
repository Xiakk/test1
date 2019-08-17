import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, 'w')
            file.write(data)
            file.close()
        fd.close()

        self.config = configparser.ConfigParser()
        self.config.read(configPath)

    def get_http(self, name):
        value = self.config.get("HTTP", name)
        return value
    def get_email(self, name):
        value = self.config.get("EMAIL", name)
