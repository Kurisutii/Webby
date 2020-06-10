#!/usr/bin/python
# -*- coding: utf-8 -*-
# Started 10 June 2020.
# Author - Kurisuti.
# Python Version 3.8.2.
# Web Request Handler and Manipulator.
# Designed for Debian Based Distro's.

# Library importing.

import os
import sys
import time
import requests
import subprocess

# Function defining.

def rootcheck():
    if os.geteuid() != 0:
        exit("""

              [#] This script has to be run with 'sudo' or from user 'root'.

             """)

def request(url):
    req = requests.get(url)
    print ('        [#] Response Code: ' + str(req.status_code))
    print ('\n      [#] Response:\n' + req.text)

def requestoutput(url , output):
    req = requests.get(url)
    print ('        [#] Response Code: ' + str(req.status_code))
    print ('\n      [#] Response:\n' + req.text)
    file = open(output , "a")
    status = "[#] Response Code: " + str(req.status_code) 
    text = req.text.encode('utf-8').strip()
    file.write(status)
    file.write("\n")
    file.write(text)
    file.close()

def helpie():
    print ("""

        [#] Webby - v0.1. - Usage : [ -u (URL) -- URL of the target. ex. 'https://www.google.com' ]
                                    [ -o (*.txt) -- Output text file location. ex. '/home/me/out.txt')]
                                    [ -h -- Show this help page.]

           """)

# Checking for [ROOT] permissions.

# Currently not needed. # rootcheck()

# Defining arguments as variables.

a_url = '-u'
a_output = '-o'
a_help = '-h'

# Get the total number of args passed to the script.
total = len(sys.argv)

# Get the arguments list.
cmdargs = str(sys.argv)

# Printing usage and help page.

if total == 1:
    helpie()

# Main madness and weirdness.

if total == 2 and sys.argv[1] == a_help:
    helpie()

if total == 2 and sys.argv[1] == a_url:
    helpie()

if total == 3 and sys.argv[1] == a_output:
    helpie()

if total == 2 and sys.argv[1] == a_output:
    helpie()

if total == 4 and sys.argv[1] == a_url and sys.argv[3] == a_output:
    helpie()

if total == 3 and sys.argv[1] == a_url:
        url = sys.argv[2]
        request(url)

if total == 5 and sys.argv[1] == a_url and sys.argv[3] == a_output:
    url = sys.argv[2]
    output = sys.argv[4]
    requestoutput(url , output)
