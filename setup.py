"""
Setup
"""
import os

from setuptools import setup, find_namespace_packages


DIST_NAME = "qathir"
PACKAGE_NAME = "qathir"

REQUIREMENTS = [
    "numpy",
    "qiskit",
    "qiskit-optimization",
    # "dimod",
    "matplotlib",
    "rustworkx",
    "docplex",
    "pyqubo",
    # "seaborn",
    # "dwave-ocean-sdk",
    # "dwave_networkx",
    # "amazon-braket-default-simulator",
    # "amazon-braket-sdk",
    # "amazon-braket-ocean-plugin",
]

EXTRA_REQUIREMENTS = {
    "dev": [
        "jupyterlab>=3.1.0",
        "mypy",
        "pylint",
        "black",
        "sphinx",
        "sphinx-book-theme",
        "sphinxcontrib-napoleon",
        "Jinja2<3.1",  # https://github.com/readthedocs/readthedocs.org/issues/9038
    ],
}

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH) as readme_file:
    README = readme_file.read()

version_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), PACKAGE_NAME, "VERSION.txt")
)

with open(version_path, "r") as fd:
    version_str = fd.read().rstrip()


setup(
    name=DIST_NAME,
    version=version_str,
    description=DIST_NAME,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/qcnet/NYUAD-2023",
    author="Anubhav Shrestha, Deepesh Garg, Dhruv Srinivasan, Dilyara Sharipova, Oyungerel Amarsanaa, Samhitha Bharthulwar, Sasha, Shantanu Jha, Tasnim Ahmed, Yeji Han",
    author_email="REDACTED_EMAIL",
    license="MIT",
    packages=find_namespace_packages(exclude=["tutorials*"]),
    install_requires=REQUIREMENTS,
    extras_require=EXTRA_REQUIREMENTS,
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    ],
    keywords="quantum computing, water distribution network, fault localization, sensor placement",
    python_requires=">=3.7",
    project_urls={
        "Documentation": "https://github.com/qcnet/NYUAD-2023",
        "Source Code": "https://github.com/qcnet/NYUAD-2023",
        "Tutorials": "https://github.com/qcnet/NYUAD-2023/tree/master/tutorials",
    },
    include_package_data=True,
)
