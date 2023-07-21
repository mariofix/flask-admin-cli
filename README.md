# Flask Admin CLI

[![PyPI](https://img.shields.io/pypi/v/flask-admin-cli.svg)](https://pypi.org/project/flask-admin-cli/)
[![License](https://img.shields.io/pypi/l/flask-admin-cli.svg)](https://github.com/mariofix/flask-admin-cli/blob/master/LICENSE)
[![Test & Coverage](https://github.com/mariofix/flask-admin-cli/actions/workflows/test_and_coverage.yml/badge.svg?branch=main)](https://github.com/mariofix/flask-admin-cli/actions/workflows/test_and_coverage.yml)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-admin-cli)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/mariofix/flask-admin-cli/badge.svg?branch=main)](https://coveralls.io/github/mariofix/flask-admin-cli?branch=main)
![PyPI - License](https://img.shields.io/pypi/l/flask-admin-cli)

## Introduction

Flask Admin CLI is a command-line tool to manage Flask Admin examples. It provides commands to list original and available examples, clone a specific example repository, and perform pre-flight checks.

## Installation

To install Flask Admin CLI, use pip:

```shell
pip install flask-admin-cli
```

## Usage

### List Original Examples

To list all original Flask Admin examples along with their URLs and installation commands:

```shell
flask-admin-cli list_original_examples
```

### List Available Examples

To list all available Flask Admin examples along with their URLs and installation commands:

```shell
flask-admin-cli list_examples
```

### Clone Example Repository

To clone a specific Flask Admin example repository to the specified directory:

```shell
flask-admin-cli new_app --app example_name --dest_dir /path/to/destination
```

Replace `example_name` with the desired example (e.g., `appengine`, `auth`, `bootstrap4`, etc.) and provide the destination directory for installation.

## Documentation

For more detailed information and documentation, visit the [Flask Admin CLI Documentation](https://mariofix.github.io/flask-admin-cli).

## Credits

Special thanks to the Flask Admin team for their fantastic work.

## License

This project is licensed under the [MIT License](LICENSE).
