import imaplib
import time
from .. import flask

IMAP_SERVER = 'webmail.nitt.edu'

# Add remaining dept code
DEPARTMENTS = {6: 'CSE', 10: 'ICE', 12: 'META', 14:'PROD', 11:'MECH', 7:'EEE',8:'ECE', 2:'CHEM', 3:'CIVIL', 1:'ARCHI'}


def process_username(username):
    if '@' in username:
        username = username.split('@')[0]
    return username


def imap_login(username, password):
    try:
        imap = imaplib.IMAP4(IMAP_SERVER)
        login = imap.login(username, password)
        success = login[0]
        return success == 'OK'
    except:
        return False


def parse_username(username):
    cur_year = int(time.ctime().split(" ")[-1][2:])
    grad_year = int(username[4:6])
    year = cur_year - grad_year
    dept_num = int(username[1:3])
    try:
        dept = DEPARTMENTS[dept_num]
    except KeyError:
        dept = 'CSE'
    return year, dept


def server_login(username, password):
    year = None
    dept = None
    logged_in = False
    try:
        username = process_username(username)
        logged_in = imap_login(username, password)
        year, dept = parse_username(username)
        # Yet to test the session.
        #flask.session['rollnumber'] = username
        #flask.session['year'] = year
        #flask.session['dept'] = dept
    except:
         logged_in = False
    finally:
        return (logged_in,year,dept)

print server_login('106112091', 'sriramwebmail')
