python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install pipenv

rm Pipfil*
pipenv install django

cd project
pipenv run pip install -r requirments.txt