from abc import ABC, abstractmethod
from models.student import Student

class StudentInterface(ABC):
    
    @abstractmethod
    def importData():
        pass
    
    @abstractmethod
    def addStudent(student : Student):
        pass
    
    @abstractmethod
    def updateStudent(student : Student):
        pass
    
    @abstractmethod
    def deleteStudent(student_id: int):
        pass
    
    @abstractmethod
    def getStudent(student_id: int):
        pass
    
    @abstractmethod
    def getAll():
        pass
    