import logging
import collections


def objects_initialization(self):
    logging.debug('gui - objects_initialization.py - objects_initialization')
    self.ftp_profiles = collections.OrderedDict()
    self.hidden_items = {}
    
    self.old_local_path = ''
    
def tree_objects_init(self):

    self.type_icons = {'Image File':'file_image_icon.png',
                       'Video File':'file_video_icon.png',
                       'PDF File':'file_pdf_icon.png',
                       'Audio File':'file_audio_icon.png',
                       'eBook':'ebook_icon.png',
                       'Archive':'file_archive_icon.png',
                       'Executable':'exe_icon.png',
                       'Font':'font_icon.png',
                       'Word File':'file_word_icon.png',
                       'Excel File':'file_excel_icon.png',
                       'PowerPoint File':'file_powerpoint_icon.png',
                       'Data File':'data_icon.png',
                       'Text File':'file_text_icon.png',
                       'Shared Library':'dll_icon.png',
                       'NetCDF File':'netcdf_icon.png',
                       'HDF File':'hdf_icon.png',
                       'Subtitle File':'subtitle_icon.png',
                       'KeePass Database':'keefox_icon.png',
                       'Illustrator File':'illustrator_icon.png',
                       'InDesign File':'indesign_icon.png',
                       'Photoshop File':'photoshop_icon.png',
                       'BIN File':'bin_icon.png',
                       'XML File':'xml_file.png',
                       }
    
    self.file_types = {'jpg':'Image File',
                      'png':'Image File',
                      'gif':'Image File',
                      'webp':'Image File',
                      'cr2':'Image File',
                      'tif':'Image File',
                      'bmp':'Image File',
                      'jxr':'Image File',
                      'psd':'Photoshop File',
                      'ico':'Image File',
                      'svg':'Image File',
                      'eps':'Image File',
                      'ps':'Image File',
                      'cgm':'Image File',
                      'mp4':'Video File',
                      'm4v':'Video File',
                      'mkv':'Video File',
                      'webm':'Video File',
                      'mov':'Video File',
                      'avi':'Video File',
                      'wmv':'Video File',
                      'mpg':'Video File',
                      'flv':'Video File',
                      'ogv':'Video File',
                      'ogg':'Video File',
                      'rm':'Video File',
                      'rmvb':'Video File',
                      'mpeg':'Video File',
                      'vob':'Video File',
                      'pdf':'PDF File',
                      'mid':'Audio File',
                      'mp3':'Audio File',
                      'm4a':'Audio File',
                      'flac':'Audio File',
                      'wav':'Audio File',
                      'amr':'Audio File',
                      'epub':'eBook',
                      'zip':'Archive',
                      'tar':'Archive',
                      'rar':'Archive',
                      'gz':'Archive',
                      'bz2':'Archive',
                      '7z':'Archive',
                      'xz':'Archive',
                      'cab':'Archive',
                      'ar':'Archive',
                      'Z':'Archive',
                      'lz':'Archive',
                      'exe':'Executable',
                      'woff':'Font',
                      'woff2':'Font',
                      'ttf':'Font',
                      'otf':'Font',
                      'doc':'Word File',
                      'dot':'Word File',
                      'wbk':'Word File',
                      'docx':'Word File',
                      'docm':'Word File',
                      'dotx':'Word File',
                      'dotm':'Word File',
                      'docb':'Word File',
                      'xls':'Excel File',
                      'xlt':'Excel File',
                      'xlm':'Excel File',
                      'xlsx':'Excel File',
                      'xlsm':'Excel File',
                      'xltx':'Excel File',
                      'xltm':'Excel File',
                      'ppt':'PowerPoint File',
                      'pot':'PowerPoint File',
                      'pps':'PowerPoint File',
                      'pptx':'PowerPoint File',
                      'pptm':'PowerPoint File',
                      'potx':'PowerPoint File',
                      'potm':'PowerPoint File',
                      'ppsx':'PowerPoint File',
                      'ppsm':'PowerPoint File',
                      'xml':'XML File',
                      'dat':'Data File',
                      'txt':'Text File',
                      'dll':'Shared Library',
                      'nc':'NetCDF File',
                      'hdf':'HDF File',
                      'h4':'HDF File',
                      'hdf4':'HDF File',
                      'he4':'HDF File',
                      'h5':'HDF File',
                      'hdf5':'HDF File',
                      'he5':'HDF File',
                      'srt':'Subtitle File',
                      'kdbx':'KeePass Database',
                      'ai':'Illustrator File',
                      'indd':'InDesign File',
                      'bin':'BIN File',
                      '':'',
                      '':'',
                      '':'',
                      '':'',
                      '':'',
                      '':'',
                      }
    

def profile_window_objects_initialization(self):
    logging.debug('gui - objects_initialization.py - objects_initialization')
    self.ftp_protocols_dict = {'File Transfer Protocol (FTP)':'ftp',
                               'SSH File Transfer Protocol (SFTP)':'sftp'}
    self.inv_ftp_protocols_dict = {'ftp':'File Transfer Protocol (FTP)',
                                   'sftp':'SSH File Transfer Protocol (SFTP)'}
    