#BatchInstall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn‘，“requests",\
        "jieba","beautifulsoup4’，'wheel‘，'networkx","sympy",\
        "pyinstaller","diango","flask","werobot","pyqt5",\
        "pandas","pyopeng1","pypdf3","docopt","pygame",\
        "pdfminer","python-docx","openpyxl","wxpython",\
        "ipython","pygtk","theano","Tensorflow","scikit-learn",\
        "Pyramid","cocos2d","panda3D","tvtk","mayavi","scrapy",\
        "scipy","tesserocr","puinstaller"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")
        

