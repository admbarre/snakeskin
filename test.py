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
    print(f'Date: {g_today}')
    files = os.listdir()
    print('Editing: ')
    for f in files:
        print(f'+ {f}')

    if yesno('Resize files?'):
        resized_images = skin.resize(images,g_ratio)
        if yesno('Save files?'):
            if skin.save(resized_images, filenames):
                print('Files saved successfully.')

if __name__ == '__main__':
    main()

