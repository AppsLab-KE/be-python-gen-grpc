from setuptools import setup, find_packages
setup(
    name='everyshillings-proto',
    version='0.2.0',
    description='Apps:Lab everyshillings',
    author='Marvin Collins',
    author_email='marvin@appslab.co.ke',
    url='https://github.com/AppsLab-KE/be-python-gen-grpc',
    packages= ["everyshillingsproto"],
    install_requires=[
        'grpcio-tools',
        'grpcio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

