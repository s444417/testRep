from abc import ABCMeta, abstractmethod

class Cleaneable(metaclass=ABCMeta):
    @abstractmethod
    def doClean(self):
        pass
