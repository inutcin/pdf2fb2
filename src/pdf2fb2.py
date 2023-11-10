import sys

sys.path.append("./lib")

import os
import conf
import shell 

start_page = int(conf.settings.get('start_page'))
end_page = int(conf.settings.get('end_page'))

for dirname in [conf.jpeg_dir, conf.txt_dir, conf.box_dir]:
    if os.path.isdir(dirname)!=True:
        os.makedirs(dirname, 0o777)

for i in range(start_page, end_page + 1):
    print("Page" + str(i) + ":", end="\n---------\n")
    # Convert PDF page to JPEG image
    print ("    Converting to jpg", end=' ... ')
    current_jpg = shell.pdf2jpg(page = i)
    print("[Done]")

    #recognize single page and save it as text file
    print("    Recognizing", end=" ... ")
    current_txt = shell.jpg2txt(current_jpg, page = i)
    print("[Done]")

    #save recognized boxes for sympols
    print("    Boxing", end=" ... ")
    current_box = shell.jpj2boxes(current_jpg, page = i)
    print("[Done]")

    # remove temporary files
    # for remfile in [current_jpg]:
    #     os.remove(current_jpg)
        

