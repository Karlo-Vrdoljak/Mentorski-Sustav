from mentorski.models import *
from collections import defaultdict
import collections
class MentorskiService(object):
    
    student = None

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

    def groupPredmeti(self,upis__predmet,student):
        self.student = student
        redovni_groups = defaultdict(list)
        if self.getRedovniVanredni() == True:
            for obj in upis__predmet:
                if obj.status in ['enrolled', 'passed']:
                    redovni_groups[obj.predmet.sem_redovni].append(obj)
        elif self.getRedovniVanredni() == False:
            for obj in upis__predmet:
                if obj.status in ['enrolled', 'passed']:
                    groups[obj.predmet.sem_izvanredni].append(obj)
        
        grouped_list = redovni_groups.items()
        # print(grouped_list)
        # 
        # upis__predmet = sorted(upis__predmet,key=first)

        return grouped_list

    def getRedovniVanredni(self):
        if self.student.status == 'redovni':
            return True
        elif self.student.status == 'izvanredni':
            return False