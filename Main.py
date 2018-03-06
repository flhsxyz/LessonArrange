from manage import *
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''实例化'''
    l = myLogin()
    c1 = myControl_1()
    c2 = myControl_2()
    c3 = myControl_3()
    ins = myInputStudent()
    inc = myInputClass()
    inte = myInputTeacher()
    sch = mySchedule()
    per = myPeriod()
    subg = mySubjectGroup()
    addg = myAddGroup()
    lect = myLecture()
    less = myLesson()
    qless = myQueryLesson()

    '''显示登录界面'''
    l.show()
    '''跳转不同身份对应控制界面'''
    l.close_signal_1.connect(c1.show)
    l.close_signal_2.connect(c2.show)
    l.close_signal_3.connect(c3.show)

    '''教师页面'''
    c1.change1_sign.connect(inc.show)
    c1.change2_sign.connect(ins.show)
    c1.change3_sign.connect(inte.show)
    c1.change4_sign.connect(l.show)

    inc.return_sign.connect(c1.show)
    ins.return_sign.connect(c1.show)
    inte.return_sign.connect(c1.show)

    '''学科组长页面'''
    c2.change1_sign.connect(lect.show)
    c2.change2_sign.connect(less.show)
    c2.change3_sign.connect(qless.show)
    c2.change4_sign.connect(l.show)

    less.return_sign.connect(c2.show)
    lect.return_sign.connect(c2.show)
    qless.return_sign.connect(c2.show)

    '''教导主任页面'''
    c3.change1_sign.connect(sch.show)
    c3.change2_sign.connect(per.show)
    c3.change3_sign.connect(subg.show)
    c3.change4_sign.connect(l.show)

    sch.return_sign.connect(c3.show)
    per.return_sign.connect(c3.show)
    subg.return_sign.connect(c3.show)
    subg.addGroup_sign.connect(addg.show)

    app.exec_()

