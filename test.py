import snakeskin as skin
import sys, os, datetime
from pathlib import Path

g_today = datetime.date.today().strftime('%m-%d-%y') 
def yesno(prompt):
    while True:
        response = input(f'{prompt} (y/n): ').lower()
        if response == 'y':
            return 1
        elif response == 'n':
            return 0
        else:
            print('Invalid input. Try again')
def main():
    images = skin.ImageList()
    print(images.images)

    print(f'Date: {g_today}')
    files = [f for f in os.listdir() if f.endswith(images.formats)]
    print('Images in current directory: ')
    for f in files:
        print(f'- {f}')
    if yesno('Add these files?'):
        for f in files:
            images.add_image(f,None)
        print('Images added:')
        for img in images:
            print(f'+ {img}')
        if yesno('Resize these images?'):
            images.resize_all()
            for img in images:
                print(f'~ {img}')
            if yesno('Save these images?'):
                images.save_all()




if __name__ == '__main__':
    main()

