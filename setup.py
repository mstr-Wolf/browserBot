import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ethmeet",
    version="1.6.1-b.2",
    author="Lo Han",
    author_email="lohan.uchsa@protonmail.com",
    description="Video-chat API. Compatible with most famous platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elleaech/ethmeet",
    packages=setuptools.find_packages(),
    keywords="bot firefox automation browser selenium meeting zoom google",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
    scripts=[
        'scripts/gecko_install.py',
    ],
    install_requires=[
        'bleach==3.3.0',
        'build==0.2.1',
        'certifi==2020.12.5',
        'cffi==1.14.5',
        'chardet==4.0.0',
        'colorama==0.4.4',
        'cryptography==3.4.4',
        'docutils==0.16',
        'idna==2.10',
        'jeepney==0.6.0',
        'keyring==22.0.1',
        'packaging==20.9',
        'pep517==0.9.1',
        'pkginfo==1.7.0',
        'pycparser==2.20',
        'Pygments==2.7.4',
        'pyparsing==2.4.7',
        'readme-renderer==28.0',
        'requests==2.25.1',
        'requests-toolbelt==0.9.1',
        'rfc3986==1.4.0',
        'SecretStorage==3.3.1',
        'selenium==3.141.0',
        'six==1.15.0',
        'toml==0.10.2',
        'tqdm==4.56.2',
        'twine==3.3.0',
        'urllib3==1.26.3',
        'webencodings==0.5.1'
    ]
)
