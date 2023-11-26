from PyQt6.QtWidgets import (QWidget,QHBoxLayout,QVBoxLayout,
                            QLabel, QPushButton, QRadioButton,
                            QGroupBox, QButtonGroup)


window = QWidget()

win_width, wind_height = 700,400
window.resize(win_width, wind_height)
window.setWindowTitle("Memory Card. Автор: ....")


btn_menu = QPushButton("Меню")
btn_next = QPushButton("Відповісти")

question = QLabel()

rb_answer_1 = QRadioButton()
rb_answer_2 = QRadioButton()
rb_answer_3 = QRadioButton()
rb_answer_4 = QRadioButton()

RadioGroupBox = QGroupBox("Варіанти відповіді")

RadioGroup = QButtonGroup()

RadioGroup.addButton(rb_answer_1)
RadioGroup.addButton(rb_answer_2)
RadioGroup.addButton(rb_answer_3)
RadioGroup.addButton(rb_answer_4)


box_h_line = QHBoxLayout()
box_v_line_1 = QVBoxLayout()
box_v_line_2 = QVBoxLayout()


box_v_line_1.addWidget(rb_answer_1)
box_v_line_1.addWidget(rb_answer_2)

box_v_line_2.addWidget(rb_answer_3)
box_v_line_2.addWidget(rb_answer_4)

box_h_line.addLayout(box_v_line_1)
box_h_line.addLayout(box_v_line_2) 

RadioGroupBox.setLayout(box_h_line)

AnswerGroupBox = QGroupBox("Результат")
result_text = QLabel("правильно/неправильно")
correct_answer = QLabel("правильний варіант")

answer_box_line = QVBoxLayout()

answer_box_line.addWidget(result_text)
answer_box_line.addWidget(correct_answer)

AnswerGroupBox.setLayout(answer_box_line)



main_v_line = QVBoxLayout()

main_v_line.addWidget(question)
main_v_line.addWidget(RadioGroupBox)
main_v_line.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()
main_v_line.addWidget(btn_next)


window.setLayout(main_v_line)