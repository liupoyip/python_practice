# %%
# ---藍圖---
class Car():
    name = None
    wheel = None
    seet = None
    steer_wheel = None

    def __init__(self, name, wheel, seet, steer_wheel):
        # initialize
        self.name = name
        self.wheel = wheel
        self.seet = seet
        self.steer_wheel = steer_wheel

    def show_status(self):
        print(
            f'{"name:":<13s}{self.name:>20s}\n'
            f'{"wheel:":<13s}{self.wheel:>20s}\n'
            f'{"seet:":<13s}{self.seet:>20s}\n'
            f'{"steer wheel:":<13s}{self.steer_wheel:>20s}\n'
        )

    def step_on_accelerator(self):
        print('Acceleration!!')
# ------
