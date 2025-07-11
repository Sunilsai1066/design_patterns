class DatabaseConnector:
    _instance = None
    _initialized = False

    def __init__(self):
        if not self.__class__._initialized:
            self.is_connected = False
            self.__class__._initialized = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect_to_database(self):
        self.is_connected = True
        print('Connecting to database')

    def disconnect_from_database(self):
        self.is_connected = False
        print('Disconnecting from database')


if __name__ == '__main__':
    db1 = DatabaseConnector()
    db2 = DatabaseConnector()

    print(id(db1) == id(db2))
