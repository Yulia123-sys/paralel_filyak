import os 

file = open('Практична_3.txt', 'w', encoding='utf-8')  
file.write('Новий файл і записані в нього дані') 
file.write('\n Харук Юлія \n')

file = open('Практична_3.txt', encoding='utf-8') 
print(file.read())

file.close()
