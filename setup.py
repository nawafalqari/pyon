from setuptools import setup, find_packages

# README.md
with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='pyonr',
    packages=find_packages(),
    version='1.0.0b1',
    description='PYON Reader - Python Object Nation',
    author='Nawaf Alqari',
    author_email='nawafalqari13@gmail.com',
    keywords=['pyon', 'pyonr', 'json', 'pythonobjectnation', 'python object nation'],
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/nawafalqari/pyon/',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)