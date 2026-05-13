from abc import ABC, abstractmethod

class IWindow(ABC):
    
    @abstractmethod
    def start(self):
        pass
     
    
        