#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B68301 maqiang <maqiang626@qq.com> [2020-10-11 18:18 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 使用 requests 模拟登录石墨文档 https://shimo.im
# 作业更新：石墨文档有验证码，更换网站 https://processon.com
#
# ==================================================================
#

import requests
from fake_useragent import UserAgent
from time import sleep
import random


def login(url):
    try:
        ua = UserAgent(verify_ssl=False)
        headers = {
            'User-Agent': ua.random,
            'Referer': 'https://processon.com/login?f=index'
        }

        requests_session = requests.Session()

        login_url = 'https://processon.com/login'
        form_data = {
            'login_email': '139********',
            'login_password': '******'
        }

        response = requests_session.post(login_url, data=form_data,
                                         headers=headers)
        print('============================= login  =============================')
        print(response.text)
        sleep(random.randint(3, 9))

        # 登陆成功：账户中心
        setting_url = 'https://processon.com/setting'
        setting_response = requests_session.get(setting_url, headers=headers)
        print('============================ setting  ============================')
        print(setting_response.text)
        sleep(2)

    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == "__main__":
    login('https://processon.com')
