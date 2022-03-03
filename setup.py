import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ollivanders",
    version="0.0.1",
    author="nicolaujoan",
    author_email="joannicolau23@gmail.com",
    description="REST API with flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolaujoan/Ollivanders-Rest/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "aniso8601==9.0.1",
        "attrs==21.4.0",
        "click==8.0.4",
        "distlib==0.3.4",
        "filelock==3.6.0",
        "Flask==2.0.3",
        "Flask-RESTful==0.3.9",
        "iniconfig==1.1.1",
        "itsdangerous==2.1.0",
        "Jinja2==3.0.3",
        "MarkupSafe==2.1.0",
        "multipledispatch==0.6.0",
        "packaging==21.3",
        "platformdirs==2.5.1",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==3.0.7",
        "pytest==7.0.1",
        "pytz==2021.3",
        "six==1.16.0",
        "toml==0.10.2",
        "tomli==2.0.1",
        "tox==3.24.5",
        "virtualenv==20.13.2",
        "Werkzeug==2.0.3"
    ],
)