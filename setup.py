# setup.py
from setuptools import setup, find_packages

setup(
    name="bigvgan",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # mirror what's in requirements.txt
        "torch",
        "numpy",
        "librosa",
        "scipy",
        "matplotlib",
        "tensorboard",
        "soundfile",
        "pesq",
        "matplotlib",
        "auraloss",
        "tqdm",
        "nnAudio",
        "ninja",
        "huggingface_hub",
        # …etc.
    ],
)
