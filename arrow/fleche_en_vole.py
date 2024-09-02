def scene( speed, distance, etape):
    field = list("."*distance)
    field[distance - 1] = 'C'
    if (speed*etape < distance):
        field[speed*etape] = '>'
    else:
        field[:-1] = '>'
    for i  in range(distance):
        print(field[i], end = '')
    print("\n")



def ft_putArrow( speed,  distance):
    i = 0
    while (speed*i < distance):
        scene(speed, distance, i)
        i += 1

if  __name__ == '__main__':
    speed = 5
    distance = 30
    ft_putArrow(speed, distance)
