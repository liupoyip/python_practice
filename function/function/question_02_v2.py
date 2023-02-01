# %%
def transpose_list_v2(num_list_summary):

    print(
        f'List size before transposed: {len(num_list_summary)} x {len(num_list_summary[0])}\n'
        'result:')
    for num_list in num_list_summary:
        print(''.join([f'{num},' for num in num_list]))

    num_list_summary_tranposed = list()
    for num_1, num_2 in zip(num_list_summary[0], num_list_summary[1]):
        num_list = [num_1, num_2]
        num_list_summary_tranposed.append(num_list)

    print(
        f'List size after transposed: {len(num_list_summary_tranposed)} x {len(num_list_summary_tranposed[0])}\n'
        'result:')
    for num_list in num_list_summary_tranposed:
        print(''.join([f'{num},' for num in num_list]))

    return num_list_summary_tranposed


num_list_1 = list(range(1, 4))
num_list_2 = list(range(4, 7))
num_list_summary = [num_list_1, num_list_2]
num_list_summary_tranposed = transpose_list_v2(num_list_summary)
