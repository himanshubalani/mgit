from setuptools import setup

setup (name= "mgit",
	   version="1.0",
	   packages=["mgit"],
	   entry_points = {
           'console_scripts' : [
               'mgit = mgit.cli:main'
           ]
       })