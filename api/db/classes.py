class ReadOnlyCollection:
    def __init__(self, collection):
        self.__collection = collection
    
    def find(self, *args, **kwargs):
        return self.__collection.find(*args, **kwargs)

    def find_one(self, *args, **kwargs):
        return self.__collection.find_one(*args, **kwargs)
    
    def aggregate(self, *args, **kwargs):
        return self.__collection.aggregate(*args, **kwargs)

    def distinct(self, *args, **kwargs):
        return self.__collection.distinct(*args, **kwargs)
    
    def count_documents(self, *args, **kwargs):
        return self.__collection.count_documents(*args, **kwargs)