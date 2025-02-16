python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install pipenv

pipenv install django

git clone https://github.com/simoare732/recibook.git
rm .\recibook\Pipfil*
mv .\recibook\* .
Remove-Item -Path ".\recibook" -Recurse -Force
cd project
pipenv run pip install -r requirments.txt