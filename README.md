# <PROJECT_NAME>
Template repository for creating extendable and modern python cli and gui applications. Well documented configuration files so it can be edited to match projects needs.

## TODO

- finish setting up uv and creating virtual env

- install package

- run and configure test suite for python 3.12, 3.13, and 3.14

- set up argparse with debug, version arguments

- set up ty type checking and ruff

- set up pre commit

- containerize with docker

- set up github actions - lint, format, type check, build, test, deploy package to github packages
- create workflow to change current version on pyproject.toml before build



# Development

- System python is available at /usr/bin/python3.12

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

- Install editable package

```bash
uv pip install -e .
```

- Run template app

```bash
uv run jarvis
```

# References

[uv](https://docs.astral.sh/uv/concepts/tools/#tool-versions)

# References

- [Customization](https://code.visualstudio.com/docs/copilot/concepts/customization)
- [mcp-server](https://modelcontextprotocol.io/extensions/apps/build#manual-setup)