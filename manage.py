from login import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from sql import database
from PyQt5.QtWidgets import *

class myLogin(Login, QMainWindow):
    close_signal_1 = pyqtSignal()
    close_signal_2 = pyqtSignal()
    close_signal_3 = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(lambda:self.login_btn(self.usernameEdit.text(), self.passwordEdit.text()))
        self.btn2.clicked.connect(self.close)

    def login_btn(self, username, password):
        if username == '' or password == '':
            QMessageBox.information(self, '无法登录', '请正确填写用户名和密码')
        elif username == 'wang' and password == '123456':
            self.close_signal_1.emit()
            self.close()
        elif username == 'leader' and password == '123456':
            self.close_signal_2.emit()
            self.close()
        elif username == 'master' and password == '123456':
            self.close_signal_3.emit()
            self.close()
        else:
            QMessageBox.information(self, '无法登陆', '用户名和密码不匹配')

class myControl_1(Control_1, QDialog):
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    change4_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(self.changeInputClass)
        self.btn2.clicked.connect(self.changeInputStudent)
        self.btn3.clicked.connect(self.changeInputTeacher)
        self.btn4.clicked.connect(self.returnLogin)

    def changeInputClass(self):
        self.change1_sign.emit()
        self.close()

    def changeInputStudent(self):
        self.change2_sign.emit()
        self.close()

    def changeInputTeacher(self):
        self.change3_sign.emit()
        self.close()

    def returnLogin(self):
        self.change4_sign.emit()
        self.close()

class myControl_2(Control_2, QDialog):
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    change4_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(self.changeTeacher)
        self.btn2.clicked.connect(self.changeLesson)
        self.btn3.clicked.connect(self.changeQueryLesson)
        self.btn4.clicked.connect(self.returnLogin)

    def changeTeacher(self):
        self.change1_sign.emit()
        self.close()

    def changeLesson(self):
        self.change2_sign.emit()
        self.close()

    def changeQueryLesson(self):
        self.change3_sign.emit()
        self.close()

    def returnLogin(self):
        self.change4_sign.emit()
        self.close()

class myControl_3(Control_3, QDialog):
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    change4_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(self.changeSchedule)
        self.btn2.clicked.connect(self.changePeriod)
        self.btn3.clicked.connect(self.changeSubjectGroup)
        self.btn4.clicked.connect(self.returnLogin)

    def changeSchedule(self):
        self.change1_sign.emit()
        self.close()

    def changePeriod(self):
        self.change2_sign.emit()
        self.close()

    def changeSubjectGroup(self):
        self.change3_sign.emit()
        self.close()

    def returnLogin(self):
        self.change4_sign.emit()
        self.close()

class myInputClass(InputClass, QWidget):
    return_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.id = 0
        self.classid = -1
        self.returnbtn.clicked.connect(self.returnControl)
        self.submit.clicked.connect(lambda: self.getinfo(self.sectionComboBox.currentText(), self.gradeComboBox.currentText(), self.nameEdit.text(), self.classroomEdit.text()))

    def getinfo(self, section, grade, classNo, classRoomNo):
        if section == '初中部':
            self.id = 1
        elif section == '高中部':
            self.id = 2

        if grade == '一年级':
            self.id = self.id * 10 + 1
        elif grade == '二年级':
            self.id = self.id * 10 + 2
        elif grade == '三年级':
            self.id = self.id * 10 + 3

        if classNo == '' or classRoomNo == '':
            QMessageBox.information(self,'wrong', '有信息未选择')
        else:
            self.id = self.id * 10 + int(classNo)
            flag = database.queryClassId_isExist(self.id)
            if flag:
                database.updateClassInfo(self.id, classRoomNo)
            else:
                database.insertClassInfo(self.id, section, grade, classNo, classRoomNo)
            self.info.append('%s  %s  %s班  教室：%s' % (section, grade, classNo, classRoomNo))

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class myInputStudent(InputStudent, QWidget):
    return_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.gender = ''
        list = []
        list = database.queryClassId(self)
        for i in range(len(list)):
            self.classnameBox.addItem(str(list[i][0]))
        self.sexbtn1.toggled.connect(self.getMaleSex)
        self.sexbtn2.toggled.connect(self.getFemaleSex)
        self.submit.clicked.connect(lambda: self.getinfo(self.nameEdit.text(),self.gender,self.classnameBox.currentText()))
        self.returnbtn.clicked.connect(self.returnControl)

    def returnControl(self):
        self.return_sign.emit()
        self.close()

    def getMaleSex(self):
        if self.sexbtn1.isChecked():
            self.gender = '男'

    def getFemaleSex(self):
        if self.sexbtn2.isChecked():
            self.gender = '女'

    def getinfo(self, studentName, sex, classNo):
        if studentName == '' or sex == '' or classNo == '':
            QMessageBox.information(self,'wrong', '有信息未选择')
        else:
            self.info.append('%s  %s  %s' % (studentName, sex, classNo))
            database.insertStudentInfo(studentName, sex, classNo)

