# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Thu Mar 26 11:08:45 2009
#      by: The Resource Compiler for PyQt (Qt v4.5.0)
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore

qt_resource_data = "\
\x00\x00\x00\x35\
\x46\
\x69\x6e\x65\x21\x20\x44\x69\x73\x68\x6f\x6e\x6f\x72\x21\x20\x44\
\x69\x73\x68\x6f\x6e\x6f\x72\x20\x6f\x6e\x20\x79\x6f\x75\x2c\x20\
\x64\x69\x73\x68\x6f\x6e\x6f\x72\x20\x6f\x6e\x20\x79\x61\x20\x63\
\x6f\x77\x21\x0a\
"

qt_resource_name = "\
\x00\x09\
\x06\xa8\xaa\x74\
\x00\x71\
\x00\x75\x00\x6f\x00\x74\x00\x65\x00\x2e\x00\x74\x00\x78\x00\x74\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()