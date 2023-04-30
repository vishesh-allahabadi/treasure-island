# Switching numbers wihtout introducing 3rd variable

a = int(input('a:'))
b = int(input('b:'))
print('a = ' + str(a))
print('b = ' + str(b))


a = a + b
b = a - b
a = a - b

print('New a = ' + str(a))
print('New b = ' + str(b))
