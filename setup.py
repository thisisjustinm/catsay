from setuptools import setup, find_packages

setup(
    name="catsay",
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    description="Make cats say stuff",
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    author="Justin M.",
    author_email="thisisjustinm@outlook.com",
    url="https://github.com/thisisjustinm/",
    license="MIT",
    install_requires=['beautifulsoup4', 'drawtable', 'soupsieve', 'argparse', 'termcolor', 'requests'],
    entry_points={
        'console_scripts': [
            'catsay = catsay.main:main',
        ],
    }
)
