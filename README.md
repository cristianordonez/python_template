#ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOySzYGaU8FiLAmq9/kTKGqgU/ZKl53pbWg51F2otR94 cristianordonezrd@gmail.com
 <PROJECT_NAME>
Template repository for creating extendable and modern python cli and gui applications. Well documented configuration files so it can be edited to match projects needs.

## TODO

- install package

- run and configure test suite for python 3.12, 3.13, and 3.14

- set up argparse with debug, version arguments

- set up ty type checking and ruff

- set up pre commit

- containerize with docker

- set up github actions - lint, format, type check, build, test, deploy package to github packages

- create workflow to update version in __version__.py

- create workflow to change current version on pyproject.toml before build

- Update README.md



# Development

- System python is available at /usr/bin/python3

- Python shim created using pyenv is available at ~/.pyenv/shims. View all available shims with following command:

```bash
pyenv versions
```

- Virtual environments are managed with uv. Install new python versions with the following command:

```bash
uv python install <version>
```

- View all available uv managed python versions with the following command:

```bash
uv python list
```

- Install package locally

```bash
uv pip install -e .
```

- Update uv.lock

```bash
uv sync
```

- Run application

```bash
uv run python -m python-template
```

# Testing

- Install tox with uv

```bash
uv tool install tox --with tox-uv
```

# References

[uv](https://docs.astral.sh/uv/concepts/tools/#tool-versions)
[tox-uv](https://github.com/tox-dev/tox-uv)
[ruff](https://docs.astral.sh/ruff/)
[ty](https://docs.astral.sh/ty/)

- [Customization](https://code.visualstudio.com/docs/copilot/concepts/customization)
- [mcp-server](https://modelcontextprotocol.io/extensions/apps/build#manual-setup)