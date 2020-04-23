import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dijkstra-Algorithm", # Replace with your own username
    version="1.2.0",
    author="Rocchio Pietro - Cerbaro Jessica",
    description="A small example package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pietro2356/Dijkstra-Algorithm.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)