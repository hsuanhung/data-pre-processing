from hashlib import new
import pandas as pd

'''
this py file is using to combine the element of columns into a new column.
'''

old_file = pd.read_csv('3425_reverse.csv')
new_file = pd.read_csv('new_output.csv')

# print(len(old_file['A1']))
# print(old_file['A1'])
data_size = len(old_file)


def CombineB1a_d():
    col = ["a", "b", "c", "d"]
    
    tmp = []
    for i in range(data_size):
        count = 0
        for c in col:
            count += old_file[f'B1{c}'][i]
        tmp.append(count)
    
    new_file['B1'] = tmp




def CombineB4_6():
    col = ["4", "6f", "6g"]

    tmp = []
    for i in range(data_size):
        count = 0
        for c in col:
            count += old_file[f'B{c}'][i]
        tmp.append(count)
    
    new_file['B4-6'] = tmp
    # pass

def CombineD1a_f():
    col = ["a", "b", "c", "d", "e", "f"]

    tmp = []
    for i in range(data_size):
        count = 0
        for c in col:
            count += old_file[f'D1{c}'][i]
        tmp.append(count)
    
    new_file['D1'] = tmp
    # pass



# just copy and paste

new_file['A1'] = old_file['A1']
new_file['E11a'] = old_file['E11a']
new_file['A3'] = old_file['A3']
new_file['opinionated'] = old_file['opinionated']

CombineB1a_d()
CombineB4_6()
CombineD1a_f()

new_file.to_csv('new_output.csv', index=False)



print("done")

