from setuptools import setup, find_packages
 
setup(
    name                = 'k1rh4pip',
    version             = '0.2',
    description         = 'test apt attack',
    author              = 'k1rh4.lee',
    author_email        = 'k1rha87@gmail.com',
    url                 = 'https://github.com/k1rh4/k1rh4pip',
    download_url        = 'https://github.com/k1rh4/k1rh4pip/archive/master.zip',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['pypi deploy'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
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
