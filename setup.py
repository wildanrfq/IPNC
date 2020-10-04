
from distutils.core import setup

def readme():
  with open('README.md', 'r') as files:
    return files.read()

setup(
  name = 'ipnc',
  packages = ['ipnc'],
  version = '0.1',
  license='MIT',
  description = 'Indo Phone Number Checker (IPNC). Tools for checking your Indonesia phone number information',   # Give a short description about your library
  long_description=readme(),
  author = 'YOUR NAME',
  author_email = 'your.email@domain.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['numberphone', 'phone', 'indonesia'],
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)