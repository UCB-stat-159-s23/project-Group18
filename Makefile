.ONESHELL:
SHELL = /bin/bash

.PHONY: env
env:
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name final_proj_env --display-name "IPython - final_proj"

.PHONY: all
all:
	jupyter run code/*
	jupyter run main.ipynb

.PHONY: html
html:
	jupyter-book build.