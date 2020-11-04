class Student():

    # "__init__" known as constructor, is a special method which is automatically called when an object of Class is created

    def __init__(self, id, name, phone, age):

        # Self is an "Instance Variable" of a class

        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

    '''
    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
    '''
    # Print Object with Formatting
    
    def __str__(self):
        return '\n'.join(( '{} = {}' .format(item, self.__dict__[item]) for item in self.__dict__))

aaron = Student("1001", "Aaron", "012-3034445", 16)
print(aaron)





   
