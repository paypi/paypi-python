import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paypi",
    version="1.0.8",
    author="PayPI",
    author_email="hello@paypi.dev",
    description=" Official PayPI Partner Library ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paypi/paypi-python",
    project_urls={
        "Bug Tracker": "https://github.com/paypi/paypi-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "paypi"},
    packages=setuptools.find_packages(where="paypi"),
    python_requires=">=3.6",
)
