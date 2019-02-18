# Placeholder for project virutalenv

Poetry respects this directory naming convention. Makes it easier for pycharm to find the right virtual environment.

```bash
$p poetry install # creates a virtualenv in .venv (?)
$p poetry run python -m venv .venv # create a virtualenv using poetry's python 
$p cat .venv/pyvenv.cfg
$p poetry shell
$p echo $VIRTUAL_ENV
$p echo $(git rev-parse --show-toplevel)/.venv  ## should be the same value? 
```