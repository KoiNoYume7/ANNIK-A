import configparser
import os

class Config():
    def __init__(self, path):
        self.path = path

    def loadcfg(self, filename) -> dict:
        """
        Load the configuration file and return a dictionary of all the values.

        Returns:
            A dictionary containing all the values from the configuration file.
        """
        cfgpath = os.path.join(self.path, filename)
        rconfig = configparser.ConfigParser()
        rconfig.read(cfgpath)
        config = {}
        for section in rconfig.sections():
            for option in rconfig.options(section):
                config[option] = rconfig.get(section, option)
        return config