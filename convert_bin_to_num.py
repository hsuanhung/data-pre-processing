import pandas as pd


'''
This file convert binary-coding into num-coding.
'''

old_file = pd.read_csv('3425_clear.csv')
new_file = pd.read_csv('new_output.csv')

# print(len(old_file['A1']))
# print(old_file['A1'])


tmp = []
for i in old_file['opinionated']:
    if i == False:
        tmp.append(0)

    elif i == True:
        tmp.append(1)

    else:
        tmp.append(i)

    
# print()
    
print(len(tmp))
new_file['opinionated'] = tmp

print(new_file['opinionated'])




# print(old_file['A1'])

new_file.to_csv('new_output.csv', index=False)

print("done")
