from abc import abstractmethod, ABC
class TaskRepository(ABC):
    @abstractmethod
    def save(self,task):
        pass

    @abstractmethod
    def find(self,task_id):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def update(self,task):
        pass
    
    @abstractmethod
    def delete(self,task_id):
        pass