from csv import excel
import utils


def courseList(keyW, kklxdm='01'):
    print('正在进行课程查询...')
    CourseList = User.getCourseList(keyW, kklxdm).get('tmpList')
    i = 0
    for item in CourseList:
        print('---------------------------------------------------')
        print(str(i)+":"+item["jxbmc"]+"-"+item["kcmc"])
        print('   '+item["kzmc"]+'\t'+item['xf']+'学分'+'\t'+item['yxzrs']+'人已选')
        kch_ids.append({'id': item["kch_id"], 'name': item["jxbmc"]})
        i = i+1
    print('---------------------------------------------------')


if __name__ == '__main__':
    try:
        User = utils.User()
        print(1)
    except Exception as e:
        print(e)
        input()
    print('''
    *********************************
    欢迎使用【HDU抢课小助手】
    功能代码如下:
    ---------------------
    1.选主修课
    2.选通识选修课
    3.选体育课
    4.已选课程查询
    5.退课
    
    ---------------------
    ps:【】内的值为功能代码
    *********************************''')
    code = input('\n请输入功能代码(-1 退出系统):')
    while (code != '-1'):
        if code == '1':
            print('进入选主修课功能')
            kch_ids = []
            keyW = input("请输入要查询的课程关键字(为空则返回全部结果):")
            courseList(keyW)
            if kch_ids != []:
                toChooseId = int(input("请输入要选择的课程名字前的序号(-1退出选课):"))
                if toChooseId in range(0, len(kch_ids)):
                    ifChoose = input(
                        "确认选择课程 "+kch_ids[toChooseId]['name']+"? (Y/n,默认Y):")
                    if (ifChoose != 'n'):
                        kch_id = kch_ids[toChooseId]['id']
                        Detail = User.getCourseDetail(kch_id)
                        if Detail == '0':
                            print('课程具体获取失败！')
                        else:
                            jxb_ids = Detail[0]['do_jxb_id']
                            res = User.chooseCourse(jxb_ids, kch_id)
                            if res['flag'] == '1':
                                print("选课成功！")
                            else:
                                print(res['msg'])
            else:
                print('未找到课程/该课程名额已满')
        elif code == '2':
            print('进入选通识选修课功能')
            kch_ids = []
            keyW = input("请输入要查询的课程关键字(为空则返回全部结果):")
            courseList(keyW, '10')
            if kch_ids != []:
                toChooseId = int(input("请输入要选择的课程名字前的序号(-1退出选课):"))
                if toChooseId in range(0, len(kch_ids)):
                    ifChoose = input(
                        "确认选择课程 "+kch_ids[toChooseId]['name']+"? (Y/n,默认Y):")
                    if (ifChoose != 'n'):
                        kch_id = kch_ids[toChooseId]['id']
                        Detail = User.getCourseDetail(kch_id, '10')
                        if Detail == '0':
                            print('课程具体获取失败！')
                        else:
                            jxb_ids = Detail[0]['do_jxb_id']
                            res = User.chooseCourse(jxb_ids, kch_id)
                            if res['flag'] == '1':
                                print("选课成功！")
                            else:
                                print(res['msg'])
            else:
                print('未找到课程/该课程名额已满')
        elif code == '3':
            print('进入选体育课功能')
            kch_ids = []
            keyW = input("请输入要查询的课程关键字(为空则返回全部结果):")
            courseList(keyW, '05')
            if kch_ids != []:
                toChooseId = int(input("请输入要选择的课程名字前的序号(-1退出选课):"))
                if toChooseId in range(0, len(kch_ids)):
                    ifChoose = input(
                        "确认选择课程 "+kch_ids[toChooseId]['name']+"? (Y/n,默认Y):")
                    if (ifChoose != 'n'):
                        kch_id = kch_ids[toChooseId]['id']
                        Detail = User.getCourseDetail(kch_id, '05')
                        print(Detail)
                        if Detail == '0':
                            print('课程具体获取失败！')
                        else:
                            jxb_ids = Detail[0]['do_jxb_id']
                            res = User.chooseCourse(jxb_ids, kch_id)
                            if res['flag'] == '1':
                                print("选课成功！")
                            else:
                                print(res['msg'])
            else:
                print('未找到课程/该课程名额已满')
        elif code == '4':
            print('正在进行已选课程查询...')
            choosedList = User.getChoosedList()
            i = 1
            for item in choosedList:
                print('---------------------------------------------------')
                print(str(i)+":"+item["jxbmc"])
                i = i+1
            print('---------------------------------------------------')
        elif code == '5':
            kch_ids = []
            print('正在进行已选课程查询...')
            choosedList = User.getChoosedList()
            i = 0
            for item in choosedList:
                print('---------------------------------------------------')
                print(str(i)+":"+item["jxbmc"])
                kch_ids.append({'id': item["kch_id"], 'name': item["jxbmc"]})
                i = i+1
            print('---------------------------------------------------')
            if kch_ids != []:
                toQuitId = int(input("请输入要退选的课程名字前的序号(-1退出选课):"))
                if toQuitId in range(0, len(kch_ids)):
                    ifChoose = input(
                        "确认退选课程 "+kch_ids[toQuitId]['name']+"? (yes/N,默认N):")
                    if (ifChoose == 'yes'):
                        kch_id = kch_ids[toQuitId]['id']
                        print(kch_id)
                        Detail = User.getCourseDetail(kch_id)
                        if Detail == '0':
                            print('课程具体获取失败！')
                        else:
                            jxb_ids = Detail[0]['do_jxb_id']
                            res = User.quitCourse(jxb_ids)
                            if res == 'success':
                                print('退课成功')
                            else:
                                print(res)
        code = input('请输入功能代码(-1 退出系统):')
