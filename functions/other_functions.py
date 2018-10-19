import logging
import os
from functions.ftp_xml import read_profile_xml


def set_ftp_profiles(self):
    logging.debug('other_functions.py - set_ftp_profiles')
    if os.path.isfile('ftp_profiles.xml'):
        self.ftp_profiles = read_profile_xml('ftp_profiles.xml')
