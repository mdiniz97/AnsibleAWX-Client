import io
from setuptools import  setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name="ansibleawx-client",
    version="0.1.1",
    description="Ansible AWX Client",
    license='MIT',
    url='https://github.com/mdiniz97/AnsibleAWX-Client/',
    author='Marcos Diniz',
    author_email='marcosdinizpaulo@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
