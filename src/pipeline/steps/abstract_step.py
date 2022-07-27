from abc import ABCMeta, abstractmethod


class AbstractStep(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def run(cls, dataset):
        """Запускает шаг пайплайна."""
