# Моделирование непрерывных случайных величин (НСВ)
## tasks
- Используя случайные выборки реализаций объема n = 1000
- сравнить по точности и быстродействию методы моделирования CB ξ ~ N 1 (μ, σ 2 ). 
  - Положить: μ 1 = 0, σ 2 = 1.2, ∶ μ 1 = 1, σ 2 = 0.1. 
- Получить последовательность реализаций CB ξ c «усеченным» нормальным распределением. 
- Оценить долю пропущенных реализаций CB η из n = 1000 смоделированных.
  - Положить: σ 2 = 9, μ = 3,6,9.
  - 
[`report`](https://github.com/vetasavitskaya/famcs-simulation-and-statistical-modeling-labs/blob/main/lab-01/%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B5%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%BD%D1%8B%D1%85_%D1%81%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D1%8B%D1%85_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD.pdf),
[`code`](https://github.com/vetasavitskaya/famcs-simulation-and-statistical-modeling-labs/blob/main/lab-01/lab-01-standard-normal_distribution.py)

```
mcg:
-------------------------------------- Compare Time --------------------------------------
N(0, 1.2) - using the central limit theorem - time : 0.006191792999743484
N(1, 0.1) - using the central limit theorem - time : 0.006029343000136578
------------------------------------------------------------------------------------------
N(0, 1.2) - using the method of functional transformations - time : 0.0013007120001020667
N(1, 0.1) - using the method of functional transformations - time : 0.0012515439998423972
------------------------------------------------------------------------------------------
Test 1 - the central limit theorem - N(0, 1.2)
Test passed !
Test 2 - the central limit theorem - N(1, 0.1)
Test passed !
Test 3 - the method of functional transformations - N(0, 1.2)
Test 4 - the method of functional transformations - N(1, 0.1)
Test passed !
----------------------------- "Truncated" Normal Distribution ----------------------------
N(3, 9) - доля пропущенных реализаций : 0.14600000000000002
N(6, 9) - доля пропущенных реализаций : 0.020000000000000018
N(9, 9) - доля пропущенных реализаций : 0.0010000000000000009
```
