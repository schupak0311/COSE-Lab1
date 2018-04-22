from setuptools import setup

setup(name='Sport events analyzer',
      author='Egor Schupakovskiy, Alex Pivnenko, Vlad Nechiporenko',
      packages=['sport_analyzer'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'], install_requires=['requests', 'lxml', 'coverage'],)
