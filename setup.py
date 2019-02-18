from setuptools import setup

def get_readme():
    return open('README.md').read()

setup(name='PyScanner',
      version='1.0',
      packages=['scanner'],
      description='Java-like input scanner.',
      long_description=get_readme(),
      author='Kanat Bekt',
      author_email='bekt17@gmail.com',
      url='https://github.com/Bekt/PyScanner'
)
