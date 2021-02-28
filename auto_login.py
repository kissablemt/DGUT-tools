import requests
import time

url = 'http://172.31.252.91/eportal/InterFace.do?method=login'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '929',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'EPORTAL_COOKIE_OPERATORPWD=; JSESSIONID=0D45BEE3E8BFE7DE2D8C47C4A9B5575D',
    'Host': '172.31.252.91',
    'Origin': 'http://172.31.252.91',
    'Referer': 'http://172.31.252.91/eportal/index.jsp?wlanuserip=faba438720caa80bff44a0ce7773aec4&wlanacname=806f067db62e57c4a344eb08f5250b13&ssid=&nasip=bbf96d75fd8987ff0566955248aabfaa&snmpagentip=&mac=47190d8daf03f88ab3f35dd7e818c988&t=wireless-v2&url=709db9dc9ce334aa02a9e1ee58ba6fcf3bc3349e947ead368bdd021b808fdbac30c65edaa96b0727&apmac=&nasid=806f067db62e57c4a344eb08f5250b13&vid=8273c53a3fdabbda&port=2043de32fb4c99e5&nasportid=5b9da5b08a53a540871303b4f6662eb2450597a31c7f31e2f564754d744422ecfb12fee87fab2ee1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1760 Yowser/2.5 Safari/537.36',
}

# 具体data可能要抓包
data = {
    'userId': '学号',
    'password': '抓包  一串很长加密过的字符串',
    'service': '',
    'queryString': 'wlanuserip%3Dfaba438720caa80bff44a0ce7773aec4%26wlanacname%3D806f067db62e57c4a344eb08f5250b13%26ssid%3D%26nasip%3Dbbf96d75fd8987ff0566955248aabfaa%26snmpagentip%3D%26mac%3D47190d8daf03f88ab3f35dd7e818c988%26t%3Dwireless-v2%26url%3D709db9dc9ce334aa02a9e1ee58ba6fcf3bc3349e947ead368bdd021b808fdbac30c65edaa96b0727%26apmac%3D%26nasid%3D806f067db62e57c4a344eb08f5250b13%26vid%3D8273c53a3fdabbda%26port%3D2043de32fb4c99e5%26nasportid%3D5b9da5b08a53a540871303b4f6662eb2450597a31c7f31e2f564754d744422ecfb12fee87fab2ee1',
    'operatorPwd': '',
    'operatorUserId': '',
    'validcode': '',
    'passwordEncrypt': 'true',
}


if __name__ == '__main__':
    while True:
        succ = False
        try:
            res = requests.post(url=url, headers=headers, data=data)
            if res.status_code == 200:
                succ = True
    
        except Exception as e:
            err = e
            print(e)
            pass

        finally:
            with open("/home/pi/Documents/py_code/dgut/network_login/logs.txt", 'a+') as f:
                localtime = time.asctime(time.localtime(time.time()))
                print('{}: '.format(localtime), end='')
                f.write('{}: '.format(localtime))
                if succ:
                    print('登录成功')
                    f.write('登陆成功\n')
                else:
                    print('登录失败，稍后重试')
                    f.write('登录失败，稍后重试\n')
                    f.write('{}\n'.format(err))
                f.write("\n")
        time.sleep(30)

