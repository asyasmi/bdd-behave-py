# bdd-behave-py

- Usage:
```
$ git clone https://github.com/zen-tools/bdd-behave-py.git
$ cd bdd-behave-py
~/bdd-behave-py$ virtualenv -p python venv
~/bdd-behave-py$ source venv/bin/activate
(venv)~/bdd-behave-py$ pip install -r requirements.txt
(venv)~/bdd-behave-py$ # Run tests on local machine
(venv)~/bdd-behave-py$ ./run.sh
(venv)~/bdd-behave-py$ # Run tests in docker container
(venv)~/bdd-behave-py$ docker run -d -p 4444:4444 --name=selenium-firefox selenium/standalone-firefox:2.50.0
(venv)~/bdd-behave-py$ GRID_HUB_URL="http://localhost:4444/wd/hub" BASE_URL="https://github.com" ./run.sh
```
