#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B58201 maqiang <maqiang626@qq.com> [2020-10-11 18:16 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 使用 Selenium 模拟登录石墨文档 https://shimo.im
# 作业更新：石墨文档有验证码，更换网站 https://processon.com
#
# ==================================================================
#

from selenium import webdriver
from time import sleep
import random


def login(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        sleep(5)

        # 首页 - 登录 (链接)
        browser.find_element_by_link_text('登录').click()
        sleep(6)

        # 请输入邮箱地址或者手机号码
        browser.find_element_by_id('login_email').send_keys('13913103557')
        sleep(random.randint(1, 3))

        # 请输入密码
        browser.find_element_by_id('login_password').send_keys('Ilov1You*PR')
        sleep(random.randint(1, 3))

        # 立即登录
        browser.find_element_by_id('signin_btn').click()
        sleep(26)

    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == "__main__":
    login('https://processon.com')
