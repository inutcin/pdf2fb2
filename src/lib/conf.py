import os

settings = {}
settings.update({"convertDensity": 600})
settings.update({"start_page": 31})
settings.update({"end_page":    32})
settings.update({"input_file": "input.pdf"})
settings.update({"languages": "rus+eng"})

input_file = os.path.abspath("../volume/" + str(settings.get("input_file")));

jpeg_dir = os.path.abspath("../volume/jpg")
txt_dir = os.path.abspath("../volume/txt")
box_dir = os.path.abspath("../volume/box")
