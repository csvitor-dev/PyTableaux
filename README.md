# PyTableaux | **Tableaux** solver with _**Python**_

Just clone this repository and run the following command in the project root:
(make sure the **Python** version is `3.12.1`)

```bash
pip install -r ./requirements.txt
```

To insert an input file, simpley enter the following in the terminal:

```bash
python main.py < ./inputs/example.tab
```

This example file will generate the following output:

```bash
{'((a->b)&(b->c))': True, 'a': True, 'c': False}
```