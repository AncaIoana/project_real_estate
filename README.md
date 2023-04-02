GENERAL INFO: 
Project: https://www.sspaeti.com/blog/data-engineering-project-in-twenty-minutes/ 

GETTING STARTED:
1. Check if you have `pip`: `pip –version` 
If not,install `pip`: 
- download source file: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` 
- then run: `python get-pip.py 

2. Pyenv
Install pyenv  to manage  Python versions on the computer: https://towardsdatascience.com/how-to-use-manage-multiple-python-versions-on-an-apple-silicon-m1-mac-d69ee6ed0250
- Install python version 3.10.10: `pyenv install 3.10.10` 
- Set it up as local for this project: `pyenv local 3.10.10`

3. Pipenv
Create a virtual environment using Pipenv.
- Install Pipenv: `brew install pipenv` or `pip install --user pipenv`
- Create an empty directory called `.venv` (this will add all venv specific to this directory)
- Create virtual environment + download all  dependencies: `pipenv install` (you can now select it as an interpreter)
- Activate virtual environment: `pipenv shell`
- To exit virtual environment: `exit` or `deactivate`
- To run script: `pipenv run python3 myscript.py` (sometimes it needs full path)

4. Other Pipenv commands:
- To add any other new Python package: `pipenv install <package_name>` / `pipenv install <package_name=version_number>`
- To delete the virtual environment: `pipenv --rm`
- To view installed dependencies in the virtual environment: `pipenv graph` or `pipenv run pip freeze`
- To uninstall packages in the virtual environment: `pipenv uninstall <package_name>`

DOCUMENTATION: 
Pyenv and Pipenv: 
https://www.rootstrap.com/blog/how-to-manage-your-python-projects-with-pipenv-pyenv
https://pipenv-fork.readthedocs.io/en/latest/basics.html

Beautiful Soup documentation:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Web scraping with Beautiful  Soup: 
https://www.youtube.com/watch?v=gRLHr664tXA 
https://www.youtube.com/@worthwebscraping-mike6107 


