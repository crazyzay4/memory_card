from PyQt6.QtWidgets import QApplication
from random import choice,shuffle
app = QApplication([])

from main_window import *
from menu_window import *
menu_window.show()

class Question:
    def __init__(self, q_text, ans, wrong1, wrong2, wrong3) -> None:
        self.question_text = q_text
        self.answer = ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    ...

q1 = Question("Дім", "house", "hose", "mouse", "horse")
q2 = Question("Пагорб", "diamond", "hill", "dumb", "rock")
q3 = Question("бездомний", "xr", "toty", "playground", "homeless" )
q4 = Question("Яблуко", "apple", "bobik", "friend", "apply" )

radio_list = [ rb_answer_1, rb_answer_2, rb_answer_3, rb_answer_4 ]
question_list = [q1, q2, q3, q4]


def next_question():
    current_question = choice(question_list)
    question.setText(current_question.question_text)
    shuffle(radio_list)
    radio_list[0].setText(current_question.answer)
    radio_list[1].setText(current_question.wrong1)
    radio_list[2].setText(current_question.wrong2)
    radio_list[3].setText(current_question.wrong3)

    correct_answer.setText(current_question.answer)

next_question()

def cheak_result():
    RadioGroup.setExclusive(False)
    for b in radio_list:
        if b.isChecked():
            if b.text() == correct_answer.text():
                result_text.setText("правильно")
            else:
                result_text.setText("неправильно")   
            b.setChecked(False)
    
    RadioGroup.setExclusive(True)


def switch_box():
    if btn_next.text() == "Відповісти":
        cheak_result()
        RadioGroupBox.hide()
        AnswerGroupBox.show()
        btn_next.setText("Наступне питання")

    elif btn_next.text() == "Наступне питання":
        RadioGroupBox.show()
        AnswerGroupBox.hide()
        btn_next.setText("Відповісти")
        next_question()
btn_next.clicked.connect(switch_box)

def close_menu():
    menu_window.hide()
    window.show()
    
btn_back.clcked.connect(close_menu)

def open_menu():
    menu_window.close()
    window.hide()

main_v_line.addWidget(btn_menu)
btn_menu.clicked.connect(open_menu)

def clear_menu():
    le_question.clear()
    le_answer.clear()
    le_wrong1.clear()
    le_wrong2.clear()
    le_wrong3.clear()

btn_clear.clicked.connect(clear_menu)


window.show()
app.exec()