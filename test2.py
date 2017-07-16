from types import MethodType

class Student(object):
	__slots__=('name','age')
	def set_score(self,score):
		self.score=score

# s=Student()
# s.name='abx'
# print(s.name)

# def set_age(self,age):
# 	self.age=age

# s.set_age=MethodType(set_age,s)
# s.set_age(25)
# print(s.age)

# s2=Studert()
# s2.set_age(25)
# print(s2.age)

# s3=Student()
# s3.set_score(100)
# print(s3.score)

s4=Student()
s4.name="aaaa"
s4.age=22
# s4.score=100
print(s4.name+s4.age)