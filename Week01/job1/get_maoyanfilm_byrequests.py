#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B07801 maqiang <maqiang626@qq.com> [2020-09-27 21:09 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 1. 安装并使用 requests、bs4 库
# 2. 爬取猫眼电影的前 10 个电影名称、电影类型和上映时间
# 3. 并以 UTF-8 字符集保存到 csv 格式的文件中
# 4. 猫眼电影网址： https://maoyan.com/films?showType=3
#
# ==================================================================
#

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd


def get_movie_info(url):
    # Debug
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    #     "Cookie": '__mta=212219179.1600751835177.1600753641060.1600753785431.6; uuid_n_v=v1; uuid=DE4378D0FC9211EA985FDD1498D583AFFE4C6E81C55549B7805FDE1B3E0207C0; _csrf=5c8fbe3f38dc1a03dcbb381432c8e552ba12db8f3b475133ad4090aa6a907cbe; _lxsdk_cuid=174b43e86f3c8-095a87dc195b04-333769-100200-174b43e86f4c8; _lxsdk=DE4378D0FC9211EA985FDD1498D583AFFE4C6E81C55549B7805FDE1B3E0207C0; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1600751831; mojo-uuid=f217dd963702b7549b66d24c8fb1d745; __mta=212219179.1600751835177.1600751835177.1600752190255.2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1600753785; _lxsdk_s=174b509dced-dac-249-62d%7C%7C1'
    # }

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    bs_info = bs(response.text, 'html.parser')

    # Debug
    print('==================================================================')
    print(f'01 返回值：{response.text}')
    print(f'02 返回码：{response.status_code}')

    movie_info = {"serial_number": ["序号"], "movie_name": ["电影名称"],
                  "movie_type": ["电影类型"], "movie_releasetime": ["上映时间"]}
    count = 0

    # 汇总每个电影的所有信息
    for movie_data in bs_info.find_all('div', attrs={"class": "movie-hover-info"}, limit=10):
        divs = movie_data.find_all('div', attrs={"class": "movie-hover-title"})
        movie_name = divs[0].find('span', attrs={"class": "name"}).text.strip()
        movie_type = divs[1].text.strip().split()[1].strip()
        movie_releasetime = divs[3].text.strip().split()[1].strip()

        count += 1

        # Debug
        print('--------------------------------------------------------')
        print(f'03 电影信息：{count} {movie_name} {movie_type} {movie_releasetime}')

        movie_info["serial_number"].append(count)
        movie_info["movie_name"].append(movie_name)
        movie_info["movie_type"].append(movie_type)
        movie_info["movie_releasetime"].append(movie_releasetime)

        sleep(5)

    movie = pd.DataFrame(data=movie_info)

    # encoding (Linux: utf8 / Windows: gbk)
    movie.to_csv('./maoyanmovie_20200927.csv', encoding='utf8',
                 index=False, header=False)


# main
if __name__ == "__main__":
    get_movie_info('https://maoyan.com/films?showType=3')
