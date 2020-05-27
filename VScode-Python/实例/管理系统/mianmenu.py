# @Author  : Fizzyi
import regist
import land

def mainmenu():
    #主界面
    while True:
        print(''''
            ---- 欢迎 ----
            1.登陆
            2.注册
            3.退出
        ''')
        order = input('请输入：')
        if order == '1':
            ##进入登录界面
            land.landing()
        elif order == '2':
            #进入注册界面
            regist.regist_menu()
        else:
            #退出程序
            break
if __name__ == '__main__':
    stu_id = 0
    mainmenu()