# A TEST REPOSITORY
To help me learn about markdown, git, and GitHub 

This repository contains a script that can download an image using an url

## Before running the script YOU MUST...

### Clone the project 
![](https://i.ibb.co/LSthGhp/clone-1.gif)

	git clone https://github.com/NantawatLaothong/Git_Test_Project.git
	cd Git_Test_project
	
### Create a virtual environment	for the project and activate it
![](https://i.ibb.co/2WKbP3T/env.gif)

	python -m venv venv_name
	source venv_name/bin/activate
	
### Install Dependencies by...
![](https://i.ibb.co/DC9Zx77/deps.gif)

	pip install -r requirement.txt

## Two ways to run img_downloader
![](https://i.ibb.co/pvWdmZ2/run2134.gif)

	python main.py url filename
	# or
	./main.py url filename 
	# sample 
	./main.py https://images-na.ssl-images-amazon.com/images/I/91XPrGekxbL.jpg ghibli.jpg 


