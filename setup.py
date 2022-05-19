from distutils.core import setup

with open("README.rst") as f:
    readme = f.read()

setup(
    name="java_syntax_kernel",
    version="0.1",
    packages=["java_syntax_kernel"],
    description="Restricted python kernel for Jupyter",
    long_description=readme,
    author="Tim Metzler",
    author_email="tim.metzler@h-brs.de",
    url="https://github.com/DigiKlausur/java_syntax_kernel",
    install_requires=["jupyter_client", "IPython", "ipykernel"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT",
        "Programming Language :: Python :: 3",
    ],
)
