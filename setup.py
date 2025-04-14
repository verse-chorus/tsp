from setuptools import setup, find_packages

setup(
    name="tsp-solver",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "pandas>=1.3.0",
    ],
    author="Ian Schmidt",
    author_email="yanschmidt@mail.ru",
    description="A Traveling Salesman Problem solver using Genetic Algorithms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/travel_salesman_problem",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 