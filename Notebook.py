from Note import Note

class Notebook:
    '''
    Represents a collection of notes
    that can be modified or tagged and/or searched
    '''

    def __init__(self):
        '''Data Stractures: Array (a collection or a list of data, access the
        the value thru index)
        '''
        self.__notes = []
        
    def getNotes(self):
        return self.__notes
    
    def new_note(self, memo, tags = ''):
        n = Note(memo, tags)
        self.__notes.append(n)

    def modify_memo(self, note_id, memo):
        n= self.__find_note(note_id)
        if not n: #si no tiene un valor
            print ("Note not found. Try again.")
        else:
            n.memo = memo

    def modify_tags(self, note_id, tags):
        n= self.__find_note(note_id)
        if not n: #si no tiene un valor
            print ("Note not found. Try again.")
        else:
            n.tags = tags

    def __find_note(self, note_id):
        for note in self.__notes:
            if note.getId()== note_id:
                return note
        return None

    def search(self, filter):
        '''
        Find all notes that matches the given filter
        :param filter: keyword to search
        :return: notes that mathc the filter
        '''
        return [note for note in self.__notes if note.match(filter)]
