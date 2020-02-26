from mentorski.models import *
from collections import defaultdict
import collections
class MentorskiService(object):
    
    student = None

    def getStudentId(self):
        return self.student.id
    def getStudent(self):
        return self.student

    def getAllSubjectsHigherThanEcts(self,value):

        upisiStudent, _ = self.getUpisiPredmeti__Studenti()

        reportList = []
        for item in upisiStudent:
            predmet = {
                'ime': item.predmet.ime,
                'predmet': item.predmet.kod,
                'bodovi': item.predmet.bodovi,
            }
            if predmet not in reportList and predmet['bodovi'] >= value:
                reportList.append(predmet)
                
        # [print(item['ime'], item['predmet'], item['bodovi']) for item in reportList]
        return reportList

    def getAllSubjects(self):
        all_courses = Predmeti.objects.all()
        courses = []
        for course in all_courses:
            if len(course.program.split(' ')) > 4:
                course.program = (' '.join(course.program.split(' ')[:4]) + ' ...')
            courses.append(course)
        return courses

    def getUpisiPredmeti__Studenti(self):
        return (Upisi.objects.select_related('student'), Upisi.objects.select_related('predmet'))

    def getUpisiStudent(self):
        upisi = Upisi.objects.filter(student = self.student.id)
        IdCourses = []
        for item in upisi:
            IdCourses.append(item.predmet)
        return IdCourses

    def getUpisi(self):
        return Upisi.objects.filter(student = self.student.id)


    def groupPredmeti(self,upis__predmet,student):
        self.student = student
        filterList = []
        for item in upis__predmet:
            if item.student.id == self.student.id:
                filterList.append(item)
        upis__predmet = filterList

        groups = defaultdict(list)
        if self.getRedovniVanredni() == True:
            for obj in upis__predmet:
                if obj.status in ['enrolled', 'passed']:
                    groups[obj.predmet.sem_redovni].append(obj)
        elif self.getRedovniVanredni() == False:
            for obj in upis__predmet:
                if obj.status in ['enrolled', 'passed']:
                    groups[obj.predmet.sem_izvanredni].append(obj)
        
        grouped_list = groups.items()
        # print(grouped_list)
        # 
        # upis__predmet = sorted(upis__predmet,key=first)

        return grouped_list

    def getRedovniVanredni(self):
        if self.student.status == 'redovni':
            return True
        elif self.student.status == 'izvanredni':
            return False