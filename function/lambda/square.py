# %%
# --- function
def square(x):
    return x ** 2


result = square(2)
print(f'Normal Function: {result}')

# %%
# --- lambda
# syntax: lambda paramter_list : operation
result = (lambda x: x**2)(2)
print(f'Lambda Function: {result}')
