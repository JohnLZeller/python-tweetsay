python-tweetsay
===============
Copyright 2013 John Zeller <johnlzeller@gmail.com>
Licensed under the GNU LGPL version 3.0

Description
-----------
Python-tweetsay gives you the ability to bring the most recent twitter update from your home timeline to the comfort of your terminal. Python-tweetsay is setup to run once each time a new Terminal window is opened, and it can also be called with the bash command tweetsay.

Dependancies
------------
python-twitter [<http://code.google.com/p/python-twitter/>](http://code.google.com/p/python-twitter/)

System Requirements
-------------------
Operating System: Linux or Mac OSX

How to Install
--------------
In order to properly install python-tweetsay, you will need to both install python-twitter and also setup a Twitter app on your personal Twitter account.

1. Install python-twitter by going [here](http://code.google.com/p/python-twitter/)
2. Go to [<https://dev.twitter.com/user/login?destination=home>](https://dev.twitter.com/user/login?destination=home) and sign-in with your normal Twitter credentials
3. Once signed in, click your avatar in the upper-righthand corner of the screen and select 'My applications' from the drop-down menu
4. Select 'Create a new application'
5. Use the following to fill out the form:
	* Name: python-tweetsay
	* Description: Python-tweetsay gives you the ability to bring the most recent twitter update from your home timeline to the comfort of your terminal.
	* Website: https://github.com/JohnLZeller/python-tweetsay
6. Click that you agree, enter the captcha and hit 'Create your twitter application'
7. Now that you've created the application, you must generate an Access token. Select 'Create my access token' at the bottom of the page.
8. Now go ahead and select the tab that says 'OAuth tool' and you will have easy access to the tokens you need for the next step.
9. From your terminal, navigate to the directory you placed python-tweetsay and cd into python-tweetsay
10. Enter 'sudo python setup.py install'
11. The prompt will now ask you to enter the tokens you just generated. Please do so for Consumer key, Consumer secret, Access token and Access token secret.
12. You are done! You can now enjoy the awesomeness that is tweets in your terminal! Type tweetsay and you can test it out :)

Notes
-----
Python-tweetsay is a modified verion of cowsay-py. Cowsay-py was written by Jesse Chan-Norris <jcn@pith.org> and is also licensed under the GNU LGPL version 3.0