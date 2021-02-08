import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meet",
    version="1.4.2",
    author="Lo Han",
    author_email="lohan.uchsa@protonmail.com",
    description="Online meeting automation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourcerer0/meet",
    packages=setuptools.find_packages(),
    keywords="bot firefox automation browser selenium meeting zoom google",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: GNU/Linux, OS Independent",
    ],
    python_requires='>=3.6',
)