 # build_files.sh
pip install -r requirements.txt
python3 manage.py migrate 
python3 manage.py collectstatic