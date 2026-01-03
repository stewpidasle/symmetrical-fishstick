"""Setup configuration for Local AI Assistant."""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="local-ai-assistant",
    version="0.1.0",
    author="Local AI Team",
    author_email="",
    description="A free, local AI assistant with coding, vision, voice, and automation capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stewpidasle/symmetrical-fishstick",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "local-ai=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.md"],
    },
)
