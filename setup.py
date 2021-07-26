import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paypi",
    version="0.0.1",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
