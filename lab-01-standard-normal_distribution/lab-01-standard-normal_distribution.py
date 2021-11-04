import math
import timeit
from numpy.random import random
import matplotlib.pyplot as plt
import pandas as pd

n = 1000
# коэффициенты сдвига
location_01_01, location_01_02, location_02_01, location_02_02, location_02_03 = 0, 1, 3, 6, 9
# коэффициенты масштаба
variance_01_01, variance_01_02, variance_02 = 1.2, 0.1, 9
scale_01_01, scale_01_02, scale_02 = math.sqrt(variance_01_01), math.sqrt(variance_01_02), \
                                     math.sqrt(variance_02)
# выборки реалтзаций
sample_using_the_central_limit_theorem_01, sample_using_the_central_limit_theorem_02, \
    sample_using_functional_transformations_01, sample_using_functional_transformations_02 = [], [], [], []
# выборки реалтзаций c «усеченным» нормальным распределением
sample_of_truncated_normal_distribution_01, sample_of_truncated_normal_distribution_02, \
    sample_of_truncated_normal_distribution_03 = [], [], []


#  алгоритм реализуемый методом суммирования, основанном на центральной предельной теореме
def sampling_using_the_central_limit_theorem(sample_of_realizations_, location, scale, n_):
    start_time = timeit.default_timer()
    for _ in range(n_):
        sample_of_realizations_.append(location + scale * (sum([random() for _ in range(12)]) - 6))
    end_time = timeit.default_timer()
    return end_time - start_time


# алгоритм основанный на методе функционального преобразования БСВ
def sampling_using_method_of_functional_transformations(sample_of_realizations_, location, scale, n_):
    start_time = timeit.default_timer()
    for counter in range(int(n_/2)):  # пологается, что n - чётное, но вычисление медианы в критерии серий поддерживает
        # и нечётное n
        a1 = random()
        a2 = random()
        n1 = math.sqrt(-2 * math.log(a1)) * math.sin(2 * math.pi * a2)
        n2 = math.sqrt(-2 * math.log(a1)) * math.cos(2 * math.pi * a2)
        sample_of_realizations_.append(location + n1 * scale)
        sample_of_realizations_.append(location + n2 * scale)
    end_time = timeit.default_timer()
    return end_time - start_time


# критерий серий
def series_criterion(sample_of_realizations_):
    sequence_of_signed_differences = []
    # находим медиану
    median = 0  # медиана выборки
    if len(sample_of_realizations_) % 2 != 0:
        median = sorted(sample_of_realizations_)[int(len(sample_of_realizations_) / 2)]
    else:
        median = (sorted(sample_of_realizations_)[int(len(sample_of_realizations_) / 2 - 1)] +
                  sorted(sample_of_realizations_)[int(len(sample_of_realizations_) / 2)]) / 2
    for counter in range(len(sample_of_realizations_)):
        if sample_of_realizations_[counter] != median:
            if sample_of_realizations_[counter] > median:
                sequence_of_signed_differences.append(1)
            else:
                sequence_of_signed_differences.append(0)
    series = []
    counter = 0
    len_of_series = 0
    while counter < len(sequence_of_signed_differences) - 1:
        len_of_series = 0
        counter_in_series = counter
        while sequence_of_signed_differences[counter] == sequence_of_signed_differences[counter_in_series]:
            len_of_series += 1
            counter_in_series += 1
            if counter_in_series == len(sequence_of_signed_differences) - 1:
                if sequence_of_signed_differences[counter_in_series - 1] == \
                        sequence_of_signed_differences[counter_in_series]:
                    len_of_series += 1
                else:
                    series.append(1)
                break
        series.append(len_of_series)
        counter = counter_in_series
    total_number_of_series = len(series)  # общие числом серий
    length_of_the_longest_series = max(series)  # протяжённостью самой длинной серии
    number_of_elements_of_signed_sequence = len(sequence_of_signed_differences)  # число элементов знаковой
    # последовательности
    if total_number_of_series > 0.5 * (number_of_elements_of_signed_sequence + 1
                                       - 1.96 * math.sqrt(number_of_elements_of_signed_sequence - 1)) or \
            length_of_the_longest_series < 3.3 * math.log10(number_of_elements_of_signed_sequence + 1):
        print("Test passed !")


# получить последовательность реализаций CB ξ c «усеченным» нормальным распределением
def create_truncated_normal_distribution(sample_of_realizations_):
    return [x for x in sample_of_realizations_ if x > 0]


