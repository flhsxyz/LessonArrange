from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Login(QMainWindow):

    def __init__(self):
        super().__init__()

        '''用户名部分'''
        self.username = QLabel('用户名', self)
        self.username.move(110, 70)
        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.setGeometry(170, 70, 120, 30)

        '''密码部分'''
        self.password = QLabel('密码', self)
        self.password.move(115, 130)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setGeometry(170, 130, 120, 30)

        self.btn1 = QPushButton('登录',self)
        self.btn2 = QPushButton('取消',self)
        self.btn1.move(100, 220)
        self.btn2.move(250, 220)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('排课系统-欢迎登录')
        self.center()

    '''窗口居中'''
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Control_1(QDialog):
    def __init__(self):
        super().__init__()

        self.title = QLabel('教师登录，有以下选择：', self)
        self.title.setGeometry(250, 50, 300, 100)
        self.title.setFont(QFont("", 15, QFont.Bold))

        self.btn1 = QPushButton('录入班级', self)
        self.btn1.setGeometry(220, 150, 150, 50)
        self.btn1.setFont(QFont("", 15, QFont.Bold))

        self.btn2 = QPushButton('录入学生', self)
        self.btn2.setGeometry(400, 150, 150, 50)
        self.btn2.setFont(QFont("", 15, QFont.Bold))

        self.btn3 = QPushButton('录入教师', self)
        self.btn3.setGeometry(220, 220, 150, 50)
        self.btn3.setFont(QFont("", 15, QFont.Bold))

        self.btn4 = QPushButton('退出登录', self)
        self.btn4.setGeometry(400, 220, 150, 50)
        self.btn4.setFont(QFont("", 15, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-教师')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Control_2(QDialog):
    def __init__(self):
        super().__init__()

        self.title = QLabel('学科组长登录，有以下选择：', self)
        self.title.setGeometry(230, 50, 350, 100)
        self.title.setFont(QFont("", 15, QFont.Bold))

        self.btn1 = QPushButton('安排教师', self)
        self.btn1.setGeometry(220, 150, 150, 50)
        self.btn1.setFont(QFont("", 15, QFont.Bold))

        self.btn2 = QPushButton('排课', self)
        self.btn2.setGeometry(400, 150, 150, 50)
        self.btn2.setFont(QFont("", 15, QFont.Bold))

        self.btn3 = QPushButton('查看课表', self)
        self.btn3.setGeometry(220, 220, 150, 50)
        self.btn3.setFont(QFont("", 15, QFont.Bold))

        self.btn4 = QPushButton('退出登录', self)
        self.btn4.setGeometry(400, 220, 150, 50)
        self.btn4.setFont(QFont("", 15, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-教师')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Control_3(QDialog):
    def __init__(self):
        super().__init__()

        self.title = QLabel('教导主任登录，有以下选择：', self)
        self.title.setGeometry(230, 50, 350, 100)
        self.title.setFont(QFont("", 15, QFont.Bold))

        self.btn1 = QPushButton('安排节次', self)
        self.btn1.setGeometry(220, 150, 150, 50)
        self.btn1.setFont(QFont("", 15, QFont.Bold))

        self.btn2 = QPushButton('安排课时', self)
        self.btn2.setGeometry(400, 150, 150, 50)
        self.btn2.setFont(QFont("", 15, QFont.Bold))

        self.btn3 = QPushButton('设置学科组', self)
        self.btn3.setGeometry(220, 220, 150, 50)
        self.btn3.setFont(QFont("", 15, QFont.Bold))

        self.btn4 = QPushButton('退出登录', self)
        self.btn4.setGeometry(400, 220, 150, 50)
        self.btn4.setFont(QFont("", 15, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-教师')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class InputClass(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel('录入班级', self)
        self.title.setGeometry(320, 10, 200, 100)
        self.title.setFont(QFont("", 20, QFont.Bold))

        '''学部'''
        self.section = QLabel('学部：', self)
        self.section.setGeometry(130, 120, 80, 30)
        self.sectionComboBox = QComboBox(self)
        self.sectionComboBox.insertItem(1, self.tr('初中部'))
        self.sectionComboBox.insertItem(2, self.tr('高中部'))
        self.sectionComboBox.setGeometry(200, 120, 150, 30)

        '''年级'''
        self.grade = QLabel('年级：', self)
        self.grade.setGeometry(130, 170, 80, 30)
        self.gradeComboBox = QComboBox(self)
        self.gradeComboBox.insertItem(1, self.tr('一年级'))
        self.gradeComboBox.insertItem(2, self.tr('二年级'))
        self.gradeComboBox.insertItem(3, self.tr('三年级'))
        self.gradeComboBox.setGeometry(200, 170, 150, 30)

        '''班级名称'''
        self.name = QLabel('班级：', self)
        self.name.setGeometry(130, 220, 80, 30)
        self.nameEdit = QLineEdit(self)
        self.nameEdit.setPlaceholderText('填写数字即可')
        self.nameEdit.setGeometry(200, 220, 150, 30)

        '''教室'''
        self.classroom = QLabel('教室：', self)
        self.classroom.setGeometry(130, 270, 80, 30)
        self.classroomEdit = QLineEdit(self)
        self.classroomEdit.setPlaceholderText('1-101')
        self.classroomEdit.setGeometry(200, 270, 150, 30)

        '''提交按钮'''
        self.submit = QPushButton('提交', self)
        self.submit.move(220, 330)

        '''输出框'''
        self.info = QTextBrowser(self)
        self.info.setGeometry(400, 120, 300, 225)

        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.setGeometry(320, 400, 150, 40)
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-录入班级')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class InputStudent(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel('录入学生', self)
        title.setGeometry(320, 10, 200, 100)
        title.setFont(QFont("", 20, QFont.Bold))

        '''学生名称'''
        self.name = QLabel('学生姓名：', self)
        self.name.setGeometry(100, 150, 80, 30)
        self.nameEdit = QLineEdit(self)
        self.nameEdit.setGeometry(200, 150, 150, 30)

        '''性别'''
        self.sex = QLabel('性别：', self)
        self.sex.setGeometry(130, 200, 80, 30)
        self.sexbtn1 = QRadioButton('男' ,self)
        self.sexbtn1.setGeometry(200, 200, 50, 30)
        self.sexbtn2 = QRadioButton('女', self)
        self.sexbtn2.setGeometry(275, 200, 50, 30)

        '''班级'''
        self.classname = QLabel('班级：', self)
        self.classname.setGeometry(130, 250, 80, 30)
        self.classnameBox = QComboBox(self)
        self.classnameBox.setGeometry(200, 250, 150, 30)

        '''提交按钮'''
        self.submit = QPushButton('提交', self)
        self.submit.move(200, 300)

        self.info = QTextBrowser(self)
        self.info.setGeometry(400, 150, 300, 200)

        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.setGeometry(320, 380, 150, 40)
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-录入学生')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class InputTeacher(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel('录入教师', self)
        self.title.setGeometry(320, 10, 200, 100)
        self.title.setFont(QFont("", 20, QFont.Bold))

        '''教师姓名'''
        self.name = QLabel('教师姓名：', self)
        self.name.setGeometry(100, 150, 80, 30)
        self.nameEdit = QLineEdit(self)
        self.nameEdit.setGeometry(200, 150, 150, 30)

        self.subject = QLabel('教授学科：', self)
        self.subject.setGeometry(100, 220, 80, 30)
        self.subjectEdit = QLineEdit(self)
        self.subjectEdit.setPlaceholderText('语文、数学...')
        self.subjectEdit.setGeometry(200, 220, 150, 30)

        '''提交按钮'''
        self.submit = QPushButton('提交', self)
        self.submit.move(200, 300)

        '''输出框'''
        self.info = QTextBrowser(self)
        self.info.setGeometry(400, 150, 300, 200)

        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.setGeometry(320, 380, 150, 40)
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-录入教师')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Period(QWidget):
    def __init__(self):
        super().__init__()

        '''选择学部'''
        self.section = QLabel('学部：', self)
        self.section.setGeometry(280, 30, 50, 30)
        self.sectionComboBox = QComboBox(self)
        self.sectionComboBox.insertItem(1, self.tr('初中部'))
        self.sectionComboBox.insertItem(2, self.tr('高中部'))
        self.sectionComboBox.setGeometry(340, 30, 150, 30)

        '''增加/删除节次按钮'''
        self.add = QPushButton('增加课程', self)
        self.add.move(630, 150)
        self.remove = QPushButton('删除课程', self)
        self.remove.move(630, 200)
        self.submit = QPushButton('提交课时表', self)
        self.submit.move(630, 250)
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.move(630, 300)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(4)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setFont(QFont("", 12))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['课程编号','课程名称','课时数'])
        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-安排课时')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Schedule(QWidget):
    def __init__(self):
        super().__init__()

        '''选择学部'''
        self.section = QLabel('学部：', self)
        self.section.setGeometry(280, 30, 50, 30)
        self.sectionComboBox = QComboBox(self)
        self.sectionComboBox.insertItem(1, self.tr('初中部'))
        self.sectionComboBox.insertItem(2, self.tr('高中部'))
        self.sectionComboBox.setGeometry(340, 30, 150, 30)

        '''增加/删除节次按钮'''
        self.add = QPushButton('增加节次', self)
        self.add.move(630, 150)
        self.remove = QPushButton('删除节次', self)
        self.remove.move(630, 200)
        self.submit = QPushButton('提交节次表', self)
        self.submit.move(630, 250)
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.move(630, 300)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(8)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setFont(QFont("", 12))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['节次','上课时间','下课时间'])
        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        for i in range(12):
            self.table.setItem(i, 0, QTableWidgetItem('第%s节课' % str(i+1)))

        '''添加删除按钮操作'''
        self.add.clicked.connect(lambda :self.addRow())
        self.remove.clicked.connect(lambda: self.removeRow())

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-安排节次')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addRow(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem('第%s节课' % str(row_count + 1)))

    def removeRow(self):
        row_count = self.table.rowCount()
        self.table.removeRow(row_count-1)

class SubjectGroup(QWidget):
    def __init__(self):
        super().__init__()

        '''增加/删除节次按钮'''
        self.addGroup = QPushButton('增加学科组', self)
        self.addGroup.move(630, 150)
        self.refresh = QPushButton('刷新数据', self)
        self.refresh.move(630, 200)
        self.submit = QPushButton('提交表格', self)
        self.submit.move(630, 250)
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.move(630, 300)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(12)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setFont(QFont("", 12))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['学科','所属学科组'])

        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-设置学科组')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class AddGroup(QDialog):
    def __init__(self):
        super().__init__()
        self.subLabel = QLabel('学科组名称：', self)
        self.subLabel.setGeometry(100, 50, 100, 30)
        self.subLineEdit = QLineEdit(self)
        self.subLineEdit.setGeometry(200, 50, 150, 30)
        self.leaderLabel = QLabel('学科组长：', self)
        self.leaderLabel.setGeometry(113, 120, 100, 30)
        self.leaderComboBox = QComboBox(self)
        self.leaderComboBox.setGeometry(200, 120, 150, 30)
        self.addButton = QPushButton('增加学科组', self)
        self.addButton.setGeometry(210, 190, 100, 30)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('排课系统-教师')
        self.center()
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Lecture(QWidget):
    def __init__(self):
        super().__init__()

        '''学期'''
        self.semesterLabel = QLabel('学期：', self)
        self.semesterLabel.setGeometry(70, 30, 50, 30)
        self.semesterLineEdit = QLineEdit(self)
        self.semesterLineEdit.setGeometry(120, 30, 100, 30)

        '''选择学部'''
        self.section = QLabel('学部：', self)
        self.section.setGeometry(270, 30, 50, 30)
        self.sectionComboBox = QComboBox(self)
        self.sectionComboBox.insertItem(1, self.tr('初中部'))
        self.sectionComboBox.insertItem(2, self.tr('高中部'))
        self.sectionComboBox.setGeometry(320, 30, 100, 30)

        '''学科'''
        self.subjectLabel = QLabel('学科：', self)
        self.subjectLabel.setGeometry(470, 30, 50, 30)
        self.subjectComboBox = QComboBox(self)
        self.subjectComboBox.setGeometry(520, 30, 100, 30)

        '''更新'''
        self.updatebtn = QPushButton('更新', self)
        self.updatebtn.setGeometry(670, 30, 100, 30)

        '''增加/删除节次按钮'''
        self.submit = QPushButton('提交表格', self)
        self.submit.move(250, 450)
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.move(450, 450)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(150, 100, 480, 320)
        self.table.setRowCount(12)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setFont(QFont("", 12))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['班级','任课教师'])

        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-安排节次')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addRow(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.subComboBox = QComboBox()
        self.leaderComboBox = QComboBox()

        for m in range(len(self.list)):
            self.subComboBox.addItems(self.list[m])
        self.cox1.append(self.subComboBox)
        self.table.setCellWidget(row_count, 1, self.cox1[row_count])

        for n in range(len(self.leader)):
            self.leaderComboBox.addItems(self.leader[n])
        self.cox2.append(self.leaderComboBox)
        self.table.setCellWidget(row_count, 2, self.cox2[row_count])

    def removeRow(self):
        row_count = self.table.rowCount()
        self.table.removeRow(row_count-1)
        self.cox1.pop()
        self.cox2.pop()

class Lesson(QWidget):
    def __init__(self):
        super().__init__()

        '''学期'''
        self.semesterLabel = QLabel('学期：', self)
        self.semesterLabel.setGeometry(150, 30, 50, 30)
        self.semesterLineEdit = QLineEdit(self)
        self.semesterLineEdit.setPlaceholderText('201701')
        self.semesterLineEdit.setGeometry(200, 30, 100, 30)

        '''选择班级'''
        self.classNo = QLabel('班级：', self)
        self.classNo.setGeometry(350, 30, 50, 30)
        self.classNoComboBox = QComboBox(self)
        self.classNoComboBox.setGeometry(400, 30, 100, 30)

        '''更新'''
        self.updateInfo = QPushButton('更新', self)
        self.updateInfo.setGeometry(670, 30, 100, 30)

        '''增加/删除节次按钮'''
        self.submit = QPushButton('提交表格', self)
        self.submit.move(250, 450)
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.move(450, 450)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(50, 80, 720, 350)
        self.table.setColumnCount(6)
        self.table.setColumnWidth(0, 100)
        self.table.setFont(QFont("", 12))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['','星期一','星期二','星期三','星期四','星期五'])

        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-安排节次')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class QueryLesson(QWidget):
    def __init__(self):
        super().__init__()

        '''学期'''
        self.semesterLabel = QLabel('学期：', self)
        self.semesterLabel.setGeometry(150, 30, 50, 30)
        self.semesterLineEdit = QLineEdit(self)
        self.semesterLineEdit.setPlaceholderText('201701')
        self.semesterLineEdit.setGeometry(200, 30, 100, 30)

        '''选择班级'''
        self.classNo = QLabel('班级：', self)
        self.classNo.setGeometry(350, 30, 50, 30)
        self.classNoComboBox = QComboBox(self)
        self.classNoComboBox.setGeometry(400, 30, 100, 30)

        '''查询'''
        self.queryInfo = QPushButton('查询', self)
        self.queryInfo.setGeometry(600, 30, 100, 30)

        '''增加/删除节次按钮'''
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.move(350, 450)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(50, 80, 720, 350)
        self.table.setColumnCount(6)
        self.table.setColumnWidth(0, 100)
        self.table.setFont(QFont("", 12))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['','星期一','星期二','星期三','星期四','星期五'])

        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('排课系统-安排节次')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


