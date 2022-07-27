from abc import ABCMeta, abstractmethod


class AbstractStep(metaclass=ABCMeta):

    @abstractmethod
    def run(self, dataset):
        pass
