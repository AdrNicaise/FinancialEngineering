p install -r requirements.txt

source .env/bin/activate

FILE=file.py

if test -f "$FILE"; then
	echo "$FILE exists."
	#!/bin/sh
	python3 "file.py"
fi
