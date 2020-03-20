#!/bin/bash -e

# Installs nbgrader. Should be run inside the Docker container.

cd /srv/src/nbgrader

pip install .

jupyter nbextension install --symlink --sys-prefix --py nbgrader
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader

cd -

cd /kubespawner_service_jupyterhub
pip install .

# Then start jupyterhub

cd -
jupyterhub
