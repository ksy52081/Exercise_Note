

for i in file25_list:
    globals()['df{}'.format(i)]=[i]
    
    
for j in range(3,7):
    print(globals()['variable{}'.format(j)])
