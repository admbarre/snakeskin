from PIL import Image
import sys, os, datetime, zipfile
from pathlib import Path

def yesno(prompt):
    while True:
        response = input('{} (y/n): '.format(prompt)).lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('Invalid input. Try again')
'''
if len(sys.argv) < 2:
    sys.exit("Program usage: snakeskin.py [directory]")
target = Path(sys.argv[1])    # The directory with our images we want scaled
os.chdir(target)    # Move into our image directory
'''

today = datetime.date.today().strftime('%m-%d-%y')  # Today's date in our preferred format
print('Date: {}'.format(today))

ratio = (1920,1080) # Our desired image size
formats = ('.jpg', '.png')  # Our accepted image formats

images = [Image.open(img) for img in os.listdir() if img.endswith(formats)]   # Opens all our images as long as the format is supported

# NOTE: Image object loses its original format and filename properties
filenames = [img.filename for img in images]
print('Editing:')
for name in filenames:
    print('+ {}'.format(name))
if yesno('Resize files?'):
    resized_images = [img.resize(ratio, Image.ANTIALIAS) for img in images]
    imgs_with_names= zip(resized_images,filenames)

    for img, name in imgs_with_names:
        img.save(name,subsampling=0,quality=100)

    if yesno("Rename folder with today's date?"):
        os.rename(Path.cwd(), Path.cwd() / '..' / today)    # Renames our folder with the current date
print('~Snakeskin has completed~')
