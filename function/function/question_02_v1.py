# %%
def transpose_list_v1(num_list_summary):

    print(
        f'List size before transposed: {len(num_list_summary)} x {len(num_list_summary[0])}\n'
        'result:')
    for num_list in num_list_summary:
        for num in num_list:
            print(f'{num},', end='')
        print()

    num_list_summary_tranposed = list()
    for i in range(len(num_list_summary[0])):
        num_list_summary_tranposed.append(list())
        for j in range(len(num_list_summary)):
            num_list_summary_tranposed[i].append(num_list_summary[j][i])

    print(
        f'List size after transposed: {len(num_list_summary_tranposed)} x {len(num_list_summary_tranposed[0])}\n'
        'result:')
    for num_list in num_list_summary_tranposed:
        for num in num_list:
            print(f'{num},', end='')
        print()

    return num_list_summary_tranposed


num_list_1 = list(range(1, 4))
num_list_2 = list(range(4, 7))
num_list_3 = list(range(7, 10))
num_list_summary = [num_list_1, num_list_2, num_list_3]
num_list_summary_tranposed = transpose_list_v1(num_list_summary)
