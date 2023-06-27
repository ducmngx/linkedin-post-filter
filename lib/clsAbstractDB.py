'''
This is an abstract class for Database.
Required methods by database class will be defined here
Methods will be implemented in the subsequent child classes
'''

from abc import ABC, abstractmethod

class clsAbstractDatabase(ABC):

    @abstractmethod
    def start_connection(self):
        pass

    @abstractmethod
    def end_connection(self):
        pass

    @abstractmethod
    def run_query(self, query: str):
        pass

    @abstractmethod
    def get_data(self, query: str):
        pass

    @abstractmethod
    def get_headers(self, query: str):
        pass

