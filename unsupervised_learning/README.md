# Unsupervised-learning

## [Введение](../README.md)

Вся проведенная работа содержится в Jupiter-ноутбуке [main.ipynb](main.ipynb). Файл включает в себя:

* Подготовку тестовых, тренировочных, валидационных данных
* Создание моделей
* Обучение моделей
* Визуализацию каждого шага
* Тестирование модели с использованием тестовых данных

## Теория

В качестве алгоритма без учителя для инициализации начальных весов сети - выберем автокодировщик.
Автокодировщики применяют для предварительного обучения глубокой сети без учителя.
К каждому новому необученному слою на время обучения подключается дополнительный выходной слой, дополняющий сеть до архитектуры автокодировщика, после чего на вход сети подается набор данных для обучения. 

Веса необученного слоя и дополнительного слоя автокодировщика обучаются при помощи метода обратного распространения ошибки. 
Затем слой автокодировщика отключается и создается новый, соответствующий следующему необученному слою сети. 
На вход сети снова подается тот же набор данных, обученные первые слои сети остаются без изменений и работают в качестве входных для очередного обучаемого автокодировщика слоя. 

Так обучение продолжается для всех слоев сети за исключением последних. Последние слои сети обычно обучаются без использования автокодировщика при помощи того же метода обратного распространения ошибки и на маркированных данных (обучение с учителем).

Мы взяли архитектуру модели из второй лабораторной работы , так как она показала наилучший результат.

Конфигурация модели:

|  Layer (type)           |Output Shape    | Param #   |
|------------------------|----------------|-----------| 
|  Conv2D                 | (112, 112, 64) | 9472      |
|  batch_normalization    | (112, 112, 64) | 256       |
|  Relu                   | (112, 112, 64) | 0         |
|  max_pooling            | (56, 56, 64)   | 0         |
|  Conv2D                 | (56, 56, 128)  | 73856     |
|  batch_normalization    | (56, 56, 128)  | 512       |
|  Relu                   | (56, 56, 128)  | 0         |
|  Conv2D                 | (56, 56, 128)  | 147584    |
|  batch_normalization    | (56, 56, 128)  | 512       |
|  Relu                   | (56, 56, 128)  | 0         |
|  max_pooling            | (28, 28, 128)  | 0         |
|  Conv2D                 | (28, 28, 256)  | 295168    |
|  batch_normalization    | (28, 28, 256)  | 1024      |
|  Relu                   | (28, 28, 256)  | 0         |
|  Conv2D                 | (28, 28, 256)  | 590080    |
|  batch_normalization    | (28, 28, 256)  | 1024      |
|  Relu                   | (28, 28, 256)  | 0         |
|  max_pooling            | (14, 14, 256)  | 0         |
|  global_average_pooling | (256)          | 0         |
|  Dense                  | (37)           | 9509      |

Результаты работы модели:

|  loss   | accuracy |
|:------:|:--------:|
|  1.0759 | 0.6678   |

В нашей модели было использовано:

- GlobalAveragePooling2D, который берет среднее по всем каналам. Это позволяет сильно уменьшить количество обучаемых параметров на классификационном Dense слое, что в свою очередь помогает бороться с переобучением

