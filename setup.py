from setuptools import setup

setup(
    name='webcrawler',
    version='0.1',
    py_modules=['main'],
    url='https://github.com/nickr77/project1webcrawler',
    install_requires=['BeautifulSoup', 'Mechanize', 'snowballstemmer'],
    author='sbock-nroberts',
    author_email='robertsn@smu.edu',
    description='Web Crawler Project for CSE 5337; Steven Bock - Nick Roberts'
)
