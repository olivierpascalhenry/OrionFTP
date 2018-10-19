Version:
-------

OrionFTP 0.5.0.


Project Overview:
-----------------

The idea behind OrionFTP is to propose a small and simple FTP client with basic options. It was designed for my own use and for my familly (in particular my father). It is based on Python 3.5, PyQt 5.10 and written with the help of Eclipse.


Important information:
----------------------

Until version 1.0.0, the config file is expected to evolve and can be deleted without further notice to introduce new options.


Features:
---------

For now, it can download files from a FTP or SFTP server. In the future, folder(s) download and basic upload will be added. Drag and drop is not available at this time, but it will be in a future release.


Compatibility:
--------------
    - sources : linux, windows, macos
    - binaries : windows (from Windows 7 32), linux (not yet)


Install instructions for binaries:
----------------------------------
Download and install the last binary file in the Release directory. Actually, the binary file is only compatible with Windows (from Windows 7 32) and Linux (from Ubuntu 14.04). The software should be installed in the Home directory for Linux, and outside the Program Files directory for Windows to avoid issues with Windows admin protections.


Install instructions for sources:
---------------------------------
Download sources and uncompress them somewhere on your hard drive. Open a terminal in the new directory and launch CMEMS Data Downloader by typing: python cmems_data_downloader.py. Do not forget to install dependencies :

* PyQt5 v5.11+
* requests v2.18+


Documentation:
--------------

Actually there are 3 different info window to give details on how the option window, the FTP manager and the main window work. A formal documentation will be released later.
