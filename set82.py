    
num = input()
key = 'aeiou'
for i in key:
    if i in num:
        num = ''
        break
    else:
        continue
if num == '':
    print('yes')
else:
    print('no')
