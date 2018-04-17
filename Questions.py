
class Question(object):

    def __init__(self):
        self.background = ""
        self.question = ""
        self.option_1 = ""
        self.option_2 = ""
        self.option_3 = ""
        self.option_4 = ""

    def get_right_option(self):
        right_answer=""
        for i in range(1,5):
            if getattr(self, "option_"+str(i)).startswith("R"):
                right_answer = getattr(self, "option_"+str(i))
        return right_answer

    def get_background(self):
        return self.background#.split(":",1)[1]

    def get_question(self):
        return self.question#.split(":",1)[1]