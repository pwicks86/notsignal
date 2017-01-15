import setuptools

setuptools.setup(
    name="notsignal",
    version="0.1.0",
    url="https://github.com/pwicks86/notsignal",

    author="Paul Wicks",
    author_email="pwicks86@gmail.com",

    description="Software for emergency brake from Viennese tram",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
