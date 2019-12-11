class Animal:
    location = "earth"

    def test(self):
        return 'test'

    def location_info(self):
        return self.location

    def __private_function(self):  # with __,create a private function
        return self.location

    def test_private(self):
        str1 = self.__private_function(self)
        return str1


class Cat(Animal):
    kind = "cat"
    location = "North American"

    def location_info(self):
        return self.location


a = Animal()
cat1 = Cat()
print(cat1.location)
print(cat1.location_info())  # call parent class method with different name
print(cat1.test())
# print(cat1.location_info(Animal)) # not work
print(Animal.location)
# print(Animal.location_info()) # not work
print(Animal.location_info(type(a)))
print(Animal.location_info(Animal))  # call parent class method not have a instance
print(isinstance(cat1, Animal))  # cat1 is an instance of Animal
print(isinstance(Cat, Animal))  # but Cat is not instance ,Cat is class
print(issubclass(Cat, Animal))
# print(Animal.__private_function(type(a))) # private function,can not access outside Animal class
print(Animal.test_private(Animal))  # function in class call another private function in same calss