- Слой Dropout, который случайным образом отключает часть нейронов. Это позволяет предотвратить переобучение, путем тренировки некого ансамбля сетей ([arxiv](https://arxiv.org/abs/1207.0580))

- Функция активации SoftMax на выходном полносвязном слое: 

![softmax](https://latex.codecogs.com/gif.latex?softmax%28x%29%20%3D%20%5Cfrac%7Be%5E%7Bx%7D%7D%7B%5Csum_%7Bk%3D1%7D%5E%7BK%7De%5E%7Bx_%7Bk%7D%7D%7D)

- Оптимизатор Adam - adaptive momentum ([arxiv](https://arxiv.org/abs/1412.6980v9)).  ***Learning rate=1e-2*** , установлен по умолчанию в выбранной библиотеке

![m](https://latex.codecogs.com/gif.latex?m_%7Bt%7D%20%3D%20%5Cbeta_1%20m_%7Bt-1%7D%20&plus;%20%281%20-%20%5Cbeta_1%29%20%5Cnabla%20f%28x_t%29)

![v](https://latex.codecogs.com/gif.latex?v_%7Bt%7D%20%3D%20%5Cbeta_2%20v_%7Bt-1%7D%20&plus;%20%281%20-%20%5Cbeta_2%29%20%5Cnabla%20%28f%28x_t%29%29%5E2)

![hat_m](https://latex.codecogs.com/gif.latex?%5Cwidehat%7Bm_t%7D%20%3D%20%5Cfrac%7Bm_t%7D%7B1%20-%20%5Cbeta_%7B1%7D%5Et%7D)

![hat_v](https://latex.codecogs.com/gif.latex?%5Cwidehat%7Bv_t%7D%20%3D%20%5Cfrac%7Bv_t%7D%7B1%20-%20%5Cbeta_%7B2%7D%5Et%7D)

![x](https://latex.codecogs.com/gif.latex?x_%7Bt&plus;1%7D%20%3D%20x_t%20-%20%5Calpha%20%5Cfrac%7B%5Cwidehat%7Bm_t%7D%7D%7B%5Csqrt%7B%5Cwidehat%7Bv_t%7D%7D%20&plus;%20%5Cvarepsilon%7D)

- Функция ошибки ***Categorical Cross-Entropy*** для классификации на несколько классов:

 ![crossentropy](https://latex.codecogs.com/gif.latex?categorical%5C_crossentropy%20%3D%20-%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bi%3D1%7D%5E%7BN%7D%20y_i%20%5Ccdot%20%5Clog%28%5Chat%7By_i%7D%29)

#### Аугментация для наших изображений

В данной работе была применена аугметация данных для предотвращения переобучения и стабильности модели к небольшим изменениям изображений.

- случайный поворот на 10 градусов
- случайное зуммирование на 10%
- случайное изменение яркости в диапозоне [0.7, 1.3]
- случайное горизонтальное отображение

### Автокодировщик
Для построения автокодировщика была добавлена часть декодера вместо классификатора.

Конфигурация автодекодера:

|  Layer (type)           |Output Shape    | Param #   |
|------------------------|----------------|-----------| 
| conv2d                 | (14, 14, 128)       | 295040    |
| batch_normalization                 | (14, 14, 128)       | 512       |
| re_lu                 | (14, 14, 128)       | 0         |
| conv2d                 | (14, 14, 128)       | 147584    |
| batch_normalization                 | (14, 14, 128)       | 512       |
| re_lu                 | (14, 14, 128)       | 0         |
| conv2d_transpose                | (28, 28, 128)       | 147584    |
| batch_normalization                 | (28, 28, 128)       | 512       |
| re_lu                 | (28, 28, 128)       | 0         |
| conv2d                 | (28, 28, 64)        | 73792     |
| batch_normalization                 | (28, 28, 64)        | 256       |
| re_lu                 | (28, 28, 64)        | 0         |
| conv2d                 | (28, 28, 64)        | 36928     |
| batch_normalization                 | (28, 28, 64)        | 256       |
| re_lu                 | (28, 28, 64)        | 0         |
| conv2d_transpose                 | (56, 56, 64)        | 36928     |
| batch_normalization                 | (56, 56, 64)        | 256       |
| re_lu                 | (56, 56, 64)        | 0         |
| conv2d_transpose                 | (112, 112, 32)      | 18464     |
| batch_normalization                 | (112, 112, 32)      | 128       |
| re_lu                 | (112, 112, 32)      | 0         |
| dropout_                 | (112, 112, 32)      | 0         |
| conv2d_transpose | ( 224, 224, 3)    |   867       |

Total params: 1,879,107

Для обучения автокодировщика было использовано 1/3 тренировочных и валидационых данных.

 - Слой ***conv2d_transpose*** был использован для увеличения размера изображения.

 - Функция ошибки ***MSE*** для обучения автокодировщика:

 ![mse](https://latex.codecogs.com/gif.latex?MSE%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bi%3D1%7D%5E%7BN%7D%20%28%5Chat%7By_i%7D%20-%20y_i%29%5E2)


### Результаты обучения автокодировщика.

Ошибка на тестовых данных составила = 0.008817542484030128

![](../resources/unsupervised_learning_1.png)

Как видно автокодировщик попытался выделить на изображении главные части, которые могут повлиять на дальнейшую классификацию.

Уберем из модели часть декодера и вставим наш классификатор из предыдущей работы.
Обучим получившуюся модель с проинициализированными весами. При этом будем применять аугментацию данных.

Полученные результаты:

![](../resources/unsupervised_learning_2.png)
![](../resources/unsupervised_learning_3.png)

Ошибка и точность модели никак не изменились. Но изменилось колучиство эпох для достижения таких же результатов. 34 эпохи против 66 в предыдущей работе.
Попробуем так же уменьшить learnnig rate в надежде на большую сходимость к минимуму.


![](../resources/unsupervised_learning_4.png)
![](../resources/unsupervised_learning_5.png)

Опять же совершенно аналогичные результаты, за исключением количества эпох.
Получились неплохие результаты с учетом того, что время на обучение модели потребовалось в 2 раза меньше. К увеличению точности, к сожалению, это не привело.

## Тестирование

|  Loss   | Accuracy |
|:------:|:--------:|
|  1.2430409238584017 | 0.6544850508239974   |

### Пример

Запустим модель и попробуем определить породу для данного изображения 

![Bombay](../resources/Bombay_test.png)

Expected category : Bombay

| Category | Result |
|:--------:|:----------------:|
| Bombay    | 0.99999905 |
| scottish_terrier   |9.241556e-07       |
| Siamese   | 1.5148202e-09 |
