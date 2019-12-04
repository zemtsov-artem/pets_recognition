# Deep Learning Course

## Постановка задачи

Цель настоящей работы состоит в том, чтобы получить базовые навыки работы с 
библиотекой глубокого обучения Keras на примере
полностью связанных нейронных сетей.

В рамках данной лабораторной работы будет решаться задача классификации пород кошечек/собачек

Пусть ![equation](https://latex.codecogs.com/gif.latex?X) — множество изображений, ![equation](https://latex.codecogs.com/gif.latex?Y) — множество наименований классов. 

Математическая формулировка:
Существует неизвестная целевая зависимость — отображение ![equation](https://latex.codecogs.com/gif.latex?y%5E*%20%3A%20X%20%5Crightarrow%20Y), значения которой известны только 
на объектах конечной обучающей выборки ![equation](https://latex.codecogs.com/gif.latex?X%5Em%20%3D%20%5C%7B%20%28x_1%2C%20y_1%29%2C%20...%2C%20%28x_m%2C%20y_m%29%20%5C%7D). 
Требуется построить алгоритм ![equation](https://latex.codecogs.com/gif.latex?a%20%3D%20X%20%5Crightarrow%20Y), способный классифицировать
произвольный объект ![equation](https://latex.codecogs.com/gif.latex?x%20%5Cin%20X).

## Описание множества данных


Используемые данные [The Oxford-IIIT Pet Dataset](https://www.kaggle.com/tanlikesmath/the-oxfordiiit-pet-dataset)

Обучающая выборка содержит 37 классов с различными породами кошечек и собачек. На каждый класс имеется около 200 изображений. На изображениях животные могут быть изображены в различных положениях, при разных условиях света.

|Elements|Category|
|------------------------------|-------|
|200   | 	Birman                     |
|200   | 	saint_bernard			   |                     
|191   | 	staffordshire_bull_terrier |                     
|200   | 	japanese_chin              |
|200   | 	american_pit_bull_terrier  |
|200   | 	newfoundland               |
|199   | 	scottish_terrier           |
|200   | 	chihuahua                  |
|200   | 	american_bulldog           |
|200   | 	Sphynx                     |
|200   | 	basset_hound               |
|200   | 	keeshond                   |
|200   | 	British_Shorthair          |
|200   | 	Persian                    |
|200   | 	great_pyrenees             |
|200   | 	english_setter             |
|200   | 	samoyed                    |
|200   | 	Siamese                    |
|200   | 	Maine_Coon                 |
|200   | 	pomeranian                 |
|200   | 	Bengal                     |
|200   | 	shiba_inu                  |
|200   | 	Bombay                     |
|200   | 	yorkshire_terrier          |
|200   | 	leonberger                 |
|200   | 	miniature_pinscher         |
|200   | 	pug                        |
|200   | 	Ragdoll                    |
|200   | 	Egyptian_Mau               |
|200   | 	german_shorthaired         |
|200   | 	Russian_Blue               |
|200   | 	Abyssinian                 |
|200   | 	boxer                      |
|200   | 	beagle                     |
|200   | 	havanese                   |
|200   | 	wheaten_terrier            |
|200   | 	english_cocker_spaniel	   |

## Метрики качества

В качестве метрики качества используем accuracy.

![equation](https://latex.codecogs.com/gif.latex?%5Ctextrm%7BAccuracy%7D%20%3D%20%5Cfrac%7B%5Ctextrm%7BNumber%20of%20correct%20predictions%7D%7D%7B%5Ctextrm%7BTotal%20number%20of%20predictions%7D%7D)

## Исходный формат хранения данных

Обучающая выборка состоит из изображений в формате RGB, название файлов содержит название породы животного.
Каждое изображение имеет разный размер.
Данные никак не группированы.

## Подготовка входных данных

Подготовка включает в себя подготовку csv файла с данными о названии класса и пути к изображению для каждого обучающего элемента.

Подготовка изображений включала в себя следующие действия: 
1. Приведение изображений к одному размеру (32x32)


Так как загрузка всех изображений выборки является затратной по памяти операцией,
для передачи входных данных в модели использовались генераторы, которые случайным образом достают
batch изображений. Размер используемого batch_size = 64.

