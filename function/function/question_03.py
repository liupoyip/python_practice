def show_alphabet_series(num):
    checker_list = [65, 97]
    if num not in checker_list:
        raise "Input is illegal, only 65 or 97 accepted."

    loop_times = 1024
    end_num = num + loop_times
    level = 1
    # v1 --------------
    ascii_code = num
    while ascii_code < end_num:
        for _ in range(level):
            if ascii_code < end_num:
                print(chr(ascii_code), end='')
                ascii_code += 1
            else:
                break
        print()
        level += 1
    # v2 --------------
    # i = 0
    # ascii_code = num
    # while i < loop_times:
    #     for _ in range(level):
    #         if ascii_code < end_num:
    #             print(chr(ascii_code), end='')
    #             i += 1
    #             ascii_code = num + i
    #         else:
    #             break
    #     level += 1
    #     print()


show_alphabet_series(65)
