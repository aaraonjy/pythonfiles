class MyClass:
    
    string = "Test String"
    string2 = "Test String 2"

    def function(self):
        print("String Message from Function() class")

myobjectx = MyClass()
print(myobjectx.string2)#Print specific variable only

myobjectx.function()#Access the entire function


myobjecty = MyClass()
myobjecty.string = "Modified"
print(myobjecty.string)


