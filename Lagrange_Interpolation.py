import matplotlib.pyplot as plt
import numpy as np
import random

SCALE = 100
PAD = 0.05 * SCALE
DOTS = int(input('Enter Number of points\n'))

while DOTS > SCALE:
    print('Invalid. Enter number <= ' + str(SCALE) + '\n')
    DOTS = int(input('Enter Number of points\n'))

data_x = []
data_y = []

for i in range(DOTS):
    value_x = random.randint(0, SCALE)
    value_y = random.randint(0, SCALE)
    while value_x in data_x:
        value_x = random.randint(0, SCALE)

    data_x.append(value_x)
    data_y.append(value_y)

print('Data:')

data = ''
for i in range(len(data_x)):
    coords = '(' + str(data_x[i]) + ', ' + str(data_y[i]) + ') '
    data += coords

print(data + '\n')

show_df = input('Show Delta Functions? (Enter 1) \n')
data_labels = input('Show Data Labels? (Enter 1) \n')

def interpolation(x_value: float) -> float:
    res = 0
    for i in range(len(data_x)):
        pre_i = data_x[:data_x.index(data_x[i])]
        post_i = data_x[data_x.index(data_x[i]) + 1:] 
        coeffs =  pre_i + post_i
        delta_num = 1
        delta_dnm = 1

        if show_df == '1' and x_value == data_x[i]:
            x_delta = np.linspace(-PAD, SCALE + PAD, SCALE * DOTS//2)
            y_delta = []
            for x in x_delta:
                d_num = 1
                d_dnm = 1
                for j in coeffs:
                    d_num *= (x - j)
                    d_dnm *= (data_x[i] - j)
                
                y_delta.append((d_num/d_dnm) * data_y[i])

            plt.plot(x_delta, y_delta, ':', linewidth = 0.95)

        for j in coeffs:
            delta_num *= (x_value - j)
            delta_dnm *= (data_x[i] - j)
        
        delta = (delta_num/delta_dnm) * data_y[i]
        res += delta
    
    return res

domain = np.linspace(-PAD, SCALE + PAD, SCALE * DOTS//2)
x_coord = np.append(domain, data_x)
x_coord.sort()
y_coord = []
for i in x_coord:
    y_coord.append(interpolation(i))

if show_df == '1':
    plt.axis([min(data_x) - PAD, max(data_x) + PAD, 0 - PAD, max(data_y) + PAD])
else:
    plt.axis([min(data_x) - PAD, max(data_x) + PAD, min(data_y) - PAD, max(data_y) + PAD])

plt.xlabel('Locations')
plt.ylabel('Data Values')
plt.title('Lagrange Interpolation')

if data_labels == '1':
    for i in range(len(data_x)):
        label = ' (' + str(data_x[i]) + ', ' + str(data_y[i]) + ')'
        plt.text(data_x[i], data_y[i], label)

plt.plot(x_coord, y_coord, '#9787D2')
plt.scatter(data_x, data_y, 20, '#9787D2')

plt.show()
