from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox
from random import shuffle, choice as chc
from time import *


app = QApplication([])
from main_window import *


class Question():
    def __init__(self, text, answer, ans2, ans3, ans4):
        self.text = text
        self.answer = answer
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.attempts = 0
        self.success = 0
    def getText(self):
        return self.text
    def gotAnswer(self):
        self.attempts += 1
        self.success += 1
    def gotWrong(self):
        self.attempts += 1

question1 = Question("Яблуко", "apple", "application", "pineapple", "apply")
question2 = Question("Дім", "house", "horse", "hurry", "hour")
question3 = Question("Миша", "mouse", "mouth", "muse", "museum")
question4 = Question("Число", "number", "digit", "amount", "summary")

radio_list = [q_rb_1, q_rb_2, q_rb_3, q_rb_4]
question_list = [question1, question2, question3, question4]

def newQuestion():
    global currentQuestion

    currentQuestion = chc(question_list)
    lb_question.setText(currentQuestion.getText())

    shuffle(radio_list)

    radio_list[0].setText(currentQuestion.answer)
    radio_list[1].setText(currentQuestion.ans2)
    radio_list[2].setText(currentQuestion.ans3)
    radio_list[3].setText(currentQuestion.ans4)

def check_result():
    for answer in radio_list:
        correct = answer.isChecked()
        if correct:
            if answer.text() == currentQuestion.text:
                lb_question.setText('Правильно')
        else:
            lb_question.setText("Неправльно")

def switch_screen():
    if btn_next.text() == 'Відповісти':
        check_result()
        question_group.hide()
        gb_answer.show()

        btn_next.setText("Наступне питання")
    else:
        newQuestion()
        question_group.hide()
        gb_answer.show()

        btn_next.setText("Відповісти")


def rest():
    main_win.hide()
    sleep(sb_rest.value() * 60)
    main_win.show()


newQuestion()

btn_rest.clicked.connect(rest)
btn_next.clicked.connect(switch_screen)

main_win.show()
app.exec_()

