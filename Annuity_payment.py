# Рассчёт ануитетного платежа с выплатами на срок n лет и последующим продлением срока погашения займа
# на n лет и увеличении процентной ставки с момента конверсии до i%

def annuite_payment(p, t, s):
    coefficient = (p * (1 + p) ** t) / ((1 + p) ** t - 1)
    payments = round(coefficient * s, 2)
    return payments


credit_sum = float(input('Введите сумму кредита: '))
credit_time = int(input('На сколько лет выдан: '))
percent = int(input('Сколько процентов годовых: '))

percent /= 100
remainder_debt = credit_sum

for years in range(1, 4):
    print()
    annu_pay = annuite_payment(percent, credit_time, credit_sum)

    credit_body = (annu_pay - percent * remainder_debt)
    percent_sum = percent * remainder_debt

    print(f'Период: {years}')
    print(f'Остаток долга на начало периода: {remainder_debt}')
    print(f'Выплачено процентов: {percent_sum}')
    print(f'Выплачено тела кредита: {credit_body}')

    remainder_debt -= credit_body

print()
print(f'Остаток долга: {remainder_debt}\n')
print('', '=' * 30, '\n')

change_credit_time = int(input('На сколько лет продлевается договор? '))
change_percent = int(input('Увеличение ставки до: '))

change_percent /= 100
change_credit_time = credit_time + change_credit_time - 3
credit_sum = remainder_debt

for years in range(1, change_credit_time + 1):
    print()
    annu_pay = annuite_payment(change_percent, change_credit_time, credit_sum)

    credit_body = (annu_pay - change_percent * remainder_debt)
    percent_sum = change_percent * remainder_debt

    print(f'Период: {years}')
    print(f'Остаток долга на начало периода: {remainder_debt}')
    print(f'Выплачено процентов: {percent_sum}')
    print(f'Выплачено тела кредита: {credit_body}')

    remainder_debt -= credit_body

print()
print(f'Остаток долга: {remainder_debt}')
