import configparser
import requests
import login
import bs4

CONF_FILE = './config.ini'
cf = configparser.ConfigParser()
cf.read(CONF_FILE)  # 读取配置文件
userName = cf.get("accountConfig", "userName")
passWord = cf.get('accountConfig', "passWord")
base_url = cf.get('baseConfig', "baseUrl")
isEnglishCourse = cf.get('baseConfig', "isEnglishCourse")
print(base_url)
# lgn = login.Login(base_url=base_url)
# lgn.login(userName, passWord)  # 登陆

cookie_str = "JSESSIONID=DF94DD907C7C98085709F0321AB5C100; route=a7740d479b99ac200742596ec5b9ce98"  # 字符串形式的的cookies
# print(cookie_str)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Cookie': cookie_str}
res = requests.get(base_url+'/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default',
                   headers=headers)  # 发送请求，获得网页数据
res.encoding = 'utf-8'  # 改变编码格式
web_content = res.text  # 获得网页内容
soup = bs4.BeautifulSoup(web_content, 'lxml')
# print(xkkz_id,xkxqm,xkxnm,njdm_id,zyh_id,kklxdm,xsbj)


def getHtmlconfig(soup, parameterName):
    try:
        return soup.find(id=parameterName).get("value")
    except:
        return 1


class User(object):
    def __init__(self):
        Ck = cookie_str
        self.userName = cf.get("accountConfig", "userName")
        self.kklxdm = cf.get("baseConfig", "kklxdm") if cf.get(
            "baseConfig", "kklxdm") != 'null' else getHtmlconfig(soup, 'firstKklxdm')
        self.xkxnm = cf.get("baseConfig", "xkxnm") if cf.get(
            "baseConfig", "xkxnm") != 'null' else getHtmlconfig(soup, 'xkxnm')
        self.xkxqm = cf.get("baseConfig", "xkxqm") if cf.get(
            "baseConfig", "xkxqm") != 'null' else getHtmlconfig(soup, 'xkxqm')
        self.njdm_id = cf.get("baseConfig", "njdm_id") if cf.get(
            "baseConfig", "njdm_id") != 'null' else getHtmlconfig(soup, 'njdm_id')
        self.zyh_id = cf.get("baseConfig", "zyh_id") if cf.get(
            "baseConfig", "zyh_id") != 'null' else getHtmlconfig(soup, 'zyh_id')
        self.xkkz_id = cf.get("baseConfig", "xkkz_id") if cf.get(
            "baseConfig", "xkkz_id") != 'null' else getHtmlconfig(soup, 'firstXkkzId')
        self.xsbj = cf.get("baseConfig", "xsbj") if cf.get(
            "baseConfig", "xsbj") != 'null' else getHtmlconfig(soup, 'xsbj')
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Cookie': Ck
        }

    def getCourseList(self, keyW):
        url = base_url+'/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html'
        if isEnglishCourse == 'false':
            data = {'xkxnm': self.xkxnm, 'xkxqm': self.xkxqm,
                    'kklxdm': self.kklxdm, 'kspage': 1, 'jspage': 20, 'yl_list[0]': 1}
        else:
            data = {'xkxnm': self.xkxnm, 'xkxqm': self.xkxqm, 'kklxdm': self.kklxdm, 'kspage': 1, 'jspage': 20, 'yl_list[0]': 1,
                    'xsbj': self.xsbj, 'xqh_id': '0', 'jg_id': '0', 'zyfx_id': 'wfx', 'bh_id': '0', 'xbm': '0', 'xslbdm': '0', 'ccdm': '0'}
        if keyW != "":
            data['filter_list[0]'] = keyW
        req = requests.post(url, data, headers=self.header)
        print(req.text)
        return (req.json())

    def getCourseDetail(self, kch):
        url = base_url+'/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html'
        if isEnglishCourse == 'false':
            data = {'bklx_id': 0, 'njdm_id': self.njdm_id, 'xkxnm': self.xkxnm,
                    'xkxqm': self.xkxqm, 'kklxdm': self.kklxdm, 'kch_id': kch, 'xkkz_id': self.xkkz_id, 'rwlx': '1', 'xkly': '1', 'bh_id': self.userName}
        else:
            data = {'bklx_id': 0, 'njdm_id': self.njdm_id, 'xkxnm': self.xkxnm, 'xkxqm': self.xkxqm, 'kklxdm': self.kklxdm, 'kch_id': kch, 'xkkz_id': self.xkkz_id,
                    'xsbj': self.xsbj, 'xqh_id': '0', 'jg_id': '0', 'zyfx_id': 'wfx', 'bh_id': '0', 'xbm': '0', 'xslbdm': '0', 'ccdm': '0', 'rwlx': '1', 'xkly': '1', 'bh_id': self.userName}
        req = requests.post(url, data, headers=self.header)
        return (req.json())

    def getChoosedList(self):
        url = base_url+'/jwglxt/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html'
        data = {'xkxnm': self.xkxnm, 'xkxqm': self.xkxqm}
        req = requests.post(url, data, headers=self.header)
        return (req.json())

    def chooseCourse(self, jxb_ids, kch_id):
        url = base_url+'/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html'
        data = {'jxb_ids': jxb_ids, 'kch_id': kch_id, 'qz': 0,
                'njdm_id': self.njdm_id, 'zyh_id': self.zyh_id}
        req = requests.post(url, data, headers=self.header)
        return (req.json())

    def quitCourse(self, jxb_ids):
        url = base_url+'/jwglxt/xsxk/zzxkyzb_tuikBcZzxkYzb.html?gnmkdm=N253512'
        data = {'jxb_ids': jxb_ids}
        req = requests.post(url, data, headers=self.header)
        print(req.json())
        if req.json() == '1':
            url = base_url+'/jwglxt/xsxk/zzxkyzb_xkBcZypxZzxkYzb.html?gnmkdm=N253512'
            data = {'zypxs': "", "jxb_ids": ""}
            req = requests.post(url, data, headers=self.header)
            print(req.text)
            return req.json()
        return (req.json())
