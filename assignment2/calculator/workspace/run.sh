# a) Install dependencies
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# b) Run all necessary parts of the codebase
# Run the application
python3 main.py &

# Run the test case
pytest test_calculator.py &
