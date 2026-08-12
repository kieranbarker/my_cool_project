# Getting started

Assuming you are using PowerShell on Windows:

1. Create a virtual environment:
   - `py -m venv venv`
2. Activate the virtual environment:
   - `.\venv\Scripts\Activate.ps1`
3. Install the dependencies:
   - `pip install pandas pytest pytest-cov`
4. Run the tests and generate a coverage report:
   - `pytest --cov=helpers --cov-report=html`
5. View the coverage report:
   - Open `.\htmlcov\index.html` in your browser (open your browser and press <kbd>Ctrl</kbd> + <kbd>O</kbd>).
