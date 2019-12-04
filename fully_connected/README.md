# FCNN

## [Введение](../README.md)

Вся проведенная работа содержится в Jupiter-ноутбуке [main.ipynb](./main.ipynb).
Файл включает в себя:
* Подготовку тестовых, тренировочных, валидационных данных.
* Создание моделей
* Обучение моделей
* Визуализацию каждого шага
* Тестирование модели с использованием тестовых данных

Мы использовали Data Augmentation:

1. Random rotation
2. Horizontal flip
3. Width/height shifts
4. Zoom range.

Для остановки обучения в случаях не уменьшения валидационной ошибки мы использовали EarlyStoping c patience=4.

## Конфигурации моделей

В данной работе были проведены эксперементы со следующими моделями

1. Полносвязная модель с одним скрытым слоем

Базовая модель с 128 нейронами на скрытом слое:

 | Layer (type)     |              Output Shape         |       Param     | 
|--------------------------|----|-------|
| flatten_3 (Flatten)     |     (None, 3072)        |      0         |
|dense_5 (Dense) |              (None, 128)              | 393344 |
|activation_3 (Activation)  |   (None, 128)  |              0         |
|dense_6 (Dense)      |        (None, 37)       |         4773      |
|Total params:  398,117|
|Trainable params: 398,117|
|Non-trainable params: 0|


Были произведены эксперименты с разным количеством нейронов и разными функциями активации на скрытом слое.

Environment: 256 units, tanh activation
  - epochs: 20  - test loss: 3.29  - val loss: 3.2853  - test acc: 0.1017  - val acc: 0.1111
Environment: 256 units, relu activation
  - epochs: 20  - test loss: 3.1947  - val loss: 3.2156  - test acc: 0.1287  - val acc: 0.1236
Environment: 256 units, selu activation
  - epochs: 9  - test loss: 3.4162  - val loss: 3.388  - test acc: 0.0889  - val acc: 0.1017
Environment: 1024 units, tanh activation
  - epochs: 17  - test loss: 4.1531  - val loss: 4.14  - test acc: 0.0794  - val acc: 0.1064
Environment: 1024 units, relu activation
  - epochs: 17  - test loss: 3.1786  - val loss: 3.2312  - test acc: 0.1247  - val acc: 0.1283
Environment: 1024 units, selu activation
  - epochs: 5  - test loss: 15.5103  - val loss: 15.6388  - test acc: 0.0275  - val acc: 0.0297

2. Полносвязная модель с двумя скрытыми слоями.


 | Layer (type)              |     Output Shape            |    Param    | 
|--------------------------|----|-------|
 | flatten_13 (Flatten)      |     (None, 3072)       |        0    |       
 | dense_25 (Dense)           |    (None, 128)             |    393344     | 
 | activation_13 (Activation)  |   (None, 128)        |         0          | 
 | dense_26 (Dense)            |   (None, 64)       |           8256       | 
 | activation_14 (Activation)   |  (None, 64)       |           0          | 
 | dense_27 (Dense)           |    (None, 37)       |           2405       | 
 | Total params: 404,005 | 
 | Trainable params: 404,005 | 
 | Non-trainable params: 0 | 

Были произведены эксперименты с разным количеством нейронов и разными функциями активации на скрытом слое.

Environment: [512, 256] units, tanh activation
  - epochs: 8 - test loss: 3.489 - val loss: 3.4698 - test acc: 0.0603 - val acc: 0.0736
Environment: [512, 256] units, relu activation
  - epochs: 12 - test loss: 3.1767 - val loss: 3.2335 - test acc: 0.1247 - val acc: 0.1142
Environment: [512, 256] units, selu activation
  - epochs: 18 - test loss: 3.2222 - val loss: 3.2489 - test acc: 0.128 - val acc: 0.1315
Environment: [1024, 512] units, tanh activation
  - epochs: 18 - test loss: 3.5232 - val loss: 3.4836 - test acc: 0.0576 - val acc: 0.0766
Environment: [1024, 512] units, relu activation
  - epochs: 11 - test loss: 3.205 - val loss: 3.2077 - test acc: 0.1162 - val acc: 0.1236
Environment: [1024, 512] units, selu activation
  - epochs: 17 - test loss: 3.3004 - val loss: 3.3445 - test acc: 0.1084 - val acc: 0.1174
CPU times: user 52min 34s, sys: 37.6 s, total: 53min 12s
Wall time: 46min 32s

Как можно увидеть из результатов, улучшений не произошло.

## Результаты тестирования с использованием тестовой выборки.

703 validated image filenames belonging to 37 classes.
test loss: 3.335000809431076, test accuracy: 0.08


## Заключение

Были проведены эксперементы с различными конфигурациями полносвязной сети. Использовали следующие динамичные метрики:

1. Кол-во нейронов.
2. Кол-ва скрытых слоев.
3. Функции активации.

Из результатов проведенных экспериментов можно увидеть , что полносвязная нейронная сеть достаточно плохо справляется с задачей классификации пород животных на изображениях.