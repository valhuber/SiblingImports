# Sibling Imports

We love Python, but `import` statements can be... trying.

This project explores an approach, based on [this article](https://www.geeksforgeeks.org/python-import-from-sibling-directory/).  Thanks!

&nbsp;&nbsp;

## Using `__init__.py`

Works with or without.

&nbsp;&nbsp;

## Scenario 1 - run `run.py`

Works as documented above:
```
cd SiblingImports
python run.py
```
Or, launch configuration `Run`.

&nbsp;&nbsp;

## Scenario 2 - run `SiblingA/A.py`

Works like this:
```
cd SiblingA
python A.py
```
Or, launch `RunSiblingA` (which note - sets `cwd`)