import pandas as pd

'''
This file is doing the value reverse
'''

old_file = pd.read_csv('3425_clear.csv')
new_file = pd.read_csv('3425_reverse.csv')

def reverseA1():
    print(len(old_file['A1']))
    print(old_file['A1'])

    tmp = []
    for i in range(len(old_file['A1'])):
        tmp.append(6 - old_file['A1'][i])

    new_file['A1'] = tmp


    print(old_file['A1'])

    new_file.to_csv('3425_reverse.csv', index=False)

    print("A1 done")

def reverseB4():
    tmp = []
    for i in range(len(old_file['B4'])):
        tmp.append(5 - old_file['B4'][i])

    new_file['B4'] = tmp


    # print(old_file['B4'])

    new_file.to_csv('3425_reverse.csv', index=False)
    print("B4 done")

    # pass

def reverseB6():
    col = ["f", "g"]

    # tmp = []
    for j in col:
        tmp = []
        for i in range(len(old_file[f'B6{j}'])):
            tmp.append(6 - old_file[f'B6{j}'][i])

        new_file[f'B6{j}'] = tmp


        # print(old_file['A1'])

        new_file.to_csv('3425_reverse.csv', index=False)

    print("B6 done")


reverseA1()
reverseB4()
reverseB6()

