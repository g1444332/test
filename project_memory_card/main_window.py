from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QPushButton, QSpinBox, QButtonGroup, QGroupBox
from PyQt5.QtGui import QFont

main_win = QWidget()
main_win.resize(600, 500)
main_win.move(300, 300)
main_win.setWindowTitle("Memory Card")

btn_menu = QPushButton("Menu")
btn_rest = QPushButton("Відпочити")
btn_next = QPushButton("Відповісти")
sb_rest = QSpinBox()
sb_rest.setValue(30)

q_rb_1 = QRadioButton("1")
q_rb_2 = QRadioButton("2")
q_rb_3 = QRadioButton("3")
q_rb_4 = QRadioButton("4")

qb_Group = QButtonGroup()
qb_Group.addButton(q_rb_1)
qb_Group.addButton(q_rb_2)
qb_Group.addButton(q_rb_3)
qb_Group.addButton(q_rb_4)

question_group = QGroupBox("Варіанти відповідей")


gb_answer = QGroupBox()


lb_rest = QLabel("Хвилини")
lb_question = QLabel('Питання')

lineV_1 = QVBoxLayout()
lineV_1.addWidget(q_rb_1)
lineV_1.addWidget(q_rb_3)

lineV_2 = QVBoxLayout()
lineV_2.addWidget(q_rb_2)
lineV_2.addWidget(q_rb_4)

lineH_1 = QHBoxLayout()
lineH_1.addWidget(btn_menu)
lineH_1.addWidget(btn_rest)
lineH_1.addWidget(sb_rest)
lineH_1.addWidget(lb_rest)

lineH_2 = QHBoxLayout()
lineH_2.addWidget(lb_question, alignment= Qt.AlignCenter)

lineH_3 = QHBoxLayout()
lineH_3.addLayout(lineV_1)
lineH_3.addLayout(lineV_2)

h4_main = QHBoxLayout()
h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)




question_group.setLayout(lineH_3)

lineV_main = QVBoxLayout()
lineV_main.addLayout(lineH_1)
lineV_main.addLayout(lineH_2)

lineV_main.addWidget(question_group)
lineV_main.addLayout(h4_main)

main_win.setLayout(lineV_main)








