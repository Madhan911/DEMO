import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class readConfig:
    @staticmethod
    def getApllicationURL():
        url = config.get('common info', 'baseURL')
        return url


