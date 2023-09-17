import threading





class MemoryAccessor:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.next_free_address = INIT_ADDRESS

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(MemoryAccessor, cls).__new__(cls)
        return cls._instance

    # def write(self, ):
    #     with self._lock:



if __name__ == "__main__":
    mem_acc: MemoryAccessor = MemoryAccessor()

