"""Setup script for CadQuery - A parametric 3D CAD scripting framework."""

from setuptools import setup, find_packages
import re
from pathlib import Path

# Read the README for the long description
this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text() if (this_dir / "README.md").exists() else ""

# Read version from cadquery/__init__.py
def get_version():
    init_path = this_dir / "cadquery" / "__init__.py"
    if init_path.exists():
        content = init_path.read_text()
        match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
        if match:
            return match.group(1)
    return "0.0.0"


setup(
    name="cadquery",
    version=get_version(),
    description="A parametric 3D CAD scripting framework based on OCCT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="CadQuery Contributors",
    url="https://github.com/CadQuery/cadquery",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests", "tests.*", "doc", "doc.*"]),
    python_requires=">=3.8",
    install_requires=[
        "pyparsing>=2.1.9",
        "typing_extensions>=3.7.4",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
            "sphinxcadquery",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
"Topic/Engineering",
    ="c cadquery, occt, opencascade, , parametric, modeling",
    project Reportsreadthedocs.io",
        "Source": "https://github.com/CadQuery/cadquery",
    },
)
