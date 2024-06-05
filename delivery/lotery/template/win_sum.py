import random

imy = input('Введите ваше имя: ')
second_imy = input('Введите ваше отчество ')

sum = random.randint()

def all_sum():
    if sum == 1000:
        return(imy + second_imy + ' тыща', split = ',')
    elif sum == 1000000:
        return(imy + second_imy + 'лимон')    
    else:
        print(f'Ваша сумма: ', {sum})
all_sum()
print(all_sum())    


