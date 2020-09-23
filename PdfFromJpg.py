import os
from PIL import Image

def get_name(source):
    head = source.split('.')[0]
    return head + '.pdf'

def pdf_make(directory):
    d = {}
    files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    for i in range(len(files)):
        d[i] = Image.open(files[i])
        fname = get_name(files[0])
        image = Image.open(files[0])
    image.save(fname, save_all=True, append_images=d.values())

if __name__ == '__main__':
    pdf_make('.')
