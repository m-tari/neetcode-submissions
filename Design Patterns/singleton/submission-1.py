import threading

class Singleton:
    _unique_instance = None
    _instance_lock = threading.Lock()

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                cls._unique_instance = super(Singleton, cls).__new__(cls)

        return cls._unique_instance                

    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str):
        self.val = value
