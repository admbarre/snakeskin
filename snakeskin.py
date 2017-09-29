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
        response = input(f'{prompt} (y/n): ').lower()
        if response == 'y':
            return 1
        elif response == 'n':
            return 0
        else:
            print('Invalid input. Try again')

def load_images(imgs=None):
    #TODO: formats is a global NEEDS FIXING
    if imgs is None:    # Load the images in the current directory
        images = [Image.open(img) for img in os.listdir() if img.endswith(formats)]
    else:
        images = imgs
    
    # NOTE: Image object loses its original format and filename properties
    filenames = [img.filename for img in images]
    return images, filenames

def resize(images,ratio):
    return [img.resize(ratio, Image.ANTIALIAS) for img in images]

def save(images,filenames):
    for img, name in zip(images, filenames):
        img.save(name,subsampling=0,quality=100)
    return True

def quit():
    print('~Snakeskin has completed~')

def main():
    print('Date: {today}')

    images, filenames = load_images()

    print('Editing:')
    for name in filenames:
        print(f'+ {name}')

    if yesno('Resize files?'):
        resized_images = resize(images,g_ratio)
        if yesno('Save files?'):
            if save(resized_images, filenames):
                print('Files saved successfully.')
            if yesno("Rename folder with today's date?"):
                os.rename(Path.cwd(), Path.cwd() / '..' / today)    # Renames our folder with the current date
    quit()
main()

