#!/usr/bin/env python

"""
Copyright 2013 John Zeller <johnlzeller@gmail.com>
Licensed under the GNU LGPL version 3.0

Description: Python-tweetsay gives you the ability to bring the most recent twitter update from your home timeline to the
    comfort of your terminal. Python-tweetsay is setup to run once each time a new Terminal window is opened, and
    it can also be called with the bash command tweetsay.

    Some configuration is necessary to get the proper information from your twitter account, so please read the
    README file completely and thoroughly.

Dependancies:
    python-twitter <http://code.google.com/p/python-twitter/>

Note: Python-tweetsay is a modified verion of cowsay-py. Cowsay-py was written by Jesse Chan-Norris <jcn@pith.org>
    and is also licensed under the GNU LGPL version 3.0
"""

import sys
import textwrap
import twitter
import platform
system = platform.system()
if system == 'Darwin':
    sys.path.append('/Library/Python/2.7/site-packages/python-tweetsay/')
elif system == 'Linux':
    sys.path.append('/usr/local/lib/python2.7/python-tweetsay/')

def tweetsay(str, length=40):
    return buildBubble(str, length) + buildBird()

def buildBird():
    return """
                                      \\
                              IIII     \\
                   ZZ~      ?IIIIII?    \\
             : I7=?+Z$$$7ZI7IIIII..,I:   \\
             ,7+?IIII$$$$IIIIIIII,.III7, /
                +?IIIIIIIIIIIIIIIIIII,
                   I7IIIIIIIIIIIIIIII
                   IIIIIIIIIII?+:,=I
                =?IIIIIIIIIII:::::::
  ,=        ,=IIIIIIIIIIIII:::::,:,
     ~?I??IIIIIIIIIIIIIIII:::,:::
        +?IIIIIIIIIIIIIII:::::::
           ~IIIIIIIIIIIII:::::
                 ~?IIIIII=
    """

def buildBubble(str, length=40):
    bubble = []

    lines = normalizeText(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = getBorder(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalizeText(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def getBorder(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]

    elif index == 0:
        return [ "/", "\\" ]
    
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    
    else:
        return [ "|", "|" ]

def initApi():
    if system == 'Darwin':
        f = open('/Library/Python/2.7/site-packages/python-tweetsay/tweetsay.conf', 'r')
    elif system == 'Linux':
        f = open('/usr/local/lib/python2.7/python-tweetsay/tweetsay.conf', 'r')
    keys = []
    for line in f:
        keys.append(line[:-1])  # The -1 removes the added '\n' newline character from the end of each line
    f.close

    api = twitter.Api(consumer_key=keys[0], consumer_secret=keys[1], access_token_key=keys[2],  access_token_secret=keys[3])
    return api

def getMsg():
    recent = api.GetHomeTimeline()[0]
    msg = recent.text + " - " + recent.user.screen_name
    return msg

if __name__ == '__main__':
    api = initApi()
    msg = getMsg()

    print tweetsay(msg)
