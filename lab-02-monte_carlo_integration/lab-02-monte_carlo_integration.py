import numpy as np
from numpy import random
from mpmath import *

lower_limit = 0.0  # нижний предел интергрирования
upper_limit = 4.0  # верхний предел интергрирования

number_of_iterations = [100, 1000, 10000, 10000, 100000]  # чило итераций
number_of_experiments = 5  # число экспериментов для каждого числа итераций

monte_carlo_results = {}  # результаты полученные при различном числе итераций методом Монте-Карло
symmetric_function_results = {}  # результаты полученные при различном числе итераций симметризации
# подынтегральной функции


def integrand_function(value):  # вычисление подынтегральной функции
    return mpf(np.sin(value) / value)


# вычисление симметрической подынтегральной функции
def symmetric_integrand_function(value, lower_limit_, upper_limit_):
    symmetric_value = lower_limit_ + upper_limit_ - value
    return mpf(mpf(1/2) * (mpf(np.sin(value) / value) + mpf(np.sin(symmetric_value) / symmetric_value)))


# вычисление определенного интеграла простейшим методом Монте-Карло
def monte_carlo_and_symmetric_i_function_methods(results_m, results_s, iterations, experiments, lower_lim, upper_lim):
    for iter_number_counter in range(len(iterations)):  # для каждого числа итераций проводим 5 экспериметов
        monte_carlo_experiments_results = []  # результаты пяти экспериметов для метода Монте-Карло
        symmetric_function_experiments_results = []  # результаты пяти экспериметов для метода симметризации
        # подынтегральной функции
        for experiment in range(experiments):
            integral_monte_carlo = mpf(0.0)
            integral_symmetric_function = mpf(0.0)
            for counter in range(iterations[iter_number_counter]):
                value = lower_lim + (upper_lim - lower_lim) * random.uniform()  # произвольная случайная величина
                integral_monte_carlo += mpf(integrand_function(value))
                integral_symmetric_function += mpf(symmetric_integrand_function(value, lower_lim, upper_lim))
            monte_carlo_experiments_results.append((upper_lim - lower_lim) / mpf(float(iterations[iter_number_counter]))
                                                   * integral_monte_carlo)
            symmetric_function_experiments_results.append((upper_lim - lower_lim) /
                                                          mpf(float(iterations[iter_number_counter]))
                                                          * integral_symmetric_function)
        results_m[iterations[iter_number_counter]] = monte_carlo_experiments_results
        results_s[iterations[iter_number_counter]] = symmetric_function_experiments_results
    print(results_m)
    print(results_s)


monte_carlo_and_symmetric_i_function_methods(monte_carlo_results, symmetric_function_results, number_of_iterations,
                                             number_of_experiments, lower_limit, upper_limit)

