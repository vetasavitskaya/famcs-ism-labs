
# Моделирование наращенных сумм и современных величин платежа
## tasks

Вексель на сумму 𝑆 = 245000 может быть учтен в банке за 120 дней до его погашения с вероятностью 0.6, но тогда банковская учетная ставка 𝑑 будет описываться дискретной случайной величиной
![](https://github.com/vetasavitskaya/famcs-simulation-and-statistical-modeling-labs/blob/main/lab-03-accrued-amounts/image_01.png)
за 80 дней до его погашения с вероятностью 0,2 и в этом случае за 40 дней до его погашения с вероятностью 0,2 и в этом случае 𝑑 ∈ 𝑅 (7.5 %; 9 %).
![](https://github.com/vetasavitskaya/famcs-simulation-and-statistical-modeling-labs/blob/main/lab-03-accrued-amounts/image_02.png)

[`report`](https://github.com/vetasavitskaya/famcs-simulation-and-statistical-modeling-labs/blob/main/lab-03-accrued-amounts/%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%BD%D1%8B%D1%85_%D1%81%D1%83%D0%BC%D0%BC.pdf),
[`code`](https://github.com/vetasavitskaya/famcs-simulation-and-statistical-modeling-labs/blob/main/lab-03-accrued-amounts/lab-03-accrued-amounts.py)

## results
```
-------------------------------------- Min и Max P --------------------------------------
Минимальное значение реализации P : 239773.33333333334
Максимльное значение реализации P : 242956.92861292468
-------------------------------------- E{P} и D{P} --------------------------------------
Матожидание : 240822.97324314874
Дисперсия : 1216169.4954986572
----------- Количество реализаций P попавших в  P { 200 000 <= P <= 220 000 } -----------
0.0
```
