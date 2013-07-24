#!/usr/bin/env python

"""
Copyright 2013 John Zeller <johnlzeller@gmail.com>
Licensed under the GNU LGPL version 3.0

Description: Setup.py handles gathering the appropriate information from the user and then installing all necessary
    dependancies before completely installing python-tweetsay.

Dependancies:
    python-twitter <http://code.google.com/p/python-twitter/>

Note: Python-tweetsay is a modified verion of cowsay-py. Cowsay-py was written by Jesse Chan-Norris <jcn@pith.org>
    and is also licensed under the GNU LGPL version 3.0
"""

import os
import sys
import platform
import shutil
import getpass
from distutils.core import setup

def install_mac(user):
    print "Installing for Mac OS X"
    generate_conf()
    print "Moving python-tweetsay to python third-party module directory"
    dest_dir = '/Library/Python/2.7/site-packages/python-tweetsay'
    tweetsay_files = os.listdir('./')
    if os.path.exists(dest_dir):
        print "Removing old python-tweetsay directory..."
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    for current_file in tweetsay_files:
        if current_file == '.git':
            continue
        shutil.copy(current_file, dest_dir)
    print "Adding tweetsay bash alias"
    f = open('/etc/profile', 'a')
    f.write('\n')
    f.write("alias tweetsay='python /Library/Python/2.7/site-packages/python-tweetsay/tweetsay.py'\n")
    print "Adding tweetsay to Terminal startup sequence"
    f.write('tweetsay\n')
    f.close()

def install_linux(user):
    print "Installing for Linux"
    generate_conf()
    print "Moving python-tweetsay to python third-party module directory"
    dest_dir = '/usr/local/lib/python2.7/python-tweetsay'
    tweetsay_files = os.listdir('./')
    if os.path.exists(dest_dir):
        print "Removing old python-tweetsay directory..."
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    for current_file in tweetsay_files:
        current_file = './' + f
        if current_file == '.git':
            continue
        shutil.copy(current_file, dest_dir)
    print "Adding tweetsay bash alias"
    f = open('~/.bashrc', 'a')
    f.write('\n')
    f.write("alias tweetsay='python /usr/local/lib/python2.7/python-tweetsay/tweetsay.py'\n")
    print "Adding tweetsay to Terminal startup sequence"
    f.write('tweetsay\n')
    f.close()

def generate_conf():
    print "Generating config file..."
    try:
        open('tweetsay.conf')
        print "Removing old tweetsay.conf..."
        os.remove('tweetsay.conf')
    except:
        pass
    # api = twitter.Api(consumer_key='Uz00Z196A2HhDZD0Ngkg', consumer_secret='zohYxLdAxIIOgJs9MUcmM0StDBhmVxXsBtDuSJ8wY', 
    #    access_token_key='588065061-xIDtBBTVQxNXGd2x9Qre9hGNk7sD6YEYjaSMYOYw',  access_token_secret='SbHIEyCwKvDdzQsWvDBx7UDrnQS5tm49j0w2ymkO8')
    print "Before proceeding with the installation, we are going to need to know some information from your Twitter account."
    print "If you have not yet done so, go follow the directions in your README file to get the appropriate information."
    print "Please enter the following information EXACTLY as shown on your dev.twitter.com account page."
    keys = []
    keys.append(raw_input('Consumer Key: '))
    keys.append(raw_input('Consumer Secret: '))
    keys.append(raw_input('Access Token: '))
    keys.append(raw_input('Access Token Secret: '))

    f = open('tweetsay.conf', 'wb')
    for key in keys:
        f.write(key + '\n')
    f.close()

if "install" in sys.argv:
    setup(name='Python-tweetsay',
      version='1.0',
      description='Python-tweetsay gives you the ability to bring the most recent twitter update from your home timeline to the \
                    comfort of your terminal. Python-tweetsay is setup to run once each time a new Terminal window is opened, and \
                    it can also be called with the bash command tweetsay.',
      author='John Zeller',
      author_email='johnlzeller@gmail.com',
      url='https://github.com/JohnLZeller/python-tweetsay',
      requires=['twitter']
     )

    system = platform.system()
    user = getpass.getuser()
    if system == 'Darwin':
        install_mac(user)
    elif system == 'Linux':
        print "Installing for Linux"
        install_linux(user)
    elif system == 'Windows':
        print "Sorry, python-tweetsay is not configured to install on Windows at this time. But, keep checking back!"
        sys.exit(0)
    print "Congratz! Python-tweetsay has been installed :) Try it out by typing 'tweetsay'"
else:
    print "Usage: {0} setup.py install"
    sys.exit(0)
