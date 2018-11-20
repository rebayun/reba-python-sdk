# encoding=utf8

import json
from reba.api import *

server_url = 'https://sms.rebayun.com/api'
#此处为你的apikey，可登录https://web.rebayun.com/ 查看你的apikey
apikey = '2f9c56d6cf944539b4f9891d8ceb3f61'
client = RebaClient(server_url, apikey)


def test_sms_batch_submit():
    try:
        response = client.sms_batch_submit([
            {'mobile': '176xxxxxxxx', 'message': '【热巴云通讯】您的验证码是：1234'},
            {'mobile': '186xxxxxxxx', 'message': '【热巴云通讯】您的验证码是：5678'}
        ])
        print json.dumps(response)
    except RebaApiError as e:
        print 'RebaApiError. code: {0}, message: {1}'.format(e.code, e.message.encode('utf8'))
    except Exception as e:
        print 'Unexpected error. ' + e.message


def test_sms_pull_status_report():
    try:
        response = client.sms_pull_status_report()
        print json.dumps(response)
    except RebaApiError as e:
        print 'RebaApiError. code: {0}, message: {1}'.format(e.code, e.message.encode('utf8'))
    except Exception as e:
        print 'Unexpected error.' + e.message


def test_sms_pull_reply_message():
    try:
        response = client.sms_pull_reply_message()
        print json.dumps(response)
    except RebaApiError as e:
        print 'RebaApiError. code: {0}, message: {1}'.format(e.code, e.message.encode('utf8'))
    except Exception as e:
        print 'Unexpected error.' + e.message


test_sms_batch_submit()
