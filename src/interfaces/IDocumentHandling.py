from abc import ABC, abstractmethod

class IDocumentHandling(ABC):

    @abstractmethod
    def write_character(self):
        pass

    @abstractmethod
    def remove_character(self):
        pass

    @abstractmethod
    def insert_text(self, document):
        pass
