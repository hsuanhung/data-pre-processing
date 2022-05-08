import pandas as pd

'''
This file is using to categories the column A3
'''


# old_file = pd.read_csv('3425_data.csv')
old_file = pd.read_csv('3425_clear.csv')
new_file = pd.read_csv('3425_reverse.csv')


print(len(old_file['A3']))

count = 0
fcount = 0
elseCount = 0
count2 = 0

tmp = []
for i in range(len(old_file)):
    # not positive
    if old_file['A3'][i] >=0 and old_file['A3'][i] <= 5:
        tmp.append("not positive")
        # male == 1
        count +=1

    # positive
    elif old_file['A3'][i] > 5  and old_file['A3'][i] < 8:
        tmp.append("positive")
        fcount +=1

    # very positive
    else:
        tmp.append("very positive")
        elseCount +=1

    # print(len(tmp))

new_file['A3'] = tmp
new_file.to_csv('3425_reverse.csv', index=False)
print("A3 cate done")


print("tier 1 = ", count)
print("tier 2 = ", fcount)
# print("tier3 = ", count2)

print("else = ", elseCount)




# ww = 

#  writer2 = pd.ExcelWriter('test1216_copy.xlsx')

# dfExcel_old.to_csv(writer2, , index = False)
# dfExcel_new.to_excel(writer2, sheet_name = 'new', index = False)
