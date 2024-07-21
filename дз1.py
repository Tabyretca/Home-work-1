ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
command = input("Напишите команду: ")
result = any(word in command for word in ignore)
if result:
    print('Команда игнорируется')
else:
    print('Команда выполнена')
