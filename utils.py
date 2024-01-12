import configparser
import requests
import login
import bs4

CONF_FILE = "./config.ini"
cf = configparser.ConfigParser()
cf.read(CONF_FILE)  # 读取配置文件
userName = cf.get("accountConfig", "userName")
passWord = cf.get("accountConfig", "passWord")
base_url = cf.get("baseConfig", "baseUrl")
isEnglishCourse = cf.get("baseConfig", "isEnglishCourse")
print(base_url)
# lgn = login.Login(base_url=base_url)
# lgn.login(userName, passWord)  # 登陆

# Debug
cookie_str = "JSESSIONID=F91DE13CAA228B9852F594D19417276B; route=f426d7f9c4fca6b38279ec3fc13d7e6a"  # 字符串形式的的cookies
# cookie_str = lgn.cookies_str  # 字符串形式的的cookies
# print(cookie_str)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Cookie": cookie_str,
}
res = requests.get(
    base_url + "/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default",
    headers=headers,
)  # 发送请求，获得网页数据
res.encoding = "utf-8"  # 改变编码格式
web_content = res.text  # 获得网页内容
print(res.text)
soup = bs4.BeautifulSoup(web_content, "lxml")
# print(xkkz_id,xkxqm,xkxnm,njdm_id,zyh_id,kklxdm,xsbj)


def getHtmlconfig(soup, parameterName):
    try:
        return soup.find(id=parameterName).get("value")
    except:
        return 1


def getOtherXkkzId(soup, kklxdm):
    try:
        raw_attr = soup.find(id=kklxdm).get("onclick")
        param = raw_attr.split(",")[2].replace("'", "")
        return param
    except:
        return 1


