



class QuizBrain:

    def __init__(self,q_list):
        self.question_number=0
        self.question_list =q_list
        self.score=0

    def next_question(self):
        ques=self.question_list[self.question_number]
        self.question_number += 1

        ans=input(f"Q.{self.question_number}: {ques.question} (True/False):")
        self.check_answer(ans,ques.ans)
    def check_answer(self,var1,var2):
        if var1.lower()==var2.lower():
            self.score+=1
            print(f"Congrats! Correct Answer")

        else:
            self.score+=0
            print(f"That's wrong")
        print(f"The correct answer is {var2}")
        print(f" Your Score is {self.score}/{self.question_number}\n\n\n")