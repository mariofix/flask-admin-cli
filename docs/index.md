# Flask Admin CLI

## Introduction

Flask Admin CLI is a command-line tool to manage Flask Admin examples. It provides commands to list original and available examples, clone a specific example repository, and perform pre-flight checks.

## Installation

To install Flask Admin CLI, use pip:

=== "Usando pip"
    ```shell
    pip install flask-admin-cli
    ```

=== "Usando poetry"
    ```shell
    poetry add flask-admin-cli
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

For more detailed information and documentation, visit the [Flask Admin CLI GitHub repository](https://github.com/mariofix/flask-admin-cli).

## Credits

Special thanks to the Flask Admin team for their fantastic work.
