# Sliding_Window
____
На временном интервале [a, b] задан дискретный набор значений функции x(t). 
Количество точек N = 20, расположение - равномерное. Методом “скользящего окна” спрогнозировано поведение 
функции x(t) на N точках последющего интервала (b, 2b - a]. 
Для решения использовалась однослойную НС с количеством нейронов p и линейной функцией активации. Исходное количество
нейронов (длина окна) p = 6. 
Обучение проводилось методом Видроу-Хоффа. 
Исследовалось влияние количества эпох M обучения и коэффициента обучения η на среднеквадратичную погрешность приближения.
____
В начале обучения задается конфигурация нейронной сети:
1. Целевая среднеквадратичная ошибка
2. Длина окна
3. Начало интервала исследования
4. Конец интервала исследования
5. Норма обучения
----
### Структура НС
![Image alt](https://github.com/typeperfest/Sliding_Window/raw/master/img/struct.jpeg)


Обучение проводится пока среднеквадратичная ошибка не перестанет превосходить целевую среднеквадратичную ошибку.
На изображениях красным цветом выделены точки, на которых проводится обучение НС, зеленым выделены точки на которых 
производится проверка работы НС. 

![Image alt](https://github.com/typeperfest/Sliding_Window/raw/master/img/23_eras.png "23 эпохи обучения")

Результат работы НС после 23 эпох обучения с целевой среднеквадратичной ошибкой 0.1

![Image alt](https://github.com/typeperfest/Sliding_Window/raw/master/img/262849_eras.png "262 849 эпох обучения")

Результат работы НС после 262849 эпох обучения с целевой среднеквадратичной ошибкой 0.001

![Image alt](https://github.com/typeperfest/Sliding_Window/raw/master/img/608746_eras.png "608 746 эпох обучения")

После 608746 эпох обучения НС "переобучилась", и некоторые из последних значений отклонились от нормы сильнее чем
при 262849 эпохах обучения. Целевая среднеквадратичная ошибка 0.0001.

В результате различных выборок целевой среднеквадратичной ошибки была сформирована зависимость числа эпох обучения от 
значения среднеквадратичной ошибки:
![alt text](https://github.com/typeperfest/Sliding_Window/raw/master/img/dependency.png "Зависимость эпох обучения от среднеквадратичной ошибки")

На изображении видно, что зависимость экспоненциальная.

