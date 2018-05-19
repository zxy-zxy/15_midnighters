# Night Owls Detector

A python script that lists students who provided their solutions between 12-00AM and 05-00AM. 
Script works with [Devman.org API](https://devman.org).

## Requirements
Python 3 should be already installed.
 Dependencies:

1.  [Requests library](http://docs.python-requests.org/en/master/)
2.  [Pytz](http://pytz.sourceforge.net/)
 
Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt
```
For better interaction is recommended to use [virtualenv](https://github.com/pypa/virtualenv).
### Example input
```bash
python seek_dev_nighters.py
```

### Example output


```bash
0: AndreyArakelyants
1: id311542249
2: fedya_kiselev
3: id215639888
4: nick__korolev
5: id185085967
6: dreamfall3r
7: id45197784
```

# Project Goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
