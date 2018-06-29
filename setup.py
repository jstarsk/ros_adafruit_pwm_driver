## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['Adafruit_Python_PCA9685'],
    package_dir={'': 'include'})

setup(**setup_args)

# install PCA9685
# import Adafruit_Python_PCA9685
# setup('install')
