from setuptools import setup

setup(name='colorsh',
      version='0.1',
      description='simple ansi/tmux text decorator',
      url='http://github.com/radiand/colorsh',
      author='radiand',
      author_email='radiand@protonmail.com',
      license='MIT',
      packages=['colorsh'],
      scripts=["scripts/colorsh-cli"],
      zip_safe=False)
