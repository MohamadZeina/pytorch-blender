from setuptools import setup
from pathlib import Path

THISDIR = Path(__file__).parent

with open(THISDIR / "requirements.txt") as f:
    required = f.read().splitlines()

with open(THISDIR / ".." / "Readme.md", encoding="utf-8") as f:
    long_description = f.read()
print(required)

setup(
    name="blendtorch-btb",
    author="Christoph Heindl and Sebastian Zambal",
    description="Blender part of project blendtorch. See also blendtorch-btt.",
    url="https://github.com/cheind/pytorch-blender",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.4.0",
    packages=["blendtorch.btb"],
    install_requires=required,
    zip_safe=False,
)
