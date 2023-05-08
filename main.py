from threading import Thread
class AWSObj:
    #__init__(...)` - initialize the object with the bucket/region/AWS-keys to get access to the bucket;
    def __init__(self,bucket, region, keys = []):
        self.__bucket = bucket
        self.__region = region
        self.__keys = keys

    #print the Object just for tests purposes
    def __str__(self):
        return'Bucket:' + self.__bucket + ' | region: ' + self.__region + ' | keys: '+str(self.__keys)

    # get(key: str) -> BytesIO` - to get an object from the S3 bucket from a key;
    def get(self,key):
        my_set = set(self.__keys)
        if  key in my_set:
            return print(self)
        else:
            return print('Key is not present')

    #put(key: str, value: BytesIO)` - to    put    a    new    object in the    bucket;
    def put(self,key,value):
        my_set = set(self.__keys)
        if  key in my_set:
            self.__keys.append(value)
        else:
            return print('Key is not present')

    #pop(key: str) -> >BytesIO` - to remove an object from the bucket and return it;
    def pop(self, key):
        my_set = set(self.__keys)
        if key in my_set:
            self.__keys.remove(key)
            return print(self)
        else:
            return print('Key is not present')

    #__getitem__(key: str) -> BytesIO` - nicer interface for `get`;
    def __getitem__(self,key):
        my_set = set(self.__keys)
        if  key in my_set:
            return print(self)
        else:
            return print('Key is not present')
    #__setitem__(key: str, value: BytesIO)` - nicer interface for `put`;
    def __setitem__(self, key,value):
        my_set = set(self.__keys)
        if key in my_set:
            self.__keys.append(value)
        else:
            return print('Key is not present')
    #__delitem__(key: str)` - nicer interface to `pop` (that does not return anything);
    def __delitem__(self, key):
        my_set = set(self.__keys)
        if key in my_set:
            self.__keys.remove(key)
    #__contains__(key: str) -> bool` - checks if object exists;
    def __contains__(self, key):
        my_set = set(self.__keys)
        if key in my_set:
            return True
     #keys(prefix: str = '') -> str` - generator that yields the keys from S3 bucket with the option to filter with a prefix;
    def keys(self, prefix):
        return list(filter(lambda x: prefix  in x, self.__keys))
     #items(prefix: str = '') -> tuple` - similar to keys, but the generator yields `tuples` of key-value pairs (bonus: make this method multi-threaded);
    def items(self, prefix):
        listed = list(filter(lambda x: prefix in x, self.__keys))
        thread = Thread(target=self.printlist, args =(listed,))
        thread.start()
    def printlist(self,*args):
        for i, name in enumerate(args[0]):
            print ("("+str(i) + ","+name+")")



if __name__ == '__main__':
    result = AWSObj('a', 'pt', ['xxx','cccxxx'])
    result.__setitem__('xxx','ccc')
    result.__getitem__('ccc')
    result.__delitem__('xxx')
    print(result.__contains__('xxx'))
    result.items('c')







