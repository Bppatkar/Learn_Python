# Python Virtual Environment Cheatsheet

## Create a new virtual environment

```bash
python -m venv env_name
```

## Install packages

```bash
pip install package_name
```

## Save installed packages to a file

```bash
pip freeze > requirements.txt
```

or

```bash
pip list --format=freeze > requirements.txt
```

## Install packages from a file

```bash
pip install -r requirements.txt
```

## Deactivate the current virtual environment

```bash
deactivate
```

## In Linux or Mac, activate the new python environment

```bash
source env_name/bin/activate
```

## Or in Windows

```bash
.\env_name\Scripts\activate
```
