#!/Users/Adrian/.virtualenvs/slides/bin/python
from PIL import Image
import sys, os, datetime, zipfile
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit("Program usage: slides.py [directory]")
target = Path(sys.argv[1])    # The directory with our images we want scaled
os.chdir(target)    # Move into our image directory

today = datetime.date.today().strftime('%m-%d-%y')  # Today's date in our preferred format
ratio = (1920,1080) # Our desired image size
formats = ('.jpg', '.png')  # Our accepted image formats

'''
dest = Path.cwd() / today # Folder that will hold our resized images
Path.mkdir(dest, exist_ok=True) # Create the folder if it doesn't already exist
'''

images = [Image.open(img) for img in os.listdir() if img.endswith(formats)]   # Opens all our images

# NOTE: Image object loses its original format and filename properties
filenames = [img.filename for img in images]
resized_images = [img.resize(ratio) for img in images]
test = zip(resized_images,filenames)

counter = 0
for img in test:
    counter += 1
    img[0].save(img[1])  # Saves the image with a prepended number
os.rename(Path.cwd(), Path.cwd() / '..' / today)    # Renames our folder with the current date
