import os
from fpdf import FPDF 
import matplotlib.pyplot as plt
from datetime import date 
import matplotlib
matplotlib.use('Agg')

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 17)
        self.set_text_color(255,50,6)  
        self.set_draw_color(255,50,6)
        self.cell(200, 10, txt = "", ln = 2, align = 'C') 
        self.cell(190, 20, txt = "INDIAN INSTITUTE OF INFORMATION TECHNOLOGY, NAGPUR", \
         ln = 1, align = 'C',border=1)   
    
    def sub_head(self):
        self.set_text_color(5,52,252)  
        self.set_font("Times", size = 21,style='B') 
        self.blank()
        self.cell(200, 10, txt = "PROVISIONAL GRADE SHEET", ln = 2, align = 'C') 
        self.blank()

    def side_head(self,title):
        self.set_font(family='Times',style='I',size=17)
        self.set_text_color(26,82,34)
        self.cell(200,10,txt=title,align='C',ln=3)
        self.blank()
        
    def personal_details(self,dictionary):
        self.set_font(family='Times',style='B',size=19)
        self.set_text_color(0,0,0)
        self.cell(0, 10, 'Name                    : '+dictionary['name'], 0, 1)
        self.cell(0, 10, 'Semester              : '+dictionary['semester'], 0, 1)
        self.cell(0, 10, 'Department          : '+dictionary['department'], 0, 1)
        self.cell(0, 10, 'Enrollment I.D.    : '+dictionary['roll number'], 0, 1)
        self.cell(0, 10, 'Year                      : '+dictionary['year'], 0, 1)
        self.cell(0, 10, 'Hostel                    : '+dictionary['hostel'], 0, 1)    
            
    def blank(self):
        self.cell(200, 10, txt = "", ln = 2, align = 'C')
        
    def academic_details(self,dictionary):
        self.set_font(family='Times',style='B',size=19)
        self.set_text_color(46,160,236)
        self.cell(0, 10, 'Course             Marks ',0,1)
        self.set_font(family='Times',style='B',size=19)
        self.set_text_color(0,0,0) 
        self.cell(0, 10, dictionary['course1']+' '+dictionary['marks1']+'/100',0,1)
        self.cell(0, 10, dictionary['course2']+' '+dictionary['marks2']+'/100',0,1)
        self.cell(0, 10, dictionary['course3']+' '+dictionary['marks3']+'/100',0,1)
        self.cell(0, 10, dictionary['course4']+' '+dictionary['marks4']+'/100',0,1)
        self.cell(0, 10, dictionary['course5']+' '+dictionary['marks5']+'/100',0,1)
        self.cell(0, 10, dictionary['course6']+' '+dictionary['marks6']+'/100',0,1)

    def remark(self):
        self.set_font('Times', 'I', 15)
        self.set_text_color(0,0,0)
        self.cell(0, 10, '  _____________________________________________________________________', 0, 0, 1)
         
    def graph(self,dictionary):
        self.blank()
        marks=[int(dictionary['marks1']),int(dictionary['marks2']),int(dictionary['marks3']),
               int(dictionary['marks4']),int(dictionary['marks5']),int(dictionary['marks6'])]
        courses=['course1', 'course2', 'course3', 'course4', 'course5', 'course6']
        grand_total=sum(marks)
        mean=grand_total/6
        percentage=(grand_total/600)*100
        fig = plt.figure(tight_layout=True)
        ax = fig.add_axes([0,0,1,1])
        ax.bar(courses,marks)
        ax.set_title('MARKS DISTRIBUTION')
        ax.set_xlabel('SUBJECTS')
        ax.set_ylabel('MARKS')
        fig.savefig('fig.png',bbox_inches='tight')
        self.set_font(family='Times',style='B',size=19)
        self.set_text_color(0,0,0) 
        self.cell(0,10,txt='Total Marks Obtained   : '+str(grand_total)+'/600',ln=1 )
        self.cell(0,10,txt='Average Marks Obtained : '+str(mean),ln=1 )
        self.cell(0,10,txt='Percentage Marks Obtained : '+str(percentage)+'%',ln=3)
        self.image('fig.png', 25, 95, 155,125)
        os.remove('fig.png')
        
    def stamp(self):
        self.set_y(250)
        self.cell(200, 10, txt = 'Stamp : _________       ', ln = 2, align = 'R')
        self.cell(200, 10, txt = 'Date  : '+str(date.today())+'       ',align='R' )
        
    def footer(self):
        self.set_y(-15)
        self.set_text_color(0,0,0)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
   
def create_pdf(dictionary):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.sub_head()
    pdf.side_head('Personal Details ')
    pdf.personal_details(dictionary)
    pdf.side_head('Academic Details ')
    pdf.academic_details(dictionary)
    pdf.side_head('Remarks')
    pdf.remark()
    pdf.add_page(orientation = 'P')
    pdf.graph(dictionary)
    pdf.stamp()
    pdf.output('PDF\\'+dictionary['roll number']+'.pdf', 'F')






