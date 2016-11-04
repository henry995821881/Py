class people:
	country ='china'

        @classmethod
	def getCountry(cls):
		return cls.country

	@classmethod
	def setCountry(cls,country):
		cls.country =country

p=people()
print p.getCountry()
print people.getCountry()

p.setCountry("us")

print p.getCountry()
print people.getCountry()