# первая часть задания - сравнение точности и быстродействия
#  алгоритм реализуемый методом суммирования, основанном на центральной предельной теореме
time_using_the_central_limit_theorem_01 = sampling_using_the_central_limit_theorem(
    sample_using_the_central_limit_theorem_01, location_01_01, scale_01_01, n)

time_using_the_central_limit_theorem_02 = sampling_using_the_central_limit_theorem(
    sample_using_the_central_limit_theorem_02, location_01_02, scale_01_02, n)

# алгоритм основанный на методе функционального преобразования БСВ
time_using_method_of_functional_transformations_01 = sampling_using_method_of_functional_transformations(
    sample_using_functional_transformations_01, location_01_01, scale_01_01, n)

time_using_method_of_functional_transformations_02 = sampling_using_method_of_functional_transformations(
    sample_using_functional_transformations_02, location_01_02, scale_01_02, n)

# сравнение быстродействия
print('-------------------------------------- Compare Time --------------------------------------')
print('N(', location_01_01, ', ', variance_01_01, ') - using the central limit theorem - time : ',
      time_using_the_central_limit_theorem_01, sep='')
print('N(', location_01_02, ', ', variance_01_02, ') - using the central limit theorem - time : ',
      time_using_the_central_limit_theorem_02, sep='')
print('------------------------------------------------------------------------------------------')
print('N(', location_01_01, ', ', variance_01_01,
      ') - using the method of functional transformations - time : ',
      time_using_method_of_functional_transformations_01, sep='')
print('N(', location_01_02, ', ', variance_01_02,
      ') - using the method of functional transformations - time : ',
      time_using_method_of_functional_transformations_02, sep='')
print('------------------------------------------------------------------------------------------')
pd.DataFrame({'using the central limit theorem N(0, 1.2) ': sample_using_the_central_limit_theorem_01}).plot(
    kind='hist', bins=100, alpha=0.4)
pd.DataFrame({'using the central limit theorem N(1, 0.1) ': sample_using_the_central_limit_theorem_02}).plot(
    kind='hist', bins=100, alpha=0.4)
pd.DataFrame(
    {'using the method of functional transformations N(0, 1.2) ': sample_using_functional_transformations_01}).plot(
    kind='hist', bins=100, alpha=0.4)
pd.DataFrame(
    {'using the method of functional transformations N(1, 0.1) ': sample_using_functional_transformations_02}).plot(
    kind='hist', bins=100, alpha=0.4)
plt.show()

#  проверка точности моделирования с помощью критерия серий
print("Test 1 - the central limit theorem - N(0, 1.2)")

series_criterion(sample_using_the_central_limit_theorem_01)
print("Test 2 - the central limit theorem - N(1, 0.1)")
series_criterion(sample_using_the_central_limit_theorem_02)
print("Test 3 - the method of functional transformations - N(0, 1.2)")
series_criterion(sample_using_functional_transformations_01)
print("Test 4 - the method of functional transformations - N(1, 0.1)")
series_criterion(sample_using_functional_transformations_02)

# так как в предыдущем задании лучшие результаты были при использовании алгоритма основанного на методе
# функционального преобразования БСВ, будем использовать его для генерации выборок во втором задании
print('----------------------------- "Truncated" Normal Distribution ----------------------------')

sampling_using_method_of_functional_transformations(
    sample_of_truncated_normal_distribution_01, location_02_01, scale_02, n)
sample_of_truncated_normal_distribution_01 = \
    create_truncated_normal_distribution(sample_of_truncated_normal_distribution_01)
print('N(', location_02_01, ', ', variance_02, ') - доля пропущенных реализаций : ',
      1 - len(sample_of_truncated_normal_distribution_01) / n, sep='')

sampling_using_method_of_functional_transformations(
    sample_of_truncated_normal_distribution_02, location_02_02, scale_02, n)
sample_of_truncated_normal_distribution_02 = \
    create_truncated_normal_distribution(sample_of_truncated_normal_distribution_02)
print('N(', location_02_02, ', ', variance_02, ') - доля пропущенных реализаций : ',
      1 - len(sample_of_truncated_normal_distribution_02) / n, sep='')

sampling_using_method_of_functional_transformations(
    sample_of_truncated_normal_distribution_03, location_02_03, scale_02, n)
sample_of_truncated_normal_distribution_03 = \
    create_truncated_normal_distribution(sample_of_truncated_normal_distribution_03)
print('N(', location_02_03, ', ', variance_02, ') - доля пропущенных реализаций : ',
      1 - len(sample_of_truncated_normal_distribution_03) / n, sep='')
