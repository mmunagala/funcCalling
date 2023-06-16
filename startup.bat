@echo off

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Update virtual environments package manager
pip install --upgrade pip

REM Install the requirements
pip install -r requirements.txt

REM Run the FastAPI application using uvicorn
streamlit run main.py

