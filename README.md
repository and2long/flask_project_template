# Flask Project Template
Flask 项目模版

### Setup

#### Prerequisites
1. Install direnv
Follow instructions at https://direnv.net/docs/installation.html. For mac it will be something like: `brew install direnv`
2. Install Python 3.12
Recommend installing asdf (https://github.com/asdf-vm/asdf) or similar and running `asdf install python 3.12.8`
3. Make sure you have docker and docker-compose installed
You can use instructions at https://github.com/abiosoft/colima to getting up and running with colima if you're on mac

#### Install dependencies and setup local environment
```bash
# 0. Any time you change .envrc you'll have to re-run this to give direnv permission to load new values into your environment
direnv allow

# 1. Create a virtual environment
python3 -m venv venv

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. database setup
flask db init
flask db migrate
flask db upgrade
```

### Run locally
`flask run --debug`
