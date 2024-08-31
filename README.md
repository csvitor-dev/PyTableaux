# PyTableaux | Tableaux solver with _Python_

Before anything else, set up your _**Python**_ environment (`venv`) with the follwing command in the current folder:

The first step is to install the version of _**Python**_ used in the project, which is contained in the file `.python-version`:

```bash
pyenv install
```

Now create the environment using this installed version:

```bash
pyenv virtualenv <py_version> <env_name>
pyenv activate <env_name>
```

And install the dependencies:

```bash
pip install --require-virtualenv -r ./requirements.txt
```

To insert an input file, simpley enter the following in the terminal:

```bash
python main.py < ./inputs/example.tab
```

This example file will generate the following output:

```bash
{'((a->b)&(b->c))': True, 'a': True, 'c': False}
```
