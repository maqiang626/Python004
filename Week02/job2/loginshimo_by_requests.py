#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B48101 maqiang <maqiang626@qq.com> [2020-10-11 18:16 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 使用 requests 模拟登录石墨文档 https://shimo.im
#
# ==================================================================
#

import requests
from fake_useragent import UserAgent
from time import sleep


def login(url):
    try:
        ua = UserAgent(verify_ssl=False)
        headers = {
            'User-Agent': ua.random,
            'Referer': 'https://shimo.im/login?from=home'
        }

        requests_session = requests.Session()
        login_url = 'https://shimo.im/lizard-api/auth/password/login'
        form_data = {
            'mobile': '13913103557',
            'password': '******'
        }

        response = requests_session.post(login_url, data=form_data,
                                         headers=headers)

        # 出现验证码，需手动验证通过：卡住
        print('============================= login  =============================')
        print(response.text)
        sleep(56)

        # 登陆成功：最近使用
        used_url = 'https://shimo.im/dashboard/used'
        used_response = requests_session.get(used_url, headers=headers)
        print('============================== used ==============================')
        print(used_response.text)
        sleep(2)

    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == "__main__":
    login('https://shimo.im/')


# ========================== MQDEBUG INFO ==========================
# ============================= login  =============================
# CSRF violation
#
