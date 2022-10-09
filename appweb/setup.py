from setuptools import setup
import sys,os

setup(
    name = 'appweb',
    version = '0.1.0',
    description = 'appweb with Python and Flask',
    license='Public Domain',
    author = 'diegocerinom',
    packages = ['src'],
    package_data={'src': ['description.txt']},
    install_requires=['click', 'Flask', 'itsdangerous', 'Jinja2', 'MarkupSafe', 'pip', 'setuptools', 'Werkzeug', 'waitress'],
    entry_points = {'console_scripts': ['appweb=src.appweb:main']},
    python_requires='>=3.6',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX',
        'License :: Public Domain'],
)
