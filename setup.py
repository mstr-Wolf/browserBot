import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meet-sourcerer0", # Replace with your own username
    version="1.4.1.3",
    author="Lo Han",
    author_email="lohan.uchsa@protonmail.com",
    description="Online meeting automation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourcerer0/meet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: GNU/Linux, OS Independent",
    ],
    python_requires='>=3.6',
)