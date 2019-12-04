import os
import re
from pandas import DataFrame

import config


def dir_list(path):
    return os.listdir(path)


def dir_pathes_list(path):
    return [path + s for s in dir_list(path)]


def parse_categories(name_list):
    return [re.split(r'_\d*\.jpg', name)[0] for name in name_list]


def create_csv(images_path):
    image_names = dir_list(images_path)
    categories = parse_categories(image_names)
    pathes = dir_pathes_list(images_path)

    data = {'Category': categories, 'Path': pathes}
    df = DataFrame(data, columns=['Category', 'Path'])

    validation_data = DataFrame(columns=['Category', 'Path'])
    test_data = DataFrame(columns=['Category', 'Path'])
    train_data = DataFrame(columns=['Category', 'Path'])

    unique_categories = df['Category'].unique()
    for unique_cat in unique_categories:
        split_num = df.shape[0] // config.categories_num // 10  # 10% of each category from dataset

        validation_data = test_data.append(df[df['Category'] == unique_cat][:split_num], ignore_index=True)
        test_data = test_data.append(df[df['Category'] == unique_cat][split_num:split_num*2], ignore_index=True)
        train_data = train_data.append(df[df['Category'] == unique_cat][split_num*2:], ignore_index=True)

    test_data.to_csv(f'./test_pets.csv')
    validation_data.to_csv(f'./val_pets.csv')
    train_data.to_csv(f'./train_pets.csv')


if __name__ == '__main__':
    create_csv('../images/')
