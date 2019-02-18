# Placeholder for project virutalenv

Poetry respects this directory naming convention. Makes it easier for pycharm to find the right virtual environment. You have to create the virtualenv first
however.

```bash
$p pyenv local 3.7.0 # or pyenv global
$p poetry run python -m venv .venv # populate a virtualenv using poetry's python 
$p cat .venv/pyvenv.cfg
$p poetry shell
$p echo $VIRTUAL_ENV
$p echo $(git rev-parse --show-toplevel)/.venv  ## should be the same value?
$p poetry update
$p poetry install
$p poetry -vvv show ## should show you ${VIRTUAL_ENV}
```

I might have this workflow wrong. It's a little confusing.