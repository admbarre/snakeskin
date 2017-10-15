from PIL import Image

class ImageList():
    def __init__(self, formats = ('.jpg', '.png') ):
        self._images = []
        self._formats = formats
    
    @property
    def images(self):
        return self._images
    @property
    def formats(self):
        return self._formats

    def add_image(self,path,date):
        if path not in [img.path for img in self._images]:
            self._images.append(ExpiringImage(path,date))
    def resize_all(self,ratio=(1920,1080)):
        for img in self._images:
            img.resize(ratio)
    def save_all(self):
        for img in self._images:
            img.save()
    def __iter__(self):
        return iter(self._images)

class ExpiringImage():
    def __init__(self, path, date):
        self._path = path
        self._image = Image.open(self.path)
        self._expiration = date

    #TODO: Better way to do this...?
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f'Path: {self._path}, Expiration: {self._expiration}, Size: {self._image.size}'

    @property
    def path(self):
        return self._path
    @property
    def expiration(self):
        return self._expiration
    
    @expiration.setter
    def expiration(self, date):
        self._expiration = date

    @path.setter
    def path(self, path):
        self._path = path
        self._image = Image.open(self._path)

    def resize(self,ratio):
        # Resize is not done in place
        self._image = self._image.resize(ratio, Image.ANTIALIAS)
    def save(self):
        self._image.save(self._path,subsampling=0,quality=100)
