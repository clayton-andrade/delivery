from setuptools import setup, find_packages

def read(filename):
    with open(filename) as file:
        return [req.rstrip() for req in file.readlines()]

setup(
    name="delivery",
    version="0.1.0",
    description="Delivery App",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)