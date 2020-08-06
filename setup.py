import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ugreshaper", # Replace with your own username
    version="0.0.1",
    author="Ezmet",
    author_email="azmat3111@gmail.com",
    description="Text reshaper package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abdusalamstd/ugreshaper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)