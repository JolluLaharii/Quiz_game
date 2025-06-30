from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
Question_bank=[]
for i in range(12):
    Que=Question(question_data[i]["text"],question_data[i]["answer"])
    Question_bank.append(Que)
quiz=QuizBrain(Question_bank)
for i in range(12):

    quiz.next_question()