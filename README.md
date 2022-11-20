# Unbabel cli
Hi 👋, I'm João and welcome to my solution! 

This is a simple command line application that parses a stream of events and produces an aggregated output. In this case, we're instered in calculating, for every minute, a moving average of the translation delivery time for the last X minutes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install unbabel-cli.

Create a Virtual Environment (Optional)

```bash
python3 -m venv <venv-name>
```
or
```bash
make virtualenv
```

Install Requirements

```bash
pip3 install -r requirements.txt
```
or
```bash
make local-init
```

## Usage

```python
cd cli
python unbabel_cli.py
```

## Example
```
python unbabel_cli.py --input_file ../data/inputs/input.json  --window_size 10`
```

## Run tests
```
cd cli
python -m pytest tests
```

or
```
make local-test
```