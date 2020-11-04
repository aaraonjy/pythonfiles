class School:

    firstname = ""
    lastname = ""

    def student(self):

        fullname = "Your First Name is %s, Last Name is %s" % (self.firstname, self.lastname)
        return fullname

object1 = School()
object1.firstname = "Aaron"
object1.lastname = "Goh"

print(object1.student())
