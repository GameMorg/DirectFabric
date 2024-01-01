def start():
    Shc = int(input('Введите ширину спины '))
    Rost = int(input('Введите рост '))
    h = int(input('Введите высоту плеча '))
    A8P1 = int(input('Введите ширину плеча '))
    mc_M = int(input('Введите расстояние от 7 шейного позвонка до стены '))

    Mr = Rost / 34
    Mg = Shc / 10

    if Mg > Mr:
        M = Mg
    else:
        M = Mr
    mc = (mc_M / M)

    AT = 8.75 * Mr
    T9T5 = 5 * Mg
    AA9 = 0.5 * Mr
    AA8 = 1.25 * Mr
    A8P = 2.5 * Mr
    DTS = (mc - M) / 2

    if DTS == 0:
        P1P2 = 0.25 * Mr
    else:
        P1P2 = 0.5 * Mr

    if mc <= 1.25 * M:
        P1P6 = 2 * M
    else:
        P1P6 = 2 * M + DTS
    print('Ширина спины', Shc)
    print('рост', Rost)
    print('высота плеча', h)
    print('ширина плеча', A8P1)
    print('расстояние от 7 шейного позвонка до стены', mc_M)
    print('Мр =', Mr)
    print('Мг =', Mg)
    print('М =', M)
    print('mc =', mc)
    print('АТ =', AT)
    print('Т9Т5 =', T9T5)
    print('АА9 =', AA9)
    print('АА8 =', AA8)
    print('А8П =', A8P)
    print('ДТС =', DTS)
    print('П1П2 =', P1P2)
    print('П1П6 =', P1P6)


if __name__ == '__main__':
    start()
