#!/usr/bin/python
# << 代码作者：HUNX04（HunxByts）
# << 想重写/魔改？？请先征得许可，至少请标注作者本人的 GitHub 账号指向本仓库；更简单的做法是直接 Fork
# << 若不遵守以上约定，作者可不答应——毕竟别人未经允许拿走你的劳动成果，你也不会甘心
# “信道的人们啊！你们不要借诈术而侵蚀别人的财产。”（《古兰经》4:29）先知同样禁止穆斯林未经允许拿走他人的权利。（原注释引文，中文仅为意译）

# IMPORT MODULE

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # 终端颜色变量
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# 工具函数

# 装饰器：调用函数前先刷新运行横幅
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# 菜单功能函数
@is_option
def IP_Track():
    ip = input(f"{Wh}\n 输入目标 IP：{Gr}")  # 输入 IP 地址
    print()
    print(f' {Wh}============= {Gr}IP 地址信息查询结果 {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API：IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n 目标 IP         :{Gr}", ip)
    print(f"{Wh} IP 类型         :{Gr}", ip_data["type"])
    print(f"{Wh} 国家            :{Gr}", ip_data["country"])
    print(f"{Wh} 国家代码        :{Gr}", ip_data["country_code"])
    print(f"{Wh} 城市            :{Gr}", ip_data["city"])
    print(f"{Wh} 大洲            :{Gr}", ip_data["continent"])
    print(f"{Wh} 大洲代码        :{Gr}", ip_data["continent_code"])
    print(f"{Wh} 地区            :{Gr}", ip_data["region"])
    print(f"{Wh} 地区代码        :{Gr}", ip_data["region_code"])
    print(f"{Wh} 纬度            :{Gr}", ip_data["latitude"])
    print(f"{Wh} 经度            :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} 地图            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} 欧盟成员        :{Gr}", ip_data["is_eu"])
    print(f"{Wh} 邮编            :{Gr}", ip_data["postal"])
    print(f"{Wh} 电话区号        :{Gr}", ip_data["calling_code"])
    print(f"{Wh} 首都            :{Gr}", ip_data["capital"])
    print(f"{Wh} 接壤国家        :{Gr}", ip_data["borders"])
    print(f"{Wh} 国旗            :{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} 组织            :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} 运营商          :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} 域名            :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} 夏令时          :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} 当前时间        :{Gr}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}输入目标手机号 {Gr}示例 [+6281xxxxxxxxx] {Wh}：{Gr}")  # 输入手机号
    default_region = "ID"  # 默认国家：印度尼西亚

    parsed_number = phonenumbers.parse(User_phone, default_region)  # phonenumbers 解析变量
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}手机号信息查询结果 {Wh}==========")
    print(f"\n {Wh}归属地               :{Gr} {location}")
    print(f" {Wh}地区代码             :{Gr} {region_code}")
    print(f" {Wh}时区                 :{Gr} {timezoneF}")
    print(f" {Wh}运营商               :{Gr} {jenis_provider}")
    print(f" {Wh}号码有效             :{Gr} {is_valid_number}")
    print(f" {Wh}格式可能             :{Gr} {is_possible_number}")
    print(f" {Wh}国际格式             :{Gr} {formatted_number}")
    print(f" {Wh}手机拨号格式         :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}原始号码             :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}国家区号             :{Gr} {parsed_number.country_code}")
    print(f" {Wh}本地号码             :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}号码类型             :{Gr} 这是一个手机号码")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}号码类型             :{Gr} 这是一个固定电话号码")
    else:
        print(f" {Wh}号码类型             :{Gr} 这是其他类型的号码")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}输入目标用户名：{Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}未找到该用户名 {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}用户名信息查询结果 {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}本机 IP 信息查询结果 {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] 本机 IP 地址     : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP 追踪',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': '显示本机 IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': '手机号追踪',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': '用户名追踪',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': '退出',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('选项不存在')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('未检测到对应功能')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}按回车键继续')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}已退出')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # 工具横幅
    clear()
    stderr.writelines(f"""
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_| 

              {Wh}[ + ]  C O D E   B Y  H U N X  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o    `.        {Wh}|       {Gr}@CODE BY HUNXBYTS      {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}请选择选项：{Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}请输入数字')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}已退出')
        time.sleep(2)
        exit()
