#!/Users/Adrian/.virtualenvs/slides/bin/python
from PIL import Image
import sys, os, datetime, zipfile
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit("Program usage: snakeskin.py [directory]")
target = Path(sys.argv[1])    # The directory with our images we want scaled
os.chdir(target)    # Move into our image directory

today = datetime.date.today().strftime('%m-%d-%y')  # Today's date in our preferred format
ratio = (1920,1080) # Our desired image size
formats = ('.jpg', '.png')  # Our accepted image formats

images = [Image.open(img) for img in os.listdir() if img.endswith(formats)]   # Opens all our images

# NOTE: Image object loses its original format and filename properties
filenames = [img.filename for img in images]
resized_images = [img.resize(ratio) for img in images]
imgs_with_names= zip(resized_images,filenames)

for img in imgs_with_names:
    img[0].save(img[1])  

os.rename(Path.cwd(), Path.cwd() / '..' / today)    # Renames our folder with the current date

def scale(directory, ratio):
    os.chdir(directory)
