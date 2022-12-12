from glob import glob
from shutil import copyfile

import tqdm as tqdm

def copy():
    output = glob('datas/**', recursive=True)

    for i in tqdm.tqdm(output):
        if i.endswith(".jpg"):
            copyfile(i, f'./images/{i.split("/")[-1]}')