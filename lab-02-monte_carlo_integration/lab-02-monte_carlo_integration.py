import numpy as np
from numpy import random

lower_limit_of_integration = 0.0  # нижний предел интергрирования
upper_limit_of_integration = 4.0  # верхний предел интергрирования
number_of_iterations = [100, 1000, 10000, 10000, 100000]  # чило итераций
integral_calculation_results = {}  # результаты полученные при различном числе итераций
number_of_experiments = 5  # число экспериментов для каждого числа итераций


def calculate_integrand_function(value):  # вычисление подынтегральной функции
    return np.sin(value) / value


def monte_carlo_integration(integral_calculation_results_, number_of_iterations_, lower_limit_of_integration_,
                            upper_limit_of_integration_):
    for iter_number_counter in range(len(number_of_iterations_)):  # для каждого числа итераций проводим 5 экспериметов
        experiments_results = []  # результаты пяти экспериметов для данного числа итераций
        for experiment in range(number_of_experiments):
            integral_value = 0.0
            for counter in range(number_of_iterations_[iter_number_counter]):
                value = lower_limit_of_integration_ + (upper_limit_of_integration_ - lower_limit_of_integration_) \
                        * random.uniform()
                integral_value += calculate_integrand_function(value)
            experiments_results.append((upper_limit_of_integration_ - lower_limit_of_integration_) /
                                       float(number_of_iterations_[iter_number_counter]) * integral_value)

        integral_calculation_results_[number_of_iterations_[iter_number_counter]] = experiments_results
    print(integral_calculation_results_)


monte_carlo_integration(integral_calculation_results, number_of_iterations, lower_limit_of_integration,
                        upper_limit_of_integration)
