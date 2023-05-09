.ONESHELL:
SHELL = /bin/bash

env:
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name final_proj_env --display-name "IPython - final_proj"

all:
	jupyter run main.ipynb DataCleaning.ipynb AgeGender.ipynb GreenSpaceVSHealth.ipynb MentalHealthVsEducation.ipynb PollutantsVsWellbeing.ipynb Modeling.ipynb
