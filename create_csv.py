import os
import re
from pandas import DataFrame
from PIL import Image
from config import size_barrier, categories_num

def dir_list(path):
    return os.listdir(path)


def dir_pathes_list(path):
    return [path + s for s in dir_list(path)]

def parse_categories(name_list):
    return [re.split(r'_\d*\.jpg', name)[0] for name in name_list]

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

def filter_pathes_with(pathes,barrier_value,verbose=True):
    filtered_pathes = []
    minSize = (float('inf'),float('inf'))
    maxSize = (0,0)
    height_sum = 0
    weight_sum = 0
    good_quality_images_counter=0
    for path in pathes:
        if re.search(r'.jpg', path):
            im = Image.open(path)
            width, height = im.size
            weight_sum+=width
            height_sum+=height
            if (height>=barrier_value and width>=barrier_value):
                good_quality_images_counter+=1
                filtered_pathes.append(path)
            if (width * height) > (maxSize[0] * maxSize[1]):
                maxSize = (width,height)
            if (width * height) < (minSize[0] * minSize[1]):
                minSize = (width,height)

    if (verbose):
        print('average height: %s' % (height_sum / len(pathes)) )
        print('average weight: %s' % (weight_sum / len(pathes)) )
        print('minSize : %s x %s' % (minSize[0],minSize[1]) )
        print('maxSize : %s x %s' % (maxSize[0],maxSize[1]) )
        print('unused elements counter:%s' % (len(pathes) - good_quality_images_counter))
        print('images with size more than %sx%s counter: %s' % 
            (barrier_value,barrier_value,good_quality_images_counter))
    return filtered_pathes

def create_csv(images_path):
    image_names = dir_list(images_path)
    pathes = dir_pathes_list(images_path)
    filtered_pathes = filter_pathes_with(pathes,size_barrier)
    categories = parse_categories([remove_prefix(s,images_path) for s in filtered_pathes])
    
    data = {'Category': categories, 'Path': filtered_pathes}

    df = DataFrame(data, columns=['Category', 'Path'])

    validation_data = DataFrame(columns=['Category', 'Path'])
    test_data = DataFrame(columns=['Category', 'Path'])
    train_data = DataFrame(columns=['Category', 'Path'])

    unique_categories = df['Category'].unique()
    for unique_cat in unique_categories:
        split_num = df.shape[0] // categories_num // 10  # 10% of each category from dataset

        validation_data = test_data.append(df[df['Category'] == unique_cat][:split_num], ignore_index=True)
        test_data = test_data.append(df[df['Category'] == unique_cat][split_num:split_num*2], ignore_index=True)
        train_data = train_data.append(df[df['Category'] == unique_cat][split_num*2:], ignore_index=True)

    test_data.to_csv(f'./test_pets.csv')
    validation_data.to_csv(f'./val_pets.csv')
    train_data.to_csv(f'./train_pets.csv')



if __name__ == '__main__':
    create_csv('./images/')
