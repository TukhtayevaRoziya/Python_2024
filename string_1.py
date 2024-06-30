name = 'Roziya'
# str = '''aaaa
# sdfsdf
# ddd'''
course = name + ' ' + 'Tukhtayeva zo\'r odam'
# length = len(course)
# print(course)
# print('Length of sentence is', length)
# print('-'*10, sep='/')
# # print(course.lower())
# print(course.title())

str = '             python             '
print(str)
print(str.strip()) #remove a space from str text
print(str.lstrip()) #remove a space from left side of str(or we have rstrip)
print(course.replace('Roziya', "Zizi"), course)
print(course.count('a'))