"""#!/usr/bin/python3"""
"""magic method"""
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
