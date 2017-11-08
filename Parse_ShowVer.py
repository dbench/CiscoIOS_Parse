"""
- This script iterates through the showveroutput.txt file to determine all IOS-XE devices and the version of code running
- The showveroutput.txt file is located at C:\Python27

- Created by Dustin Bench on 9/11/17
- Version 1.0

- This script is still a work in progress
"""

import sys
import re
from pprint import pprint

file = open('C:\Python27\showveroutput.txt', 'r')

# create regular expression to match the current software version
current_version = re.compile('Version ([0-9]*\.[0-9]*\.[0-9])')
device = re.compile('>>>>>>>>>>>>>>> Device ([0-9]*\.[0-9]*\.[0-9]*\.[0-9].)')
ios_xe = re.compile('Cisco IOS Software, IOS-XE Software')

for line in file:
    version_match = ios_xe.search(line)
    ip = device.search(line)
    if version_match:
        version = version_match.group(1)
        print(version_match)
    elif ip:
        ip_match = ip.group(1)
        print(ip_match)
        print 'Current versions of ios-xe switches'
        print '------------------------------------'
    else:
        continue

print ''

file.close()



