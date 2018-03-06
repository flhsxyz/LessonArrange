import pymssql

def connect():
    conn = pymssql.connect(host='.', user='SA', password='123456', database='CourseSchedule')
    return conn

class database(object):
    def __init__(self):
        pass

    @staticmethod
    def login_check(username, password):
        print(username, password)
        sql = "SELECT * FROM Teacher"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchone()
        flag = 0
        for row in rows:
            if username == rows[1] and password == rows[2]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def insertStudentInfo(studentName, sex, classId):
        print(studentName, sex, classId)
        sql = "INSERT INTO Student VALUES(%s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(studentName, sex, classId))
        conn.commit()
        conn.close()

    @staticmethod
    def insertClassInfo(classid, classSection, classGrade, classNo, classRoomNo):
        sql = "INSERT INTO Class VALUES(%d, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(classid, classSection, classGrade,classNo, classRoomNo))
        conn.commit()
        conn.close()

    def queryClassId_isExist(ClassId):
        sql = "SELECT classId FROM Class"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if ClassId == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    def updateClassInfo(classId, classRoomNo):
        sql = "UPDATE Class SET classRoomNo = %s WHERE classId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (classRoomNo, classId))
        conn.commit()
        conn.close()

    def queryClassId(self):
        sql = "SELECT classId FROM Class"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def insertTeacherInfo(teacherName, teachSubject, subjectId):
        sql = "INSERT INTO Teacher(teacherName, teachSubject, subjectId) VALUES(%s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (teacherName, teachSubject, subjectId))
        conn.commit()
        conn.close()

    @staticmethod
    def querySchedule_by_timeId(id):
        sql = "SELECT timeId FROM Schedule"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if id == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def updateScheduleInfo(id, startTime, endTime):
        sql = "UPDATE Schedule SET startTime = %s, endTime = %s WHERE timeId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (startTime, endTime, id))
        conn.commit()
        conn.close()

    @staticmethod
    def insertScheduleInfo(timeId, setion, startTime, endTime):
        sql = "INSERT INTO Schedule VALUES(%d, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (timeId, setion, startTime, endTime))
        conn.commit()
        conn.close()

    @staticmethod
    def querySubjectNo_by_subjectName(subjectName):
        sql = "SELECT subjectNo FROM Subjects WHERE subjectName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,subjectName)
        id = cur.fetchone()
        return id[0]
        conn.close()

    @staticmethod
    def queryPeriod(id):
        sql = "SELECT periodId FROM Period"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0

        for row in rows:
            if id == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def updatePeriodInfo(periodNumber,id):
        sql = "UPDATE Period SET periodNumber = %s WHERE periodId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (periodNumber, id))
        conn.commit()
        conn.close()

    @staticmethod
    def insertPeriodInfo(periodId, setion, subjectName, periodNumber):
        sql = "INSERT INTO Period VALUES(%d, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (periodId, setion, subjectName, periodNumber))
        conn.commit()
        conn.close()

    def queryAllSubject(self):
        sql = "SELECT subjectName FROM Subjects"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    def queryAllTeacher(self):
        sql = "SELECT teacherName FROM Teacher"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    def queryTeacherId_by_teacherName(teacherName):
        sql = "SELECT teacherId FROM Teacher WHERE teacherName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,teacherName)
        id = cur.fetchone()
        return id[0]
        conn.close()

    @staticmethod
    def insertSubjectGroup(groupName, leaderId):
        sql = "INSERT INTO SubjectGroup VALUES (%s, %d)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (groupName, leaderId))
        conn.commit()
        conn.close()

    def queryAllSubjectGroup(self):
        sql = "SELECT SubjectGroupName FROM SubjectGroup"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def updateSubjectsInfo(subjectName, subjectGroupNo):
        print(subjectName, subjectGroupNo)
        sql = "UPDATE Subjects SET subjectGroupNo = %d WHERE subjectName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (subjectGroupNo, subjectName))
        conn.commit()
        conn.close()

    def querySubjectGroupId_by_SubjectGroupName(subjectGroupName):
        sql = "SELECT subjectGroupId FROM SubjectGroup WHERE subjectGroupName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,subjectGroupName)
        id = cur.fetchone()
        print(id[0])
        return id[0]
        conn.close()

    @staticmethod
    def queryClass_by_Section(section):
        sql = "SELECT classId FROM Class WHERE classSection = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, section)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def queryTeacherName_by_subject(subject):
        sql = "SELECT teacherName FROM Teacher WHERE teachSubject = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,subject)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def insertLectureForm(lectureId, semesterNo, teacherId, subjectName, classId):
        sql = "INSERT INTO LectureForm VALUES (%d, %d, %d, %s, %d)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (lectureId, semesterNo, teacherId, subjectName, classId))
        conn.commit()
        conn.close()

    @staticmethod
    def queryTeacherId_by_LectureId(lectureId):
        sql = "SELECT lectureId FROM LectureForm"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if lectureId == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def updateLectureForm(teacherId, lectureId):
        sql = "UPDATE LectureForm SET teacherId = %d WHERE lectureId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (teacherId, lectureId))
        conn.commit()
        conn.close()

    @staticmethod
    def querySection_by_classId(classId):
        sql = "SELECT classSection FROM Class WHERE classId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, classId)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def queryTimeId_by_Section(section):
        sql = "SELECT timeId FROM Schedule WHERE section = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, section)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def queryPeriod_by_Section(section):
        sql = "SELECT subjectName,periodNumber FROM Period WHERE section = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, section)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def insertLesson(courseId, lectureId, weekNo, timeId):
        sql = "INSERT INTO Lesson VALUES (%d, %d, %s, %d)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (courseId, lectureId, weekNo, timeId))
        conn.commit()
        conn.close()

    @staticmethod
    def updateLesson(courseId, lectureId):
        sql = "UPDATE Lesson SET lectureId = %d WHERE courseId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (lectureId, courseId))
        conn.commit()
        conn.close()

    @staticmethod
    def queryLectureId_by_courseId(courseId):
        sql = "SELECT lectureId FROM Lesson WHERE courseId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, courseId)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def querySubjectId_by_lectureId(lectureId):
        sql = "SELECT subjectId FROM LectureForm WHERE lectureId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, lectureId)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def querySubjectName_by_Id(Id):
        sql = "SELECT subjectName FROM Subjects WHERE subjectNo = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, Id)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def queryLessonId_isExist(courseId):
        sql = "SELECT courseId FROM Lesson"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if courseId == row[0]:
                flag = 1
                break
        return flag
        conn.close()


