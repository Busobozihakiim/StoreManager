@echo off
echo to use admin endpoint enter admin
echo to use attendants endpoint enter attendant
SET /P user= Please enter your choice:

IF %user% == admin (
set FLASK_APP=app\apiv1\admin.py
python -m flask run
)
IF %user% == attendant (
set FLASK_APP=app\apiv1\attendant.py
python -m flask run
)
