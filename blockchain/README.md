**Activate the virual environment**

'''
souce blockchain/bin/activate
(conda) activate blockchain
'''

**Install all packages**
'''
pip3 install -r requirements.txt
(conda) conda install -r requirements.txt
'''

**Run the tests**

Make sure to activate the virtual environment.
'''
python -m pytest backend/tests
'''

**Run the application and API**
Make sure to activate the virtual environment.
'''
python -m backend.app
'''