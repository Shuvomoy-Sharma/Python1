 # class, object() or instance , method
 # what is init method or constructor
 #self
class Person:
	def __init__(self,firstname,lastname,age,dob):
		# instance variabel
		self.firstname=firstname
		self.lastname=lastname
		self.age=age
		self.dob=dob
# creating object
p1=Person('Victor','sen',22,'1900-02-02')
# p2=Person('Maria','khatun',20)
print(p1.firstname,p1.lastname,p1.age)
# print(p2.firstname,p2.lastname,p2.age)					
