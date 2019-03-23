import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyLoRa",
    version="0.2.5",
    author="Rui Silva",
    author_email="ruisilva.real@sapo.pt",
    description="This is a python interface to the Ai-Thinker Ra-02 Modules LoRa long range, low power transceiver family. This module uses SX1278 IC and works on a 433MHz frequency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rpsreal/pySX127x",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Natural Language :: Portuguese",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ),
)
