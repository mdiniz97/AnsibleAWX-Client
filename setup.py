from setuptools import  setup, find_packages

setup(
    name="ansibleawx-client",
    version="0.1.0",
    description="Ansible AWX Client",
    license='MIT',
    url='https://github.com/mdiniz97/AnsibleAWX-Client/',
    author='Marcos Diniz',
    author_email='marcosdinizpaulo@gmail.com',
    packages=find_packages(),
    include_package_data=True,
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
