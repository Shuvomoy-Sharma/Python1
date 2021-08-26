# Python1
 # class, object() or instance , method
 # what is init method or constructor
 #self
class Person:
	def __init__(self,firstname,lastname,age):
		# instance variabel
		self.firstname=firstname
		self.lastname=lastname
		self.age=age
# creating object
p1=Person('Victor','sen',22)
# p2=Person('Maria','khatun',20)
print(p1.firstname,p1.lastname,p1.age)
# print(p2.firstname,p2.lastname,p2.age)					
