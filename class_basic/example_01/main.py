# %%
class AnimalFourFeetsMammal:
    head = None
    body = None
    feets_num = 4
    tail = None

    def eat_food(self):
        print('oishii')

    def scream(self):
        print('AHHHHHH!!!!')


class Dog(AnimalFourFeetsMammal):
    def __init__(self, head):
        self.head = head

    def scream(self):
        super().scream()
        print('WanWan')


class Cat(AnimalFourFeetsMammal):
    def __init__(self, head):
        self.head = head

    def scream(self):
        super().scream()
        print('MeowMeow')


dog = Dog('Dog head')
print(dog.head)
dog.scream()

print()

cat = Cat('Cat head')
print(cat.head)
cat.scream()
