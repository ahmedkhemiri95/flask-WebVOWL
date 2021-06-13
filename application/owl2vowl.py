import subprocess 
import os 
import shutil

def convert():

    # Run owl2vowl.jar converter : convert ontology file TTL to JSON format supported by WebVOWL
    proc = subprocess.Popen("java -jar ../application/static/owl2vowl.jar -file ../application/static/data/YOUR_ONTOLOGY.ttl", shell=True, stdout=subprocess.PIPE) 
    script_response = proc.stdout.read() 
    script_response=script_response.decode("utf-8")

    # Move generated JSON file to data dir 
    source = '../YOUR_ONTOLOGY.json' 
    destination = '../application/static/data/YOUR_ONTOLOGY.json'
    if os.path.exists(source):
     dest = shutil.move(source, destination) 
