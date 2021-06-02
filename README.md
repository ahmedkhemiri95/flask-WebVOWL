# flask-WebVOWL
WebVOWL integration As a flask application  -  OWL2VOWL converter is included.

# Running this app

1. install [python](https://www.python.org/) 
2. `git clone` the project then `cd` into the directory
3. run `virtualenv -p /usr/bin/python3 venv`or `python -m venv venv` to create a virtual environment
4. activate it using `source venv/bin/activate`
5. `pip install -r requirements.txt` to install the app libaries and it dependencies

# Usage

To convert and visualize your ontology file automatically :
* Rename your ontology file to "YOUR_ONTOLOGY.TTL" 
* Place it in data folder (application/static/data)

# IMPORTANT NOTE

To convert and visualize an ontology file with diffirent extenstions (RDF,OWL..):
* Please navigate to application/owl2vowl.py script and change the file extension.
* It's important to keep ontology file name to "YOUR_ONTOLOGY".



