from typing import Union


def plus(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y + 87


x = 1
y = 2
result = plus(x, y)
print(result)
