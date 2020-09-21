from PIL import Image
import os

def get_name(source):
    head = source.split('.')[0]
    return head + '.pdf'

def pdf_make(dir):
    imagelist = []
    files = [f for f in os.listdir(dir) if f.endswith('.jpg')]
    for i in range(len(files)):
        image = Image.open(files[i])
        imagelist.append(image)
        fname = get_name(files[0])
        image = Image.open(files[0])
    image.save(fname, save_all=True, append_images=imagelist[1:])

if __name__ == '__main__':
    pdf_make('.')