import numpy as np

#def predict8(number: int = 1) -> int:

number = np.random.randint(1, 1000) # загадываем рандомное число, используя генератор рандомных чисел
print(number)
count = 0
mn = 1
mx = 1000
    
while True:
    count += 1
        #print(count)
    md = round((mn + mx)/2)
        
    if md > number:
        mx = md
    elif md < number:
        mn = md
    else:
        print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
        break # конец игры и выход из цикла
     
    #print(count, number) 
    #return count
    

