def ninja(code):
    print('Function check...')
    if not isinstance(code, list):
        raise BaseException('ninja say: 87')
    if len(code) != 3:
        raise BaseException('ninja say: 87分不能再高了')
    if code[0] != int(0xFF):
        raise BaseException('ninja say: You are not a pro ninja, but you do better!!')
    if code[1] != 'ninja':
        raise BaseException('ninja say: You are a clerkship ninja!!')
    if code[2] != 'I\'m ninja!':
        raise BaseException('ninja say: It\'s very close!! あと一歩')
    print('おめでとうございます！　忍者なれました！')
