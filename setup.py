from setuptools import setup, find_packages



setup(
    name='otter_factory', 
    version='0.0.1', 
    packages=find_packages(),
    install_requires=[
        "numpy", "scikit-learn",
    ],
    )
