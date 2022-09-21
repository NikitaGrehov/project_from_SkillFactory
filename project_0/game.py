import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count +=1
    predict_number = int(input('input number'))

    if predict_number > number:
        print('число меньше')
    elif predict_number < number:
        print('число больше')
    else:
        print(f'правильно! число: {number}, было потрачено {count} попыток')
        break