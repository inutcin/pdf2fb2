import os
import conf

# Convert PDF page to JPEG image
def pdf2jpg(page):
    current_jpg = conf.jpeg_dir + "/" + str(page) + ".jpg"
    convertCommand = [] 
    convertCommand.append("convert")
    # convertCommand.append("-verbose")
    convertCommand.append("-density " + str(conf.settings.get("convertDensity")))
    convertCommand.append(conf.input_file + "["+str(page)+"]")
    convertCommand.append(current_jpg);
    os.system(' '.join(convertCommand))
    return current_jpg

#recognize single page and save it as text file
def jpg2txt(current_jpg, page):
    current_txt = conf.txt_dir + "/" + str(page)
    recognizeCommand = []
    recognizeCommand.append("tesseract")
    recognizeCommand.append(current_jpg)
    recognizeCommand.append(current_txt)
    recognizeCommand.append("--dpi " + str(conf.settings.get("convertDensity")))
    recognizeCommand.append("--oem 1")
    recognizeCommand.append(" -l "+ str(conf.settings.get("languages")))
    recognizeCommand.append(" > /dev/null 2>&1")
    os.system(' '.join(recognizeCommand))
    return current_txt

#save recognized boxes for sympols
def jpj2boxes(current_jpg, page):
    current_box = conf.box_dir + "/" + str(page)
    boxCommand = []
    boxCommand.append("tesseract")
    boxCommand.append(current_jpg)
    boxCommand.append(current_box)
    boxCommand.append("--dpi " + str(conf.settings.get("convertDensity")))
    boxCommand.append("--oem 1")
    boxCommand.append("--psm 6") 
    boxCommand.append(" -l "+ str(conf.settings.get("languages")))
    boxCommand.append(" lstmbox")
    boxCommand.append(" > /dev/null 2>&1")
    os.system(' '.join(boxCommand))
    return current_box


