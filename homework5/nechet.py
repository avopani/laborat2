
def get_number():
    for number in range(30):
        if number % 2 != 0:  
            yield number  
          
def numb():

    numbers = list(get_number())
    print('Все нечетные числа:',numbers)  
    print(f'1-е нечетное число:{numbers[0]};\n 5-е нечетное число: {numbers[4]};\n последнее нечетное число: {numbers[-1]}')
    

numb()


