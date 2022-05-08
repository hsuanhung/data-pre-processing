import pandas as pd

old_file = pd.read_csv('3425_new.csv')
# new_file = pd.read_csv('3425_clear.csv')

def delete_A1():
    old_file = pd.read_csv('3425_new.csv')
    new_file = pd.read_csv('3425_clear.csv')


    # print(old_file['A1'])

    drop_row = []

    for i in range(len(new_file['A1'])):
        if new_file['A1'][i] < 1 or new_file['A1'][i] > 5:
            drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(new_file['A1'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[A1] this is old", len(old_file['A1']))
    print("[A1] this is new", len(new_file['A1']))

    print("done")

def delete_B1():
    new_file = pd.read_csv('3425_clear.csv')


    drop_row = []
    drop_col = ['a', 'b', 'c', 'd']
    for col in drop_col:
        for i in range(len(new_file[f'B1{col}'])):
            if new_file[f'B1{col}'][i] < 1 or new_file[f'B1{col}'][i] > 2:
                drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(old_file['A1'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[B4_6] this is old", len(old_file['A1']))
    print("[B4_6] this is new", len(new_file['A1']))

    print("done")

    


def delete_D1():

    new_file = pd.read_csv('3425_clear.csv')


    drop_row = []
    drop_col = ['a', 'b', 'c', 'd', 'e', 'f']
    for col in drop_col:
        for i in range(len(new_file[f'D1{col}'])):
            if new_file[f'D1{col}'][i] < 1 or new_file[f'D1{col}'][i] > 5:
                drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(old_file['A1'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[D1] this is old", len(old_file['A1']))
    print("[D1] this is new", len(new_file['A1']))

    print("done")

# def delete_A1():
#     pass

def delete_E11a():
    new_file = pd.read_csv('3425_clear.csv')

    drop_row = []

    for i in range(len(new_file['E11a'])):
        if new_file['E11a'][i] < 1 or new_file['E11a'][i] > 4:
            drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(new_file['E11a'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[E11a] this is old", len(old_file['A1']))
    print("[E11a] this is new", len(new_file['A1']))

    print("done")


def deleteB4():
    new_file = pd.read_csv('3425_clear.csv')

    drop_row = []

    for i in range(len(new_file['B4'])):
        if new_file['B4'][i] < 1 or new_file['B4'][i] > 5:
            drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(new_file['A1'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[B4] this is old", len(old_file['A1']))
    print("[B4] this is new", len(new_file['A1']))

    print("done")

def deleteB6():
    new_file = pd.read_csv('3425_clear.csv')

    drop_row = []
    drop_col = ['f', 'g']
    for col in drop_col:
        for i in range(len(new_file[f'B6{col}'])):
            if new_file[f'B6{col}'][i] < 1 or new_file[f'B6{col}'][i] > 5:
                drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(old_file['A1'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[B6] this is old", len(old_file['A1']))
    print("[B6] this is new", len(new_file['A1']))

    print("done")


def delete_A3():

    new_file = pd.read_csv('3425_clear.csv')

    drop_row = []

    for i in range(len(new_file['A3'])):
        if new_file['A3'][i] < 0 or new_file['A3'][i] > 10:
            drop_row.append(i)

    new_file = new_file.drop(drop_row)

    # print(new_file['E11a'])

    new_file.to_csv('3425_clear.csv', index=False)
    print("[A3] this is old", len(old_file['A1']))
    print("[A3] this is new", len(new_file['A1']))

    print("done")

delete_A1()

delete_B1()
delete_D1()
delete_E11a()
deleteB4()
deleteB6()

delete_A3()