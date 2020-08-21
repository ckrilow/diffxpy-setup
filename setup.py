import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-ckrilow", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="chad.krilow@nih.gov",
    description="A setup script for the Difxpy module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ckrilow/diffxpy-setup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
