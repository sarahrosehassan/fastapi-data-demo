@echo off
echo Setting up Tech Products API...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo.
echo Setup complete!
echo To start the server, run: start.bat
