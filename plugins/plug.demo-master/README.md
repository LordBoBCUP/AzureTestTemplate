Plug Demo Module
================
This package acts as a "Hello World" module for Plug.  It provides functionality
for transferring tokens between accounts.

## Installation
Balance demo for Plug (and its dependencies) are currently hosted on a private repository,
so you will need to install directly from GitHub:

```bash
pipenv install -e git+ssh://git@github.com/plugblockchain/plug@master#egg=plug_framework
pipenv install -e git+ssh://git@github.com/plugblockchain/plug.demo@master#egg=plug_demo
```

## Testnet
If you would like to just run a network locally, clone this repo and install

```bash
pipenv install -e git+ssh://git@github.com/plugblockchain/plug@master#egg=plug_framework
pipenv install -e git+ssh://git@github.com/plugblockchain/plug.testnet@master#egg=plug_testnet

$ testnet ./config.yaml --dockerfile=./testnet/Dockerfile
```
