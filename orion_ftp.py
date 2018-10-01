import logging
import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow
from ui._version import _gui_version
import configparser


def launch_egads_gui(path):
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('icons/orionftp_splashscreen.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    config_dict = configparser.ConfigParser()
    if not os.path.exists(os.path.join(path, 'orion_ftp.ini')):
        ini_file = open(os.path.join(path, 'orion_ftp.ini'), 'w')
        config_dict.add_section('LOG')
        config_dict.add_section('OPTIONS')
        config_dict.set('LOG','level','DEBUG')
        config_dict.set('LOG','path', '')
        config_dict.set('OPTIONS','check_update','False')
        config_dict.set('OPTIONS','language','english')
        config_dict.set('OPTIONS','default_profile','')
        config_dict.set('OPTIONS','local_home','')
        config_dict.write(ini_file)
        ini_file.close()   
    config_dict.read(os.path.join(path, 'orion_ftp.ini'))
    
    
    log_filename = os.path.join(config_dict.get('LOG', 'path'),'orion_ftp.log')
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = log_filename,
                        level = getattr(logging, config_dict.get('LOG', 'level')),
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('**********************************')
    logging.info('OrionFTP ' + _gui_version + ' is starting ...')
    logging.info('**********************************')
    logging.info('OrionFTP - operating system: ' + str(sys.platform))
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.info('OrionFTP - python version: ' + python_version)
    translations = read_translations()
    ui = MainWindow(path, config_dict, translations)
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())


def read_translations():
    translations = {}
    file_list = os.listdir('translations/')
    logging.info('OrionFTP - read_translations - files: ' + str(len(file_list)))
    for file in file_list:
        name = file[:-4]
        f = open('translations/' + file, 'r', encoding='utf-8')
        for line in f:
            if line[:3] != '###':
                index = line.find('=')
                widget = line[:index]
                text = line[index + 1:].replace('\n','')
                if '|' in text:
                    text = text.split('|')
                if text:
                    try :
                        existing_dict = translations[widget]
                    except KeyError:
                        existing_dict = {}
                    existing_dict[name] = text
                    translations[widget] = existing_dict
        f.close()
    return translations


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    launch_egads_gui(path)
    
