# 杭州电子科技大学抢课小助手

本脚本暂时处于测试版阶段，还未经过实测，待更新。

🎈 代码修改，以及请求参数配置具体详见:<a href='https://github.com/shaxiu/ZF_API'>正方教务选课系统 API 分析文档</a>

---

#### 安装库

`pip3 install configparser`

`pip3 install requests`

`pip3 install rsa`

`pip3 install bs4`

`pip3 install pycryptodome`

## 脚本配置

```
[accountConfig]
userName=用户名(学号)
passWord=密码
[baseConfig]
baseUrl = https://newjw.hdu.edu.cn
xkkz_id = null
kklxdm=null
xkxnm=null
xkxqm=null
njdm_id=null
zyh_id=null
isEnglishCourse=false
```

**基础玩法**

- 将 `config.ini` 与软件脚本放于同一目录下
- 将配置文件中的 `userName` `passWord` 改为自己的用户名和密码
- 将 `baseUrl` 改为学校教学管理平台对应域名地址
- 若是拓展英语课程，将 `isEnglishCourse` 参数改为 `true`（未经测试，俺也不知道管不管用）
- 其他参数无需更改

**进阶玩法**

- 若学校进行分年级分时段选 选修课，例如 19 级可以进行选课而作为 20 级的你无法选课/只可以选主修课
- 你可以通过修改参数~~欺骗后台~~ ，~~假装自己是 19 级的~~
- 修改 `njdm_id` 如 `2020` -> ` 2019`
- 修改 `kklxdm` ：`01`为主修课 `10` 为选修课 `07`为拓展英语课 ps:每个学校不同，仅供参考
- 修改 `xkkz_id`：该参数可以找对应有权限选课的高年级/低年级同学要，每一轮次选课固定
- 其他参数配置具体详见:<a href='https://github.com/shaxiu/ZF_API'>正方教务选课系统 API 分析文档</a>

## <span id="jump">卡 bug 的简易方法</span>

注：方法主要针对分年级分时段选课，未到时间的用户无法进入通识选修课的界面的问题(前提是用户可正常进入主修课选课界面)

- F12 查看网页代码，将 `id='kklxdm'` 的 input 框的 `value` 改为 `10`

  其中`10`对应通识选修课，`01`对应主修课选课

- 修改完成后点击搜索，发现课程列表出现通识选修课，但无法正常点击展开课程进行选课

- 将 `id='xkkz_id'` 的 input 框的 value 改为 `D8243C19A3C0239AE0530264A8C00F27`(动态值,以具体情况为准)

- 将`id='njdm_id'`的 input 框的 value 值改为允许现在选网课的年级如`2018`

- 再次点击课程，发现可以正常展开并进行选课

## <span id="jump">特别鸣谢</span>

- <a href='https://github.com/shaxiu/ZF_API'>正方教务选课系统 API 分析文档</a>

- <a href='https://github.com/shaxiu/njtech_grabber'>南京工业大学抢课小助手</a>
