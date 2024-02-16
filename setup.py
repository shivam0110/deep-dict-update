from setuptools import setup, find_packages

setup(
    name='deep-dict-update',
    version='0.1.6',
    author='Shivam Malpani',
    author_email='shivammalpani111@gmail.com',
    description='Recursively update nested dictionaries with another dictionary',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shivam0110/deep-dict-update',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
