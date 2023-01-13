def hello(world):
    print('function check...', end='')
    if not isinstance(world, list):
        raise BaseException(
            'haha, you get error ^_^ || Input tpye: list')
    print('Pass!!')
