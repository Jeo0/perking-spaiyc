# Installation Instructions

this is referenced from *[electronstudio](https://electronstudio.github.io/raylib-python-cffi/README.html#installation)*<br>
if checking that isnt an option, then pls do these:

1. install latest python (any 3.12.x) in ur system <br>
    *[python on windows](https://www.python.org/downloads/windows/)*

    > *note for more advanced users (not a mandatory procedure): use conda to handle the python and pip installation [link to miniconda](https://docs.anaconda.com/miniconda/install/)*
    >
	> presummably, you are in x64 bit windows;
	> make sure to check the **"add python.exe to your PATH"** then install now.

<br>

1.1 if all goes well, open up powershell and run. It should output Python 3.12 or something

``` python --version ``` 

<br>

2. install the required packages using pip

    - setuptools
    - pyray

<br>

2.1 open up powershell and have the updated packages from pip

``` python -m pip install --upgrade pip ```

<br>

2.2  install the mentioned packages: 

``` python -m pip install setuptools raylib==5.5.0.0 ```

<br>

------------------

# Getting Started

1. with the zip project extracted on your desktop or anywhere you want, navigate into the src folder with the Change Directory command (cd): <br>

	``` cd "Path\To\Your\Desktop\or\anywhere\you\want\ProjectFolder\src\" ```

<br> 

2. run this command to run the game:

	``` python main.py ```


<br> 

-----------------
# Note to professor:

All commits past the 16th does not reflect with wat I have passed to you. To continue the things that I wanted to see, I resumed pushing features. 

For better distinction, all future commits will be labeled as "pogi" by prefix.
