import logging
import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow
from ui.version import gui_version
from functions.utilities import read_translations, create_logging_handlers, create_option_file
import configparser


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    main_path = os.path.abspath(os.path.dirname(__file__))
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('icons/orionftp_splashscreen.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    config_dict = configparser.ConfigParser()
    if not os.path.exists(os.path.join(main_path, 'orion_ftp.ini')):
        create_option_file(main_path, config_dict)
    config_dict.read(os.path.join(main_path, 'orion_ftp.ini'))
    create_logging_handlers(config_dict, 'orion_ftp.log')
    logging.info('**********************************')
    logging.info('OrionFTP ' + gui_version + ' is starting ...')
    logging.info('**********************************')
    logging.info('OrionFTP - operating system: ' + str(sys.platform))
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.info('OrionFTP - python version: ' + python_version)
    translations = read_translations()
    ui = MainWindow(main_path, config_dict, translations)
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())
