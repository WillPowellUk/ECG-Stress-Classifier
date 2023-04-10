# ECG Stress Classifier
The notebook `ECG Stress Classifier.ipynb` illustrates how stress was classified from ECG data using different Machine Learning methods. 

## Getting Started
Please try running `pip install -r requirements.txt` to load pip modules. If there are any pip related issues whilst running the notebook it is likely that your version of Python is not suitable. Please install Python Version 3.11.1. See below for details.

### Installing Python Version 3.11.1
If you have admin privaliges, please install from https://www.python.org/downloads/release/python-3111/ and save to PATH.
Otherwise, for non-root in linux please do the following steps:
    1. Download the Python source code from the official Python website, in this case Python 3.11.1: `wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz`
    2.  Extract the source code from the downloaded file: `tar xf Python-3.11.1.tar.xz`
    3. Configure the build. This will configure the build to install Python 3.11.1 to the HOME/local/python3.11 directory: `cd Python-3.11.1` and `./configure --prefix=$HOME/local/python3.11`
    4. Build and install Python: `make` and `make install`
    5. Add the Python binary directory to your PATH: `export PATH=$HOME/local/python3.11/bin:$PATH`

### Create VENV and Setup Requirements
1. In VScode: Ctrl-Shift-P and type `Python: Create Environment` and select `Venv`
2. If interpreter already in path please select it, otherwise click `Enter interpreter path...` and browse for the `Python3.11.1` directory and select the `Python` file.
3. For the requirements, select the requirements.txt file 
4. You should now have a virtual environment with Python 3.11.1 and the required pip modules installed.
