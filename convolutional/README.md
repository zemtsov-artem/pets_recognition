# Convolutional

## [Введение](../README.md)

Вся проведенная работа содержится в Jupiter-ноутбуке [main.ipynb](main.ipynb). Файл включает в себя:

* Подготовку тестовых, тренировочных, валидационных данных
* Создание моделей
* Обучение моделей
* Визуализацию каждого шага
* Тестирование модели с использованием тестовых данных

## Теория

В наших моделях было использовано:

- Функция активации Relu на скрытых слоях: ![relu](https://latex.codecogs.com/gif.latex?relu%28x%29%20%3D%20%5Cmax%20%280%2C%20x%29)
- Функция активации SoftMax на выходном слое: ![softmax](https://latex.codecogs.com/gif.latex?softmax%28x%29%20%3D%20%5Cfrac%7Be%5E%7Bx%7D%7D%7B%5Csum_%7Bk%3D1%7D%5E%7BK%7De%5E%7Bx_%7Bk%7D%7D%7D)
- Слой BatchNormalization. Этот слой нормализует данные по батчу: сводит математическое ожидание к 0 и дисперсию к 1. [Wiki](https://en.wikipedia.org/wiki/Batch_normalization)
- Слой Dropout для случайного отключения n нейронов, при ***n=70%***
- GlobalAveragePooling2D для усреднения значения по каналам.
- Оптимизатор Adam, adaptive momentum. ***Used learning rate = 1e-2***
- Инициализация начальных весов с помощью Xavier.


## Конфигурации моделей

В данной работе были проведены эксперементы со следующими моделями

1. ***Сверточная модель с тремя скрытыми слоями***

[//]: # ![](models_img/size=2,lr=0.001,use_dropout=False,use_batchnorm=False,use_globalpool=False.png)

| Layer (type) | Output Shape   | Param #   |
|--------------|----------------|-----------|
| Conv2D       | (112, 112, 64) | 9472      |
| Relu         | (112, 112, 64) | 0         |
| MaxPooling2D | (56, 56, 64)   | 0         |
| Conv2D       | (56, 56, 128)  | 73856     |
| Relu         | (56, 56, 128)  | 0         |
| Conv2D       | (56, 56, 128)  | 147584    |
| Relu         | (56, 56, 128)  | 0         |
| MaxPooling2D | (28, 28, 128)  | 0         |
| Flatten      | (100352)       | 0         |
| Dense        | (256)          | 25690368  |
| Dense        | (37)           | 9509      |

Total params: 25,930,789

![Model Accuracy](models_img/model1Acc.png)

![Model Loss](models_img/model1Loss.png)

2. ***Сверточная модель с использованием Batch Normalization + Global Pooling***

[//]: # ![](models_img/size=3,lr=0.001,use_dropout=False,use_batchnorm=True,use_globalpool=True.png)

| Layer (type)           |Output Shape    | Param #   |
|------------------------|----------------|-----------| 
| Conv2D                 | (112, 112, 64) | 9472      |
| batch_normalization    | (112, 112, 64) | 256       |
| Relu                   | (112, 112, 64) | 0         |
| max_pooling            | (56, 56, 64)   | 0         |
| Conv2D                 | (56, 56, 128)  | 73856     |
| batch_normalization    | (56, 56, 128)  | 512       |
| Relu                   | (56, 56, 128)  | 0         |
| Conv2D                 | (56, 56, 128)  | 147584    |
| batch_normalization    | (56, 56, 128)  | 512       |
| Relu                   | (56, 56, 128)  | 0         |
| max_pooling            | (28, 28, 128)  | 0         |
| Conv2D                 | (28, 28, 256)  | 295168    |
| batch_normalization    | (28, 28, 256)  | 1024      |
| Relu                   | (28, 28, 256)  | 0         |
| Conv2D                 | (28, 28, 256)  | 590080    |
| batch_normalization    | (28, 28, 256)  | 1024      |
| Relu                   | (28, 28, 256)  | 0         |
| max_pooling            | (14, 14, 256)  | 0         |
| global_average_pooling | (256)          | 0         |
| Dense                  | (37)           | 9509      |

Total params: 1,128,997

![Model Accuracy](models_img/model2Acc.png)

![Model Loss](models_img/model2Loss.png)

Переобучение снизилось. Точность на тренировочной выборке возросла до 0,68. Сходится модель намного быстрее благодаря слоям батч нормализации. Попробуем добавить дропаут перед слоем классификации, чтобы еще снизить переобучение.

3. ***Сверточная модель с использованием Batch Normalization + Global Pooling + Dropout***

[//]: # ![](models_img/size=3,lr=0.001,use_dropout=True,use_batchnorm=True,use_globalpool=True.png)

| Layer (type)           | Output Shape   | Param #   |
|------------------------|----------------|-----------| 
| Conv2D                 | (112, 112, 64) | 9472      |
| batch_normalization    | (112, 112, 64) | 256       |
| Relu                   | (112, 112, 64) | 0         |
| max_pooling            | (56, 56, 64)   | 0         |
| Conv2D                 | (56, 56, 128)  | 73856     |
| batch_normalization    | (56, 56, 128)  | 512       |
| Relu                   | (56, 56, 128)  | 0         |
| Conv2D                 | (56, 56, 128)  | 147584    |
| batch_normalization    | (56, 56, 128)  | 512       |
| Relu                   | (56, 56, 128)  | 0         |
| max_pooling            | (28, 28, 128)  | 0         |
| Conv2D                 | (28, 28, 256)  | 295168    |
| batch_normalization    | (28, 28, 256)  | 1024      |
| Relu                   | (28, 28, 256)  | 0         |
| Conv2D                 | (28, 28, 256)  | 590080    |
| batch_normalization    | (28, 28, 256)  | 1024      |
| Relu                   | (28, 28, 256)  | 0         |
| max_pooling            | (14, 14, 256)  | 0         |
| global_average_pooling | (256)          | 0         |
| dropout                | (256)          | 0         |
| Dense                  | (37)           | 9509      |

Total params: 1,128,997

![Model Accuracy](models_img/model3Acc.png)

![Model Loss](models_img/model3Loss.png)

Большой процент дропаута сильно помог с переубучением! Сохраним на состояние модели для последующих тестов.

#### Попробуем применить аугментацию наших изображений
- случайный поворот на 10 градусов
- случайное зуммирование на 10%
- случайное изменение яркости в диапозоне [0.7, 1.3]
- случайное горизонтальное отображение

Это должно привести к более стабильным результатам. Используем предыдущую архитектуру сети, т.к. она дала самые лучшие результаты.

![Model Accuracy](models_img/model4Acc.png)

![Model Loss](models_img/model4Loss.png)

Как видно из графика сильно это не помогло. Предположение: уменьшить learning rate, возможно модель зависла на плато и сойдется еще чуть-чуть. Используем lr=0.0003, как советовал ***Andrej Karpathy*** в своем [твиттере](https://twitter.com/karpathy/status/801621764144971776) =D

![Model Accuracy](models_img/model5Acc.png)

![Model Loss](models_img/model5Loss.png)

***+12% точности*** на валидационной выборке! Неплохо. Остановимся на этом и сохраним модель.

## Тестирование моделей

Для тестирования использовались следующие модели:

- С использованием аугментации данных

| loss   | accuracy |
|:------:|:--------:|
| 1.0759 | 0.6678   |

- Без использования аугментации данных

| loss   | accuracy |
|:------:|:--------:|
| 1.4011 | 0.6031   |

### Пример

Запустим обе модели и попробуем определить породу для данного изображения 

![Birman](models_img/Birdman.png)

Expected category : Birman

| Category | without data aug | with data aug |
|:--------:|:----------------:|:-------------:|
|Birman    | 0.2598           | 0.6058        |
|Siamese   | 0.7225           | 0.3518        |
|Ragdoll   | 0.0143           | 0.0421        |
