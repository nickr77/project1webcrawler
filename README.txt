Installation instructions:

Dependencies: "BeautifulSoup", "Mechanize", "snowballstemmer"

1. Unzip files into empty directory
2. If the above dependencies are already installed, skip to step 5
3. Make sure python 2.7.x is installed on your system
4. In the directory you chose, type 'install.py install' (without quotes), if this doesn't work, see step 8
5. After dependencies are installed: type "main.py" or "python main.py" to run the program
6. You will be prompted to enter a page crawl limit. Please enter a positive integer
7. Output files will be created

Troubleshooting:
8.  If the install didn't work, you will need to manually install the dependencies
8a. Follow the steps located at 'http://python-packaging-user-guide.readthedocs.org/en/latest/installing/', specifically install setuptools and pip
8b. Once pip is installed run the following commands:
8c. "pip install 'BeautifulSoup', pip install 'Mechanize', 'pip install 'snowballstemmer'"
8d. Hopefully that will work, if it does: return to step 5