class User(object):
    def __init__(self):
        Ck = cookie_str
        self.userName = cf.get("accountConfig", "userName")
        self.kklxdm = (
            cf.get("baseConfig", "kklxdm")
            if cf.get("baseConfig", "kklxdm") != "null"
            else getHtmlconfig(soup, "firstKklxdm")
        )
        self.xkxnm = (
            cf.get("baseConfig", "xkxnm")
            if cf.get("baseConfig", "xkxnm") != "null"
            else getHtmlconfig(soup, "xkxnm")
        )
        self.xkxqm = (
            cf.get("baseConfig", "xkxqm")
            if cf.get("baseConfig", "xkxqm") != "null"
            else getHtmlconfig(soup, "xkxqm")
        )
        self.njdm_id = (
            cf.get("baseConfig", "njdm_id")
            if cf.get("baseConfig", "njdm_id") != "null"
            else getHtmlconfig(soup, "njdm_id")
        )
        self.zyh_id = (
            cf.get("baseConfig", "zyh_id")
            if cf.get("baseConfig", "zyh_id") != "null"
            else getHtmlconfig(soup, "zyh_id")
        )
        self.xkkz_id = (
            cf.get("baseConfig", "xkkz_id")
            if cf.get("baseConfig", "xkkz_id") != "null"
            else getHtmlconfig(soup, "firstXkkzId")
        )
        self.ts_xkkz_id = (
            cf.get("baseConfig", "ts_xkkz_id")
            if cf.get("baseConfig", "xkkz_id") != "null"
            else getOtherXkkzId(soup, "tab_kklx_10")
        )
        self.ty_xkkz_id = (
            cf.get("baseConfig", "ty_xkkz_id")
            if cf.get("baseConfig", "xkkz_id") != "null"
            else getOtherXkkzId(soup, "tab_kklx_05")
        )
        self.xsbj = (
            cf.get("baseConfig", "xsbj")
            if cf.get("baseConfig", "xsbj") != "null"
            else getHtmlconfig(soup, "xsbj")
        )
        self.xqh_id = getHtmlconfig(soup, "xqh_id")
        self.jg_id = getHtmlconfig(soup, "jg_id_1")
        self.zyfx_id = getHtmlconfig(soup, "zyfx_id")
        self.bh_id = getHtmlconfig(soup, "bh_id")
        self.xbm = (
            cf.get("baseConfig", "xbm")
            if cf.get("baseConfig", "xbm") != "null"
            else getHtmlconfig(soup, "xbm")
        )
        self.xslbdm = getHtmlconfig(soup, "xslbdm")
        self.mzm = getHtmlconfig(soup, "mzm")
        self.xz = getHtmlconfig(soup, "xz")
        self.ccdm = getHtmlconfig(soup, "ccdm")
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Cookie": Ck,
        }

    def getCourseList(self, keyW, kklxdm):
        url = base_url + "/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html"
        if kklxdm != "05":
            if isEnglishCourse == "false":
                data = {
                    "xkxnm": self.xkxnm,
                    "xkxqm": self.xkxqm,
                    "kklxdm": kklxdm,
                    "kspage": 1,
                    "jspage": 20,
                    "yl_list[0]": 1,
                }
            else:
                data = {
                    "xkxnm": self.xkxnm,
                    "xkxqm": self.xkxqm,
                    "kklxdm": kklxdm,
                    "kspage": 1,
                    "jspage": 20,
                    "yl_list[0]": 1,
                    "xsbj": self.xsbj,
                    "xqh_id": "0",
                    "jg_id": "0",
                    "zyfx_id": "wfx",
                    "bh_id": "0",
                    "xbm": "0",
                    "xslbdm": "0",
                    "ccdm": "0",
                }
        else:
            data = {
                "rwlx": "2",
                "xkly": "0",
                "xqh_id": self.xqh_id,
                "jg_id": self.jg_id,
                "njdm_id": self.njdm_id,
                "zyh_id": self.zyh_id,
                "zyfx_id": self.zyfx_id,
                "bh_id": self.userName,
                "xbm": self.xbm,
                "xslbdm": self.xslbdm,
                "mzm": self.mzm,
                "xz": self.xz,
                "ccdm": self.ccdm,
                "xkxnm": self.xkxnm,
                "xkxqm": self.xkxqm,
                "kklxdm": kklxdm,
                "kspage": 1,
                "jspage": 20,
                "yl_list[0]": 1,
                "xsbj": self.xsbj,
            }
        if keyW != "":
            data["filter_list[0]"] = keyW
        req = requests.post(url, data, headers=self.header)
        print(req.text)
        return req.json()

    def getCourseDetail(self, kch, kklxdm, jxb_id):
        url = base_url + "/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html"
        if kklxdm != "05":
            if isEnglishCourse == "false":
                data = {
                    "bklx_id": 0,
                    "njdm_id": self.njdm_id,
                    "xkxnm": self.xkxnm,
                    "xkxqm": self.xkxqm,
                    "kklxdm": kklxdm or "01",
                    "kch_id": kch,
                    "xkkz_id": self.xkkz_id,
                    "rwlx": "1",
                    "xkly": "1",
                    "bh_id": self.userName,
                }
            else:
                data = {
                    "bklx_id": 0,
                    "njdm_id": self.njdm_id,
                    "xkxnm": self.xkxnm,
                    "xkxqm": self.xkxqm,
                    "kklxdm": kklxdm or "01",
                    "kch_id": kch,
                    "xkkz_id": self.xkkz_id,
                    "xsbj": self.xsbj,
                    "xqh_id": "0",
                    "jg_id": "0",
                    "zyfx_id": "wfx",
                    "bh_id": "0",
                    "xbm": "0",
                    "xslbdm": "0",
                    "ccdm": "0",
                    "rwlx": "1",
                    "xkly": "1",
                    "bh_id": self.userName,
                }
        else:
            data = {
                "rwlx": "2",
                "xkly": "0",
                "bklx_id": "0",
                "xqh_id": self.xqh_id,
                "jg_id": self.jg_id,
                "zyh_id": self.zyh_id,
                "zyfx_id": self.zyfx_id,
                "njdm_id": self.njdm_id,
                "bh_id": self.userName,
                "xbm": self.xbm,
                "xslbdm": self.xslbdm,
                "mzm": self.mzm,
                "xz": self.xz,
                "ccdm": self.ccdm,
                "xsbj": self.xsbj,
                "xkxnm": self.xkxnm,
                "xkxqm": self.xkxqm,
                "kklxdm": kklxdm,
                "kch_id": kch,
                "xkkz_id": self.ty_xkkz_id,
            }
        res = requests.post(url, data, headers=self.header).json()
        try:
            target = list(filter(lambda x: x["jxb_id"] == jxb_id, res))[0]
        except Exception as e:
            print(e)
            return res
        return target

    def getChoosedList(self):
        url = base_url + "/jwglxt/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html"
        data = {"xkxnm": self.xkxnm, "xkxqm": self.xkxqm}
        req = requests.post(url, data, headers=self.header)
        return req.json()

    def chooseCourse(self, jxb_ids, kch_id):
        url = base_url + "/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html"
        data = {
            "jxb_ids": jxb_ids,
            "kch_id": kch_id,
            "qz": 0,
            "njdm_id": self.njdm_id,
            "zyh_id": self.zyh_id,
        }
        req = requests.post(url, data, headers=self.header)
        return req.json()

    def quitCourse(self, jxb_ids):
        url = base_url + "/jwglxt/xsxk/zzxkyzb_tuikBcZzxkYzb.html?gnmkdm=N253512"
        data = {"jxb_ids": jxb_ids}
        req = requests.post(url, data, headers=self.header)
        return req.json()
