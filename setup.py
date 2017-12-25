from setuptools import setup

setup(name='tcdataimporter',
      version='0.1',
      description='Teamcenter Data Importer',
      url='http://github.com/storborg/funniest',
      author='Bela - Tamas Jozsa',
      author_email='jozsa.bela.tamas@gmail.com',
      license='Apache 2.0',
      packages=['tcdataimporter'],
      install_requires=['Django==2.0', 'djangorestframework', 'markdown', 'django-filter'],
      zip_safe=False)