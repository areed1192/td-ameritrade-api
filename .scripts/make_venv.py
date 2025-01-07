"""Create a virtual environment in the current directory."""

import venv

venv.EnvBuilder(
    with_pip=True,
    system_site_packages=False,
    clear=True,
    symlinks=False,
    upgrade=True,
    upgrade_deps=True
).create(".schwab_env")