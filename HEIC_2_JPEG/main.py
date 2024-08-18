from PIL import Image
from pillow_heif import register_heif_opener
import os

_currentPath = '.\\'
_filePath = 'Input'
_resultPath = 'Output'

register_heif_opener()

heic_lst = os.listdir(os.path.join(_currentPath, _filePath))
heic_lst = [os.path.join(_currentPath, _filePath, i) for i in heic_lst]


def heic_png_converter(file_path, result_path):
    print(f'{os.getcwd()}')
    print(f'Start - Path : {file_path} => {result_path}')
    print(f'first file => {heic_lst[0]}')
    for i in range(len(heic_lst)):
        img_nm = heic_lst[i].split('\\')[-1].split('.')[0]
        print(f'{img_nm} ({ round(i/len(heic_lst) * 100)} %)')
        save_path = os.path.join(_currentPath, result_path, img_nm + '.png')

        image = Image.open(heic_lst[i])
        image.convert('RGB').save(save_path)

    print(f'Save Complete 100%')


if __name__ == '__main__':
    heic_png_converter(_filePath, _resultPath)


