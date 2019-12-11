class Family:
    def show_family(self):
        print("This is our family:")


# Father class inherited from Family
class Father(Family):
    father_name = ""

    def show_father(self):
        print(self.father_name)


# Mother class inherited from Family
class Mother(Family):
    mother_name = ""

    def show_mother(self):
        print(self.mother_name)


# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


class Daughter(Father, Mother):
    def __init__(self, f, m):
        self.father_name = f
        self.mother_name = m

    def show_parent(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


s1 = Son()  # Object of Son class
s1.father_name = "Mark"
s1.mother_name = "Sonia"
s1.show_family()
s1.show_parent()
s2 = Daughter('Sawyer', 'Sophie')
s2.show_family()
s2.show_parent()