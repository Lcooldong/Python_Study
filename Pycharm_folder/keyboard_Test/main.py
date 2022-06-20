# X, Y 평면 끝점 도달 방지용
# 원하는 방향 쪽에 최대한 가깝게 감

import keyboard as kb
import time
import math

num = 0
x_direction = 0
y_direction = 0

# Max reach 320mm, Z_offset -> fixed
z_offset = 50   # height of TCP
safe_offset = 20
R_max_pow = math.pow(320 - safe_offset, 2) - math.pow(z_offset, 2)
print("round : {} mm".format(R_max_pow))

# Robot Setup
x_point = 0
y_point = 0
speed = 5


# example - do not use
point_list = {'x': 0, 'y': 0}
X_example = math.pow(point_list['x'], 2)
Y_example = math.pow(point_list['y'], 2)
R_example = X_example + Y_example + math.pow(z_offset, 2)


def get_max_y(x_value):
    if R_max_pow > math.pow(x_value, 2):
        y_value = math.sqrt(R_max_pow - math.pow(x_value, 2))
        return y_value
    else:
        return -1


def get_max_x(y_value):
    if R_max_pow > math.pow(y_value, 2):
        x_value = math.sqrt(R_max_pow - math.pow(y_value, 2))
        return x_value
    else:
        return -1


def get_round_pow(x_value, y_value):
    x_pow = math.pow(x_value, 2)
    y_pow = math.pow(y_value, 2)
    r_pow = x_pow + y_pow
    return r_pow


if __name__ == '__main__':

    while True:
        # print(kb.read_key())
        if kb.is_pressed("right"):
            x_direction = 1
        elif kb.is_pressed("left"):
            x_direction = -1
        elif kb.is_pressed("up"):
            y_direction = 1
        elif kb.is_pressed("down"):
            y_direction = -1
        else:
            x_direction = 0
            y_direction = 0

        x_point = x_point + speed * x_direction
        y_point = y_point + speed * y_direction

        R_pow = get_round_pow(x_point, y_point)

        print(R_max_pow, R_pow)

        while R_max_pow <= R_pow:
            if (x_point > 0) and (y_point > 0):
                x_point = x_point - speed
                y_point = y_point - speed
            elif (x_point < 0) and (y_point > 0):
                x_point = x_point + speed
                y_point = y_point - speed
            elif (x_point > 0) and (y_point < 0):
                x_point = x_point - speed
                y_point = y_point + speed
            elif (x_point < 0) and (y_point < 0):
                x_point = x_point + speed
                y_point = y_point - speed

            elif (x_point > 0) and (y_point == 0):
                x_point = x_point - speed
            elif (x_point < 0) and (y_point == 0):
                x_point = x_point + speed
            elif (x_point == 0) and (y_point > 0):
                y_point = y_point - speed
            elif (x_point == 0) and (y_point < 0):
                y_point = y_point + speed

            R_pow = get_round_pow(x_point, y_point)
            print(f'Back to the Safe line : {R_pow}')
            time.sleep(0.1)

        print(f'X : {x_point}, Y : {y_point}')
        time.sleep(0.1)

