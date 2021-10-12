from distutils.core import setup

setup(
    name='Certificate Generator',
    version='2.0',
    description='Generates and emails certificates',
    author='Ajay Raj Nelapudi',
    author_email='ajayraj.cseanits@gmail.com',
    url='https://ajayrajnelapudi.github.io/',
    install_requires=[
        'opencv-python==4.2.0.32',
        'img2pdf==0.3.3',
    ]
)