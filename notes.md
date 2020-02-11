step 0:
		.gitignore      --> .env

step 1:
		virtualenv .env -p python3

step 2:
		source .env/bin/activate

step 3:
		pip3 install flask

step 4:
		pip3 freeze > requirements.txt