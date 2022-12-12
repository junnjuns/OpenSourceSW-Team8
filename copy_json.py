from glob import glob
from shutil import copyfile

import tqdm as tqdm

def copy():
    output = glob('datas/**', recursive=True)
    count = 0
    for i in tqdm.tqdm(range(len(output))):
        if output[i].endswith(".json"):
            copyfile(output[i], f'./ano/{count}.json')
            count += 1