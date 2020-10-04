
from setuptools import setup

def readme():
  with open('README.md', 'r') as files:
    README = files.read()
    return README

setup(
  name = 'ipnc',
  packages = ['ipnc'],
  version = '0.1',
  license='MIT',
  description =('Indo Phone Number Checker (IPNC). Tools for checking your Indonesia phone number information'),
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'Wildan',
  author_email = 'fhxmaster@gmail.com',
  url = 'https://github.com/danrfq/IPNC',
  download_url = 'https://github.com/danrfq/IPNC/archive/v_01.tar.gz',
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