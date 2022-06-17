from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="targetnet",
    version="0.0.1",
    description="TargetNet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    url="https://github.com/katarinagresova/TargetNet",
    packages=find_packages(include=["src"]),
    package_dir={"src": "src"},
    scripts=[],
    install_requires=[
        "pip>=20.0.1",
        "numpy>=1.17.0",
        "pandas>=1.1.4",
        "biopython>=1.79",
        'torch>=1.9.0'
    ],
    #tests_require=["pytest"],
    include_package_data=True,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 3 - Alpha",
        # Define that your audience are developers
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)