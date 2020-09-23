import os
from PIL import Image

def get_name(source):
    "Function for create outfile name"
    head = source.split('.')[0]
    return head + '.pdf'

def pdf_make(directory):
    d = {}
    files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    for i in range(1, len(files)):
        d[i] = Image.open(files[i])
        image = Image.open(files[0])
        fname = get_name(files[0])
    image.save(fname, save_all=True, append_images=d.values())

if __name__ == '__main__':
    pdf_make('.')
