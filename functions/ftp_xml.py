import xml.dom.minidom
import datetime
import logging
import collections


NAMESPACE_URI = 'OrionFTP'


def create_profile_xml(out_file_name, ftp_profiles):
    logging.debug('ftp_xml.py - create_profile_xml - starting ...')
    doc = xml.dom.minidom.Document()
    doc_root = add_element(doc, "OrionFTP", doc)
    add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
    
    ############################
    # Add server
    ############################
    servers = add_element(doc, "Servers", doc_root)
    for key, profile in ftp_profiles.items():
        server = add_element(doc, "Server", servers)
        add_element(doc, "Name", server, key)
        add_element(doc, "Protocol", server, profile['protocol'])
        add_element(doc, "Encryption", server, profile['encryption'])
        add_element(doc, "Host", server, profile['host'])
        add_element(doc, "Port", server, profile['port'])
        add_element(doc, "Username", server, profile['username'])
        add_element(doc, "Password", server, profile['password'])
    
    ############################
    # File Creation
    ############################
    logging.debug('ftp_xml.py - create_profile_xml - file creation ...')
    f = open(out_file_name, 'w')
    f.write(doc.toprettyxml())
    f.close()
    logging.info('ftp_xml.py - create_profile_xml - xml file successfully created')
    

def read_profile_xml(xml_file):
    logging.debug('ftp_xml.py - read_profile_xml - xml file reading in progress (' + str(xml_file) + ') ...')
    f = open(xml_file, 'r')
    doc = xml.dom.minidom.parse(f)
    ftp_profiles = collections.OrderedDict()
    
    ############################
    # Servers
    ############################
    servers = doc.getElementsByTagName('Servers')[0]
    nodes = servers.getElementsByTagName('Server')
    for node in nodes:
        profile = dict()
        protocol = get_element_value(node, 'Protocol')
        host = get_element_value(node, 'Host')
        encryption = get_element_value(node, 'Encryption')
        port = get_element_value(node, 'Port')
        username = get_element_value(node, 'Username')
        password = get_element_value(node, 'Password')
        if protocol is None:
            protocol = ''
        if host is None:
            host = ''
        if encryption is None:
            encryption = ''
        if port is None:
            port = ''
        if username is None:
            username = ''
        if password is None:
            password = ''
        profile['protocol'] = protocol
        profile['host'] = host
        profile['port'] = port
        profile['encryption'] = encryption
        profile['username'] = username
        profile['password'] = password
        ftp_profiles[get_element_value(node, 'Name')] = profile
    
    logging.info('ftp_xml.py - read_profile_xml - xml file successfully parsed')
    return ftp_profiles


def add_element(doc, element_name, parent, value=None):
    new_element = doc.createElementNS(NAMESPACE_URI, element_name)
    if value:
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element


def get_element_value(parent, element_name):
    elements = parent.getElementsByTagName(element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()
