from setuptools import setup

setup(
    name='webfile',
    version='0.1.0',    
    description='A simple webfile api',
    url='https://github.com/prakis/webfile',
    author='Kishore',
    author_email='prakis@gmail.com',
    license='MIT',
    packages=['webfile'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)