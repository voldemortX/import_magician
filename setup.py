import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="importmagician",
    version="0.1.0",
    author="Zhengyang Feng",
    author_email="zyfeng97@outlook.com",
    description="Voldemort's Python import helper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voldemortX/import_magician",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
