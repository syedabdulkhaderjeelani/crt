#move hyphens
'''
s=input()
count_hyphen=s.count('-')
new_str='-'*count_hyphen+s.replace('-',' ')
print(new_str)

                OR
'''
s=input()
count_hyphen=s.count('-')
new_str='-'*count_hyphen+s.replace('-','')
print(new_str)
