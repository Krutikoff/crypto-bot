"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_namespace_packages as find_packages

setup(
    name="crypto-bot",
    version="0.0.1",
    description="Crypto Bot",
    url="https://github.com/Krutikoff/crypto-bot",
    author="Krutikof",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["flask", "gunicorn"],
    extras_require={
        "dev": [
            "wemake-python-styleguide",
            "mypy",
            "black",
        ]
    },
    entry_points={"console_scripts": ["robster-bi = robster_bi.app:main"]},
)
