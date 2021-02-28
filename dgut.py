import requests
import urllib
import re
import json


class CasDgut:

    def __init__(self, login_url, username, password):
        self._session = requests.session()
        self._login_url = login_url
        self._username = username
        self._password = password

    @staticmethod
    def _get_token(response):
        text = response.text
        pattern = re.compile(r'var token = "(.*?)"')
        return pattern.findall(text)[0]

    @staticmethod
    def _get_cookie(response):
        pattern = re.compile(r'<Cookie (.*?) for.*?>')
        ckd = pattern.findall(str(response.cookies))
        return '; '.join(c for c in ckd)

    def login(self):
        sess = self._session

        response = sess.get(url=self._login_url)
        response.encoding = 'utf8'
        token = self._get_token(response)
        cookie = self._get_cookie(response)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.0.1583 Yowser/2.5 Safari/537.36',
            'Cookie': cookie,
        }

        data = {
            'username': self._username,
            'password': self._password,
            '__token__': token,
        }

        response = sess.post(url=self._login_url, data=data, headers=headers)
        if response.status_code == 200 and response.text.find('验证通过') != -1:
            text = response.text.replace('\\', '')[1:-1]
            pattern = re.compile(r'\"info\":\"(.*?)\"')
            url = pattern.findall(text)[0]

            return url
        return None


if __name__ == '__main__':
    urls = {
        'jwxt': 'https://cas.dgut.edu.cn/home/Oauth/getToken/appid/jwyd/state/home.html',
        'ehall': 'https://cas.dgut.edu.cn/home/Oauth/getToken/appid/ehall/state/home.html',
    }

    username = "学号"
    password = "密码"

    login_url = urls['jwxt']

    cas = CasDgut(login_url=login_url, username=username, password=password)
    home_url = cas.login()
    print('home url: ', home_url)

    sess = requests.session()

    '''
    Get Redirect Url
    '''
    response = sess.get(url=home_url)
    re_url = response.url
    print('redirect url: ', re_url)

    response = sess.get(url=re_url)
    text = response.text
    print('text: ', text)

    # '''
    # Get Access Token
    # 疫情防控打卡用
    # '''
    # params = urllib.parse.parse_qs(urllib.parse.urlparse(re_url).query)
    # access_token = params['access_token'][0]
    # print('access_token: ', access_token)
