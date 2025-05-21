find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
 
rm db.sqlite3
pip uninstall -y django
pip install django
pip install -r requirements.txt                             
python manage.py makemigrations
python manage.py migrate