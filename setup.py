import os

from setuptools import setup

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="oura-to-sqlite",
    description="Download your data from oura to a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Andreas Madsack",
    url="https://github.com/mfa/oura-to-sqlite",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["oura_to_sqlite"],
    entry_points="""
        [console_scripts]
        oura-to-sqlite=oura_to_sqlite.cli:cli
    """,
    install_requires=["sqlite-utils~=3.17.1", "click", "oura"],
    extras_require={"test": ["pytest"], "lint": ["black", "isort"]},
    tests_require=["oura-to-sqlite[test]"],
)
