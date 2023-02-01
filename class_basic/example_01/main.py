class PeriodicTable:
    family_num = None
    element_list = None

    def show_status(self):
        print(f'Family Num: {self.family_num}')
        print(f'Family Num: {self.element_list}')


class ElementFamily1(PeriodicTable):
    def __init__(self):
        self.family_num = 0
        self.element_list = ['H', 'Li', 'Na', 'Ka', 'Ru', 'Cs', 'Fr']


class ElementFamily18(PeriodicTable):
    def __init__(self):
        self.family_num = 18
        self.element_list = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']


ElementFamily1().show_status()
ElementFamily18().show_status()
