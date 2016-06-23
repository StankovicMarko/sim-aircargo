import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from klase.login import Login

def test_checkCreds():
	user = Login('admin','admin')
	assert user.ID == "K#3"

def test_checkID():
	check = Login('nesto','nesto').checkID("nepostoji")
	assert check == (False,None)