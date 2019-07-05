from abc import ABCMeta, abstractmethod
class Channel(metaclass=ABCMeta):
    queue = []
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def Clogin(self):
        pass
    @abstractmethod
    def storeCredentials(self):
        pass
    @abstractmethod
    def sniffer(self):
        pass
    @abstractmethod
    def sendM(self):
        pass
