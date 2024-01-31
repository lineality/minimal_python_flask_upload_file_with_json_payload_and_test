# check python version: 
```bash
python --version
python3 --version
python3.11 --version
```

# check github branch
```bash
git branch
git status
```

# to build:
```bash
python3.11 -m venv env; source env/bin/activate
python3.11 -m pip install --upgrade pip; python3.11 -m pip install -r requirements.txt
```

# Optional Notebook Install
```bash
python3.11 -m pip install jupyter
```

# to run flask server:
```bash
python3.11 app.py
```
# to run test-module: (run in a new terminal, also in env) 
```python
python3.11 req_test.py
```

# to evaluate success
1. Look in the uploads_should_be_here folder/directory, see if the uploaded file is there.
2. Look at terminal output. (e.g. 200 OK or error)
