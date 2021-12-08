from numpy.random import random

n = 1000  # число реализаций
accrued_amount_S = 245000  # наращенная сумма

days_before_redemption_of_bill = [120, 80, 40]  # дни до погашения векселя
probabilities = [0.6, 0.2, 0.2]  # вероятности, с которыми может быть учтен в банке

original_amount_p_calculated_values = []  # реализации первоначальной суммы
section_start, section_end = 239800, 243000

list_of_discrete_variable_values_120_d = [0.06, 0.062, 0.064]  # ряд распределения
list_of_discrete_variable_probabilities_120_d = [0.7, 0.2, 0.1]  # соответствующие вероятности

list_of_discrete_variable_values_80_d = [0.065, 0.068, 0.07]  # ряд распределения
list_of_discrete_variable_probabilities_80_d = [0.6, 0.2, 0.2]  # соответствующие вероятности

discrete_variable_values_40_d = [0.075, 0.09]


def original_amount_p(accrued_amount_s_, number_of_days_t_, annual_bank_rate_d_):
    return accrued_amount_s_ * (1 - (number_of_days_t_ / 360.0 * annual_bank_rate_d_))


def calculate_e(original_amount_p_):  # вычисление матожидания
    return sum(original_amount_p_) / len(original_amount_p_)


def calculate_d(original_amount_p_):  # вычисление дисперсии
    return calculate_e([p ** 2 for p in original_amount_p_]) - calculate_e(original_amount_p_) ** 2


def calc_discrete_variable(discrete_variable_values_, probabilities_):
    help_vector_q = [0, probabilities_[0], probabilities_[0] + probabilities_[1], 1]  # вспомогательный вектор
    base_random_variable = random()
    if help_vector_q[0] <= base_random_variable < help_vector_q[1]:
        return discrete_variable_values_[0]
    elif help_vector_q[1] <= base_random_variable < help_vector_q[2]:
        return discrete_variable_values_[1]
    elif help_vector_q[2] <= base_random_variable <= help_vector_q[3]:
        return discrete_variable_values_[2]


def calc_continuous_variable(a, b):
    base_random_variable = random()  # получаем бсв с помощью встроенной функции
    return float(a + base_random_variable * (b - a))  #


for _ in range(0, n):

    number_of_days_t = calc_discrete_variable(days_before_redemption_of_bill, probabilities)

    if number_of_days_t == days_before_redemption_of_bill[0]:
        d = calc_discrete_variable(list_of_discrete_variable_values_120_d,
                                   list_of_discrete_variable_probabilities_120_d)
    elif number_of_days_t == days_before_redemption_of_bill[1]:
        d = calc_discrete_variable(list_of_discrete_variable_values_80_d, list_of_discrete_variable_probabilities_80_d)
    else:
        d = calc_continuous_variable(discrete_variable_values_40_d[0], discrete_variable_values_40_d[1])

    original_amount_p_calculated_values.append(original_amount_p(accrued_amount_S, number_of_days_t, d))

P_min = min(original_amount_p_calculated_values)
P_max = max(original_amount_p_calculated_values)

E_of_P = calculate_e(original_amount_p_calculated_values)
D_of_P = calculate_d(original_amount_p_calculated_values)

original_amount_p_in_section = [x for x in original_amount_p_calculated_values if section_start <= x <= section_end]
p_in_section = 100 * len(original_amount_p_in_section) / len(original_amount_p_calculated_values)

print('-------------------------------------- Min и Max P --------------------------------------')
print('Минимальное значение реализации P :', P_min)
print('Максимльное значение реализации P :', P_max)
print('-------------------------------------- E{P} и D{P} --------------------------------------')
print('Матожидание :', E_of_P)
print('Дисперсия :', D_of_P)
print('----------- Количество реализаций P попавших в  P { 200 000 <= P <= 220 000 } -----------')
print(p_in_section)
