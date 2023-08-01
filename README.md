# Qathir | كثير

<p align="center">
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=code-status&message=Good&color=orange"/>
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=initial-commit&message=Shantanu&color=inactive"/>
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=maintainer&message=qathir&color=inactive"/>
</p>


<!-- **Documentation**: TODO -->

## Motivation

By leveraging our quantum-enhanced end-to-end solution for cost-efficient sensor placement and rapid fault and vulnerability localization, qathir enables the robust and efficient use of the increasingly complex water distribution networks of tomorrow.

Please check out our [presentation](https://docs.google.com/presentation/d/e/2PACX-1vRwLkgCpkB5gSSmqP016QIRihLcBpB13e0bkr3gk_eS7b2I5p0nWXYEDG7E5tB5AnMWsFPpO7QcXLCa/pub?start=false&loop=false&delayms=3000) from NYUAD Hack 2023 to learn more about this project. 

## Installation

*Conda users, please make sure to `conda install pip` before running any pip installation if you want to install `qathir` into your conda environment.*

`qathir` may soon be published on PyPI. Once it is, simply run the following code to install the package:

```bash
pip install qathir
```
If you also want to download the dependencies needed to run optional tutorials, please use `pip install qathir[dev]` or `pip install 'qathir[dev]'` (for `zsh` users).


To check if the installation was successful, run:

```bash
python -c "import qathir"
```

This should execute silently if installation was successful.

## Building from source

To build `qathir` from source, pip install using:

```bash
git clone git@github.com:qcnet/NYUAD-2023.git qathir
cd team-13/qathir
pip install --upgrade .
```

If you also want to download the dependencies needed to run optional tutorials, please use `pip install --upgrade .[dev]` or `pip install --upgrade '.[dev]'` (for `zsh` users).

#### Installation for Devs

If you intend to contribute to this project, please install `qathir` in editable mode as follows:
```bash
git clone git@github.com:qcnet/NYUAD-2023.git qathir
cd team-13/qathir
pip install -e .[dev]
```

Please use `pip install -e '.[dev]'` if you are a `zsh` user.

Installing the package in the usual non-editable mode would require a developer to upgrade their pip installation (i.e. run `pip install --upgrade .`) every time they update the package source code.

## Documentation

<!-- Documentation should be -->

#### View locally


To view documentation locally, please open `docs/build/html/index.html` in your browser.


#### Build documentation 

To rebuild documentation, please start in the root folder and run:

```sh
cd docs
make clean
make html
```

*You may also have to delete the `docs/source/_autosummary` directory before running the above commands.*


## Acknowledgements

**Core Devs:** Anubhav Shrestha, Deepesh Garg, Dhruv Srinivasan, Dilyara Sharipova, Oyungerel Amarsanaa, Samhitha Bharthulwar, Sasha, Shantanu Jha, Tasnim Ahmed, Yeji Han


This project was created by the qathir team at NYUAD Hack 2023.

