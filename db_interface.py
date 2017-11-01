from sqlalchemy.orm import sessionmaker
import db
from db import ExpiringImage

class ImageList():
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
        self.session = self.Session(bind=db.engine)

    # Create
    def add_image(self, path, expiration):
        #TODO: add code to prevent adding of duplicates
        # Below code was preventing any adding of Images
        #if not self.session.query(ExpiringImage).filter(ExpiringImage.path == path):
        
        self.session.add(ExpiringImage(path=path,expiration=expiration))
    # Read
    def status(self):
        return f'Staged files: {self.session.new}'
    def get_images(self):
        return self.session.query(ExpiringImage).all()
    # Update
    def edit(self,image_id):
        pass
    # Delete
    def remove_image(self, image_id):
        pass

    def commit(self):
        self.sesion.commit()