class myInputTeacher(InputTeacher, QWidget):
    return_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.returnbtn.clicked.connect(lambda: self.returnControl())
        self.submit.clicked.connect(lambda: self.getinfo(self.nameEdit.text(), self.subjectEdit.text()))

    def getinfo(self, teacherName, teachSubject):
        if teacherName == '' or teachSubject == '':
            QMessageBox.information(self,'wrong', '有信息未选择')
        else:
            self.info.append('%s  教授学科：%s' % (teacherName, teachSubject))
            subjectId = database.querySubjectNo_by_subjectName(teachSubject)
            print(subjectId)
            database.insertTeacherInfo(teacherName, teachSubject, subjectId)

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class mySchedule(Schedule, QWidget):
    return_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.returnbtn.clicked.connect(self.returnControl)
        self.submit.clicked.connect(lambda: self.getSchInfo(self.sectionComboBox.currentText()))

    def getSchInfo(self, section):
        if section == '初中部':
            id = 1
        elif section == '高中部':
            id = 2
        id = id * 100

        for i in range(0,self.table.rowCount()):
            id = id+1
            flag = database.querySchedule_by_timeId(id)
            if flag:
                database.updateScheduleInfo(id, self.table.item(i,1).text(), self.table.item(i,2).text())
            else:
                database.insertScheduleInfo(id, section, self.table.item(i,1).text(), self.table.item(i,2).text())

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class myPeriod(Period, QWidget):
    return_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.returnbtn.clicked.connect(self.returnControl)
        self.submit.clicked.connect(lambda: self.getPeriodInfo(self.sectionComboBox.currentText()))

        '''学科'''
        self.cox1 = []
        for i in range(4):
            self.subComboBox = QComboBox()
            self.list = database.queryAllSubject(self)
            for m in range(len(self.list)):
                self.subComboBox.addItems(self.list[m])
            self.cox1.append(self.subComboBox)
            self.table.setCellWidget(i, 1, self.cox1[i])

        '''添加删除按钮操作'''
        self.add.clicked.connect(lambda :self.addRow())
        self.remove.clicked.connect(lambda: self.removeRow())

    def addRow(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.subComboBox = QComboBox()
        for m in range(len(self.list)):
            self.subComboBox.addItems(self.list[m])
        self.cox1.append(self.subComboBox)
        self.table.setCellWidget(row_count, 1, self.cox1[row_count])

    def removeRow(self):
        row_count = self.table.rowCount()
        self.table.removeRow(row_count-1)
        self.cox1.pop()

    def getPeriodInfo(self, section):
        if section == '初中部':
            sectionid = 1
        elif section == '高中部':
            sectionid = 2
        sectionid = sectionid*100

        for i in range(self.table.rowCount()):
            subjectName = self.cox1[i].currentText()
            subjectNo = database.querySubjectNo_by_subjectName(subjectName)
            periodNumber = self.table.item(i,2).text()
            id = sectionid + int(subjectNo)
            flag = database.queryPeriod(id)
            if flag:
                database.updatePeriodInfo(periodNumber, id)
            else:
                database.insertPeriodInfo(id, section, subjectName, periodNumber)

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class mySubjectGroup(SubjectGroup, QWidget):
    return_sign = pyqtSignal()
    addGroup_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.addGroup.clicked.connect(self.addGroup_sign.emit)
        self.refresh.clicked.connect(self.refreshGroupInfo)
        self.submit.clicked.connect(self.getSubjetGroupInfo)
        self.returnbtn.clicked.connect(self.returnControl)
        
        '''学科'''
        self.list = []
        self.cox = []
        for i in range(12):
            self.list = database.queryAllSubject(self)
            self.table.setItem(i, 0, QTableWidgetItem(self.list[i][0]))

            '''所属学科组'''
            self.groupComboBox = QComboBox()
            self.group= database.queryAllSubjectGroup(self)
            for n in range(len(self.group)):
                self.groupComboBox.addItems(self.group[n])
            self.cox.append(self.groupComboBox)
            self.table.setCellWidget(i, 1, self.cox[i])

        '''按钮操作'''

    def refreshGroupInfo(self):
        self.cox = []
        for i in range(12):
            '''所属学科组'''
            self.groupComboBox = QComboBox()
            self.group= database.queryAllSubjectGroup(self)
            for n in range(len(self.group)):
                self.groupComboBox.addItems(self.group[n])
            self.cox.append(self.groupComboBox)
            self.table.setCellWidget(i, 1, self.cox[i])

    def getSubjetGroupInfo(self):
        for i in range(12):
            subjectName = self.table.item(i, 0).text()
            group = self.cox[i].currentText()
            subjectGroupId = database.querySubjectGroupId_by_SubjectGroupName(group)
            database.updateSubjectsInfo(subjectName, subjectGroupId)

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class myAddGroup(AddGroup, QDialog):
    def __init__(self):
        super().__init__()

        '''combobox学科组长名称'''
        self.leader = database.queryAllTeacher(self)
        for i in range(len(self.leader)):
            self.leaderComboBox.addItems(self.leader[i])

        self.addButton.clicked.connect(lambda: self.getinfo(self.subLineEdit.text(), self.leaderComboBox.currentText()))

    def getinfo(self, groupName, teacherName):
        if groupName == '':
            QMessageBox.information(self,'wrong', '请填写学科组名称')
        else:
            teacherId = database.queryTeacherId_by_teacherName(teacherName)
            database.insertSubjectGroup(groupName, int(teacherId))
            QMessageBox.information(self, '成功', '添加成功')

class myLecture(Lecture, QWidget):
    return_sign = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.returnbtn.clicked.connect(self.returnControl)

        self.subjectList = []
        self.subjectList = database.queryAllSubject(self)
        for i in range(len(self.subjectList)):
            self.subjectComboBox.addItems(self.subjectList[i])

        self.updatebtn.clicked.connect(self.updateInfo)
        self.submit.clicked.connect(self.getLectureInfo)

    def updateInfo(self):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(['班级','任课教师'])
        '''表头字体颜色'''
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 15, QFont.Bold))
            headItem.setForeground(QBrush(Qt.black))
            headItem.setTextAlignment(Qt.AlignVCenter)

        self.list = []
        self.list = database.queryClass_by_Section(self.sectionComboBox.currentText())
        self.cox = []
        for i in range(len(self.list)):
            '''班级'''
            self.table.setItem(i, 0, QTableWidgetItem(str(self.list[i][0])))

            '''教师'''
            self.teacherComboBox = QComboBox()
            self.teacher= database.queryTeacherName_by_subject(self.subjectComboBox.currentText())
            for n in range(len(self.teacher)):
                self.teacherComboBox.addItems(self.teacher[n])
            self.cox.append(self.teacherComboBox)
            self.table.setCellWidget(i, 1, self.cox[i])

    def getLectureInfo(self):

        semester = self.semesterLineEdit.text()
        section = self.sectionComboBox.currentText()
        subject = self.subjectComboBox.currentText()

        for i in range (len(self.list)):
            classId = self.table.item(i, 0).text()
            teacherName = self.cox[i].currentText()
            teacherId = database.queryTeacherId_by_teacherName(teacherName)
            subjectId = database.querySubjectNo_by_subjectName(subject)
            lectureId = int(semester)%10000*100000 + int(classId)*100 + int(subjectId)

            '''判断是更新还是插入'''
            flag = database.queryTeacherId_by_LectureId(lectureId)
            if flag:
                database.updateLectureForm(teacherId, lectureId)
            else:
                database.insertLectureForm(lectureId, semester, teacherId, subjectId, classId)

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class myLesson(Lesson, QWidget):
    return_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.returnbtn.clicked.connect(self.returnControl)
        self.submit.clicked.connect(self.getInfo)

        '''获值'''
        self.classNo = []
        self.classNo = database.queryClassId(self)
        for i in range(len(self.classNo)):
            self.classNoComboBox.addItem(str(self.classNo[i][0]))

        '''按钮'''
        self.updateInfo.clicked.connect(self.refresh)

    def refresh(self):
        self.section = database.querySection_by_classId(int(self.classNoComboBox.currentText()))
        self.rowCount = database.queryTimeId_by_Section(self.section)
        self.table.setRowCount(len(self.rowCount))
        self.cox = [[] for i in range(len(self.rowCount))]
        for i in range(len(self.rowCount)):
            self.table.setItem(i, 0, QTableWidgetItem('第%s节课' % str(i+1)))

            for j in range(5):
                self.subComboBox = QComboBox()
                sub = database.queryAllSubject(self)
                for m in range(len(sub)):
                    self.subComboBox.addItems(sub[m])
                self.cox[i].append(self.subComboBox)
                self.table.setCellWidget(i, j+1, self.cox[i][j])

    def getInfo(self):
        self.subject = [[] for i in range(len(self.rowCount))]
        Chinese = 0; Math = 0; English = 0;
        Politics = 0; History = 0; Geography = 0;
        Physics = 0; Chemistry = 0; Biology = 0;
        PE = 0; Music = 0 ;ComputerScience = 0

        for i in range(len(self.rowCount)):
            for j in range(5):
                subjectItem = self.cox[i][j].currentText()
                self.subject[i].append(self.cox[i][j].currentText())
                if subjectItem == '语文':
                    Chinese += 1
                elif subjectItem =='数学':
                    Math += 1
                elif subjectItem == '英语':
                    English += 1
                elif subjectItem == '政治':
                    Politics += 1
                elif subjectItem == '历史':
                    History += 1
                elif subjectItem == '地理':
                    Geography += 1
                elif subjectItem == '物理':
                    Physics += 1
                elif subjectItem == '化学':
                    Chemistry += 1
                elif subjectItem == '生物':
                    Biology += 1
                elif subjectItem == '体育':
                    PE += 1
                elif subjectItem == '音乐':
                    Music += 1
                elif subjectItem == '计算机':
                    ComputerScience += 1
                    
        rows = database.queryPeriod_by_Section(self.section)
        flag = 1
        for i in range(len(rows)):
            if rows[i][0] == '语文':
                if int(rows[i][1]) > Chinese:
                    QMessageBox.information(self, 'wrong', '语文排课课时少%d节课' % (int(rows[i][1])-Chinese))
                    flag = 0
                    break
                elif int(rows[i][1]) < Chinese:
                    QMessageBox.information(self, 'wrong', '语文排课课时多%d节课' % (Chinese-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '数学':
                if int(rows[i][1]) > Math:
                    QMessageBox.information(self, 'wrong', '数学排课课时少%d节课' % (int(rows[i][1])-Math))
                    flag = 0
                    break
                elif int(rows[i][1]) < Math:
                    QMessageBox.information(self, 'wrong', '数学排课课时多%d节课' % (Math-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '英语':
                if int(rows[i][1]) > English:
                    QMessageBox.information(self, 'wrong', '英语排课课时少%d节课' % (int(rows[i][1])-English))
                    flag = 0
                    break
                elif int(rows[i][1]) < English:
                    QMessageBox.information(self, 'wrong', '英语排课课时多%d节课' % (English-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '政治':
                if int(rows[i][1]) > Politics:
                    QMessageBox.information(self, 'wrong', '政治排课课时少%d节课' % (int(rows[i][1])-Politics))
                    flag = 0
                    break
                elif int(rows[i][1]) < Politics:
                    QMessageBox.information(self, 'wrong', '政治排课课时多%d节课' % (Politics-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '历史':
                if int(rows[i][1]) > History:
                    QMessageBox.information(self, 'wrong', '历史排课课时少%d节课' % (int(rows[i][1])-History))
                    flag = 0
                    break
                elif int(rows[i][1]) < History:
                    QMessageBox.information(self, 'wrong', '历史排课课时多%d节课' % (History-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '地理':
                if int(rows[i][1]) > Geography:
                    QMessageBox.information(self, 'wrong', '地理排课课时少%d节课' % (int(rows[i][1])-Geography))
                    flag = 0
                    break
                elif int(rows[i][1]) < Geography:
                    QMessageBox.information(self, 'wrong', '地理排课课时多%d节课' % (Geography-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '物理':
                if int(rows[i][1]) > Physics:
                    QMessageBox.information(self, 'wrong', '物理排课课时少%d节课' % (int(rows[i][1])-Physics))
                    flag = 0
                    break
                elif int(rows[i][1]) < Physics:
                    QMessageBox.information(self, 'wrong', '物理排课课时多%d节课' % (Physics-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '化学':
                if int(rows[i][1]) > Chemistry:
                    QMessageBox.information(self, 'wrong', '化学排课课时少%d节课' % (int(rows[i][1])-Chemistry))
                    flag = 0
                    break
                elif int(rows[i][1]) < Chemistry:
                    QMessageBox.information(self, 'wrong', '化学排课课时多%d节课' % (Chemistry-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '生物':
                if int(rows[i][1]) > Biology:
                    QMessageBox.information(self, 'wrong', '生物排课课时少%d节课' % (int(rows[i][1])-Biology))
                    flag = 0
                    break
                elif int(rows[i][1]) < Biology:
                    QMessageBox.information(self, 'wrong', '生物排课课时多%d节课' % (Biology-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '音乐':
                if int(rows[i][1]) > Music:
                    QMessageBox.information(self, 'wrong', '音乐排课课时少%d节课' % (int(rows[i][1])-Music))
                    flag = 0
                    break
                elif int(rows[i][1]) < Music:
                    QMessageBox.information(self, 'wrong', '音乐排课课时多%d节课' % (Music-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '体育':
                if int(rows[i][1]) > PE:
                    QMessageBox.information(self, 'wrong', '体育排课课时少%d节课' % (int(rows[i][1])-PE))
                    flag = 0
                    break
                elif int(rows[i][1]) < PE:
                    QMessageBox.information(self, 'wrong', '体育排课课时多%d节课' % (PE-int(rows[i][1])))
                    flag = 0
                    break

            elif rows[i][0] == '计算机':
                if int(rows[i][1]) > ComputerScience:
                    QMessageBox.information(self, 'wrong', '计算机排课课时少%d节课' % (int(rows[i][1])-ComputerScience))
                    flag = 0
                    break
                elif int(rows[i][1]) < ComputerScience:
                    QMessageBox.information(self, 'wrong', '计算机排课课时多%d节课' % (ComputerScience-int(rows[i][1])))
                    flag = 0
                    break

        if flag:
            self.InsertInfo()

    def InsertInfo(self):
        semester = int(self.semesterLineEdit.text())%10000
        classId = int(self.classNoComboBox.currentText())
        weekNo = ['星期一', '星期二', '星期三', '星期四', '星期五']
        for i in range(len(self.rowCount)):
            for j in range(5):
                subId = database.querySubjectNo_by_subjectName(self.cox[i][j].currentText())
                courseId = semester*1000000 + classId*1000+(j+1)*100 + (i+1)
                lectureId = semester*100000 + classId*100 + int(subId)
                flag = database.queryLessonId_isExist(courseId)
                if flag:
                    database.updateLesson(courseId, lectureId)
                else:
                    database.insertLesson(courseId, lectureId, weekNo[j], self.rowCount[i][0])

    def returnControl(self):
        self.return_sign.emit()
        self.close()

class myQueryLesson(QueryLesson, QWidget):
    return_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.returnbtn.clicked.connect(self.returnControl)
        self.queryInfo.clicked.connect(self.queryLessonInfo)

        '''获值'''
        self.classNo = []
        self.classNo = database.queryClassId(self)
        for i in range(len(self.classNo)):
            self.classNoComboBox.addItem(str(self.classNo[i][0]))

    def returnControl(self):
        self.return_sign.emit()
        self.close()

    def queryLessonInfo(self):
        if self.semesterLineEdit.text() == '':
            QMessageBox.information(self, 'wrong', '请填写学期号')
        else:
            self.section = database.querySection_by_classId(int(self.classNoComboBox.currentText()))
            self.rowCount = database.queryTimeId_by_Section(self.section)
            self.table.setRowCount(len(self.rowCount))
            for i in range(len(self.rowCount)):
                self.table.setItem(i, 0, QTableWidgetItem('第%s节课' % str(i+1)))

            semester = int(self.semesterLineEdit.text())%10000
            classId = int(self.classNoComboBox.currentText())
            for i in range(len(self.rowCount)):
                flag = 0
                testId = semester*1000000 + classId*1000 + 1*100 + (i+1)
                flag = database.queryLessonId_isExist(testId)
                if flag:
                    for j in range(5):
                        courseId = semester*1000000 + classId*1000 + (j+1)*100 + (i+1)
                        lectureId = database.queryLectureId_by_courseId(courseId)
                        subId = database.querySubjectId_by_lectureId(lectureId)
                        sub = database.querySubjectName_by_Id(subId)
                        self.table.setItem(i, j + 1, QTableWidgetItem(sub[0]))
                else:
                    QMessageBox.information(self,'wrong', '改班级还未排课！请前往排课页面！')
                    break;
