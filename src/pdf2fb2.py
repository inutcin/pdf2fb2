import os

start_page = 29;
end_page = 31;

settings = {}
settings.update({"convertDensity": 600})
settings.update({"start_page": 29})
settings.update({"end_page": 31})
settings.update({"input_file": "input.pdf"})
settings.update({"languages": "rus+eng"})


input_file = os.path.abspath("../volume/" + str(settings.get("input_file")));
jpeg_dir = os.path.abspath("../volume/jpg")
txt_dir = os.path.abspath("../volume/txt")
start_page = int(settings.get('start_page'))
end_page = int(settings.get('end_page'))

for dirname in [jpeg_dir, txt_dir]:
    if os.path.isdir(dirname)!=True:
        os.makedirs(dirname, 0o777)

for i in range(start_page, end_page + 1):
    # Convert PDF page to JPEG image
    current_jpg = jpeg_dir + "/" + str(i) + ".jpg"
    convertCommand = [] 
    convertCommand.append("convert")
    convertCommand.append("-verbose")
    convertCommand.append("-density " + str(settings.get("convertDensity")))
    convertCommand.append(input_file + "["+str(i)+"]")
    convertCommand.append(current_jpg);
    os.system(' '.join(convertCommand))

    #recognize single page and save it as text file
    current_txt = txt_dir + "/" + str(i) + ".txt"
    recognizeCommand = []
    recognizeCommand.append("tesseract")
    recognizeCommand.append(current_jpg)
    recognizeCommand.append(current_txt)
    recognizeCommand.append("-l "+ str(settings.get("languages")))
    os.system(' '.join(recognizeCommand))

    # remove temporary files
    for remfile in [current_jpg]:
        os.remove(current_jpg)
        

