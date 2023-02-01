def mutilple_arguments(*args):
    print(args)


def keywords_arguments(**kargs):
    print(kargs)


mutilple_arguments(1, 2, 3, 4)
keywords_arguments(a=1, b=2, c=3, d=4)
