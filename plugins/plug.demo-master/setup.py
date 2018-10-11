#!/usr/bin/env python
import setuptools


version = "1.0.1"

install_requires = (
    "plug_framework",
)

setuptools.setup(
    name="plug-demo",
    version=version,
    author="Plug Developers",
    author_email="developers@plug.uk",
    url="https://github.com/plugblockchain/plug.demo",
    packages=["plug_demo"],
    install_requires=install_requires,

    dependency_links=[
        "git+ssh://git@github.com/plugblockchain/plug@master#egg=plug_framework-0",
    ],
    extras_require={
        "test": (
            "asynctest",
            "pytest > 3.3.2",
            "pytest-aiohttp",
            "pytest-asyncio",
        ),
        "dev": (
            "flake8",
            "flake8-commas",
            "flake8-isort",
            "flake8-mypy",
            "flake8-quotes",
            "pytest-cov",
        ),
    },
)
