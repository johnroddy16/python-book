# creating a basic python object with attributes (data) and methods(fubctions):

class PartyAnimal:
    x = 0  # one attibute, x

    def party(self, y=1):  # one method, party  # self is a conventional name 
        self.x += y  # self.x says the x within self, self points to the particular instance of the partyanimal object that party is 
        print('so far %d' % self.x)  # called from 

an = PartyAnimal()  # instruct python to construct an object or instance of the class PartyAnimal, like words = dict()
an.party(4)  # 
an.party(6)
an.party(12)
an.party()
PartyAnimal.party(an, 4)

print(type(an))
print(dir(an))
print()
print(type(an.x))
print(type(an.party))