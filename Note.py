import datetime

last_id = 0
class Note:
    """__ double underscore make it prrivate. available only within the class.
acceser means that they want them to be able to read them. need to make a def getID.
to get a mutator you need to make a def wit setId example.
    """
    def __init__(self, memo, tags = ''):
        self.memo = memo
        self.tags = tags
        self.__creationDate = datetime.date.today()
        global last_id
        last_id += 1
        self.__id = last_id

    def getId(self):
        return self.__id

    def getCreationDate(self):
        return self.__creationDate

    def match (self, keyword):
        '''
        Determine if this note matches the keyword text
        :param keyword: searche text. Case sensitive search.
        :return: Returns True if matches, False otherwise
        '''
        return keyword in self.memo or keyword in self.tags
    
