from setuptools import setup, find_packages

# README.md
with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='pyonr',
    packages=find_packages(),
    version='1.0.0b6',
    description='PYON Reader - Python Object Nation',
    author='Nawaf Alqari',
    author_email='nawafalqari13@gmail.com',
    keywords=['pyon', 'pyonr', 'json', 'pythonobjectnation', 'python object nation'],
    long_description=readme,
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://github.com/nawafalqari/pyon#readme',
        'Bug Tracker': 'https://github.com/nawafalqari/pyon/issues',
        'Source Code': 'https://github.com/nawafalqari/pyon/',
        'Discord': 'https://discord.gg/cpvynqk4XT'
    },
    license='MIT',
    url='https://github.com/nawafalqari/pyon/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)