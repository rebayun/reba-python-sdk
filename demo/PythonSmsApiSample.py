# encoding=utf8
import requests
requests.packages.urllib3.disable_warnings()
"""
以下代码展示的是非sdk下的调用，只是为了方便用户测试而提供的样例代码，用户也可自行编写。
正式环境建议使用sdk进行调用以提高效率，sdk中包含了使用样例
代码中额外使用了Requests库
"""
def post_json(url, json):
    response = requests.post(url, verify=False, json=json, timeout=5)
    if response.status_code != 200:
        raise Exception('Http request error, status code: {}'.format(response.status_code))
    return response.json()

print post_json('https://sms.rebayun.com/api/sms/batchSubmit', {
    'apikey': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  # 修改为您的apikey
    'submits': [{
        'mobile': '186xxxxxxxx',  # 修改为您要发送的手机号
        'message': '【热巴云通讯】您的验证码是：123456'  # 修改为您要发送的内容，内容必须和某个模板匹配
    }]
})