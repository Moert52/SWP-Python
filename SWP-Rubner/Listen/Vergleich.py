from tabulate import tabulate
data = [
['', 'Single', 'Double', 'Array', 'Single', 'Double', 'Array', 'Single', 'Double', 'Array'],
['append', 'n', '1', '1', 'n', '1', '1', 'n', '1', 'n'],
['getLastElement', 'n', '1', '1', 'n', '1', '1', 'n', '1', '1'],
['getLength', 'n', 'n', '1', 'n', 'n', '1', 'n', 'n', '1'],

['printAllElements', 'n', 'n', '1', 'n', 'n', '1', 'n', 'n', 'n'],
['getIndexOfElement', '1', '1', '1', 'n*log(n)', 'n*log(n)', 'n*log(n)', 'n', 'n', 'n'],
['getElementbyIndex', '1', '1', '1', 'n*log(n)', 'n*log(n)', '1', 'n', 'n', '1'],
['delete', '1', '1', '1', 'n', 'n', '1', 'n', 'n', '1'],
['find', '1', '1', '1', 'n', 'n', 'n', 'n', 'n', 'n'],
['insertAfter', '1', '1', '1', 'n', 'n', 'n', 'n', 'n', 'n'],

]
print (tabulate(data, headers=["Method","|", "Best Case","","|", "Avarage Case","","|", "Worst Case","|"], numalign="center"))