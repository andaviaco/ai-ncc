from setuptools import setup

setup(name='aincc',
      version='0.1',
      description='Evolutionary Algorithm approach for Normalized Cross-Correlation (NCC).',
      url='https://github.com/andaviaco/de',
      author='Andrés Ávila',
      author_email='andaviaco@gmail.com',
      license='MIT',
      packages=['aincc'],
      dependency_links=['https://github.com/andaviaco/de/tarball/master#egg=devol-0.1'],
      install_requires=[
          'numpy==1.13.3',
          'Pillow==4.3.0',
          'matplotlib==2.1.0'
      ],
      zip_safe=False)
