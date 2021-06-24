from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='aws-utils',
    url='https://github.com/jezzbox/aws-utils',
    author='Jeremy Keelty',
    author_email='keeltyj@protonmail.com',
    # Needed to actually package something
    packages=['s3utils'],
    # Needed for dependencies
    install_requires=['pandas','s3fs','openpyxl'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='some aws functions for ease of use',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)