# Rest API Automation using pytest framework, python3, requests and pytest-html for reporting

Tested on:
------------------
Pytest 6.2.5

Python 3.10.0

pytest-html 3.1.1

requests 2.26.0

Required installations:
--------------------
Install python3 from following website for your machine architecture.

Python 3  -> https://www.python.org/downloads/

Install required dependencies using pip once python is installed.

Checkout the repository and navigate to base repository folder and then run below command.

pip install -r requirements.txt

Running Tests Commands:
----------------------
Go to base checkout directory and run below commands:

1. Set PATH:

set PATH=C:\<python_install_dir>\Scripts;

2. set PYTHONPATH:

set PYTHONPATH=C:\<python_install_dir>\Lib\site-packages;D:\<repo_checkout_dir>;

These paths are for Windows machine specific, you can run respective commands for other platforms.

3. Execute all tests 
    $ pytest -s --html=logs\Report.html --self-contained-html --capture sys

4. To execute test cases with specific marker: Below command will execute only test cases which are marked as p0
    $ pytest -s --html=logs\Report.html --self-contained-html --capture sys -m p0

![alt text](https://raw.githubusercontent.com/yuvrajkpatil/APIAutomation/master/images/console.png)

![alt text](https://raw.githubusercontent.com/yuvrajkpatil/APIAutomation/master/images/logs.png)


Extra Information/Libraries/Updates/Documentations/Tools:
-------------------------------------------------------

https://robotframework.org/