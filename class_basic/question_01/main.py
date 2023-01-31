class Alcohol:
    drink_name = None
    concentration = None
    kcal = None
    ingredients = None
    bartending = None

    def __init__(self,
                 drink_name,
                 concentration,
                 kcal,
                 ingredients,
                 bartending):
        # initialize
        self.drink_name = drink_name
        self.concentration = concentration
        self.kcal = kcal
        self.ingredients = ingredients
        self.bartending = bartending

    def show_status(self):
        print(
            f'Drink name: {self.drink_name}\n'
            f'Concentration: {self.concentration}\n'
            f'kcal: {self.kcal}')
        print('Ingredients:', end='\n\t')
        print(*self.ingredients, sep='\n\t')
        print(f'Bartending: {self.bartending}')

    def show_warning_sign(self):
        print('開車不喝酒，酒後開車進監獄')

    def show_if_good_to_bartending(self):
        if self.bartending:
            print('This drink is good to bartending!')
        if self.bartending == False:
            print('This drink is bad to bartending!')


drink = Alcohol(drink_name='Asahi Super Dry',
                concentration=0.06,
                kcal=50.0,
                ingredients=['麥芽', '啤酒花', '大麥', '米', '玉米', '澱粉', '大麥萃取物'],
                bartending=False)

drink.show_status()
drink.show_warning_sign()
drink.show_if_good_to_bartending()
