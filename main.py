def start():
    Shc = int(input('Введите ширину спины '))
    Rost = int(input('Введите рост '))
    h = int(input('Введите высоту плеча '))
    A8P1 = int(input('Введите ширину плеча '))
    tc_M = int(input('Введите расстояние от 7 шейного позвонка до стены '))

    Mr = Rost / 34
    Mg = Shc / 10

    if Mg > Mr:
        M = Mg
    else:
        M = Mr
    tc = (tc_M / M)

    AT = 8.75 * Mr
    T9T5 = 5 * Mg
    AA9 = 0.5 * Mr
    AA8 = 1.25 * Mr
    A8P = 2.5 * Mr
    DTS = (tc - M) / 2

    if DTS == 0:
        P1P2 = 0.25 * Mr
    else:
        P1P2 = 0.5 * Mr

    if tc <= 1.25 * M:
        P1P6 = 2 * M
    else:
        P1P6 = 2 * M + DTS

    points = {
        "Ширина спины" : Shc,
        'Рост' : Rost,
        'Высота плеча' : h,
        'Ширина плеча' : A8P1,
        'Расстояние от 7 шейного позвонка до стены' : tc_M,
        'Мр' : Mr,
        'Мг' : Mg,
        'М' : M,
        'тc' : tc,
        'АТ' : AT,
        'Т9Т5' : T9T5,
        'АА9' : AA9,
        'АА8' : AA8,
        'А8П' : A8P,
        'ДТС' : DTS,
        'П1П2' : P1P2,
        'П1П6' : P1P6
    }
    
    for key, value in points.items():
        
        v = round(value, 2)
        print(f"{key} = {v}")


if __name__ == '__main__':
    start()
