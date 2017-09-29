from PIL import Image
import sys, os, datetime, zipfile
from pathlib import Path

'''
if len(sys.argv) < 2:
    sys.exit("Program usage: snakeskin.py [directory]")
target = Path(sys.argv[1])    # The directory with our images we want scaled
os.chdir(target)    # Move into our image directory
'''

# ==============
# Globals
# TODO: FIX THIS
# ==============
today = datetime.date.today().strftime('%m-%d-%y') 
g_ratio = (1920,1080) # Our desired image size
formats = ('.jpg', '.png')  # Our accepted image formats

def yesno(prompt):
    while True:
        response = input('{} (y/n): '.format(prompt)).lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('Invalid input. Try again')

def load_images(imgs=None):
    if imgs is None:    # Load the images in the current directory
        images = [Image.open(img) for img in os.listdir() if img.endswith(formats)]
    else:
        images = imgs
    return images

#TODO: accept ratio
def resize(images,ratio):
    return [img.resize(ratio, Image.ANTIALIAS) for img in images]
    
def main():
    print('Date: {}'.format(today))

    images = load_images()

    # NOTE: Image object loses its original format and filename properties
    filenames = [img.filename for img in images]
    print('Editing:')
    for name in filenames:
        print('+ {}'.format(name))

    if yesno('Resize files?'):
        resized_images = resize(images,g_ratio)
        imgs_with_names= zip(resized_images,filenames)

        '''
        for img in resized_images:
            print(f'{img.filename}')
        '''

        '''
        for img, name in imgs_with_names:
            img.save(name,subsampling=0,quality=100)
        '''
        if yesno("Rename folder with today's date?"):
            os.rename(Path.cwd(), Path.cwd() / '..' / today)    # Renames our folder with the current date
    print('~Snakeskin has completed~')

main()
