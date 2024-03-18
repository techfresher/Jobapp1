
set -o errexit

pip install -r requirements.txt

pip manage.py collectstatic --no-input
pythn manage.py migrate