# MachineLearningAndArchitecture

The file "scraper.py" in "./src" can be run to scrape the links to each item on the Bloomingdales website. The output of this script is a file with the source URL for each category followed by the URLs for each item (seperated by page) this will appear in "/.src/data"

to setup the venv run 
virtualenv --system-site-packages -p python3 venv 

then run 
pip install -r ./src/req.txt

also 
mkdir src/data
