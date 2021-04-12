from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
from random import randint
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
total = 0 

questions_list = []
questions_list.append(Question('What is the value of the number 𝝅?', '3.14159265359...', '8.1', '3.96...', '6'))
questions_list.append(Question('What is the value of the number e?', '2.71828...', '3.156', '7', '0.1'))
questions_list.append(Question('What is the ∑ of 10, 12, 8, 9, 6?', '45', '9.11', '0.101...', '102.3'))
 
app = QApplication([])
 
btn_OK = QPushButton('Answer...')
lb_Question = QLabel('The hardest question in the world!')
 
RadioGroupBox = QGroupBox("Variations:")
 
rbtn_1 = QRadioButton('Variation 1')
rbtn_2 = QRadioButton('Variation 2')
rbtn_3 = QRadioButton('Variation 3')
rbtn_4 = QRadioButton('Variation 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Result:")
lb_Result = QLabel('Are you correct?')
lb_Correct = QLabel('The answer will be here!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next->')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer...')
    
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        show_correct('Correct!')
        window.score += 1
        print('Statistics:\nTotal questions: ', window.total ,'\nCorrect answers: ', window.score)
        print('Rayting: ', (window.score/window.total*100), '%')
        
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')
            print('Rayting: ', (window.score/window.total*100), '%')
 
def next_question():
    if len(questions_list) > 0:
        window.total += 1
        cur_question = randint(0, len(questions_list)-1)
        q = questions_list[cur_question]
        ask(q)
        questions_list.remove(q)
    else:
        quit()
 
def click_OK():  
    if btn_OK.text() == 'Answer...':
        check_answer()
    else:
        next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('ISMaths Plus')

window.cur_question = -1 

btn_OK.clicked.connect(click_OK)
 
window.score = 0
window.total = 0

next_question()
window.resize(400, 300)
window.show()
app.exec()
