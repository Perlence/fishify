from setuptools import setup

with open('README.md') as fp:
    README = fp.read()

setup(
    name='fishify',
    version='1.0',
    author='Sviatoslav Abakumov',
    author_email='dust.harvesting@gmail.com',
    description='Modify environment in fish shell with variables from script '
                'output.',
    long_description=README,
    url='https://github.com/Perlence/fishify',
    download_url='https://github.com/Perlence/fishify/archive/master.zip',
    py_modules=['fishify'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'fishify = fishify:main',
        ],
    },
    install_requires=[
        'six',
    ],
    classifiers=[
        'Development Status :: 3 - Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
    ]
)
