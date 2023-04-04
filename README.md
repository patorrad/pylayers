# PyLayers 
This is a fork of pylayes for use in the NASA DGCR Project

# Installation
Clone this repo and follow these installation instructions. These instructions worked for Ubuntu 20.04.5 LTS.

conda create --name pylayers python=3.5 \
conda activate pylayers
cd pylayers
pip install -r requirements.txt
pip install mayavi==4.8.0
pip install basemap==1.3.6
pip install osmapi==2.0.2
pip install geocoder==1.38.1
pip install -e .

# Test installation
cd pylayers
python dlinkeval.py 
