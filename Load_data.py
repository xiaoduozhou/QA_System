from Questions import *
from Inverted_Index import *


def load_QA(filepath):
    question_list = []
    qa_set = Question()
    attributelist = ["background", "question", "option_1", "option_2", "option_3", "option_4"]
    index = 0
    for i, line in enumerate(open(filepath, 'r', encoding='utf-8').readlines()):
        line = line + " "
        setattr(qa_set, attributelist[index], line)
        if index == 5:
            question_list.append(qa_set)
            # print(qa_set.get_right_option())
            qa_set = Question()
            index = 0
            continue
        index += 1
    return question_list


def repeat_word(sentence1, sentence2):
    listA = inveted.seg_sentence(sentence1).split()
    listB = inveted.seg_sentence(sentence2).split()
    retA = [i for i in listA if i in listB]
    return len(retA)


def choose_best(qa):

    question = qa.background + " " + qa.question
    respone_list, value_list = inveted.search(question, 10)
    for string in respone_list:
        question+=" " +string
    key = 0
    final_num=1###############################################
    for i in range(1,5):
        number= repeat_word(question,getattr(qa, "option_"+str(i)))
        if number>key:
            key=number
            final_num=i

    return getattr(qa, "option_"+str(final_num)),final_num

if __name__=="__main__":
    inveted = Inverted_index()
    inveted.init()
    question_list = load_QA("data/test.txt")
    right_number=0
    option=[0]*5
    i=0
    for question in question_list:
        i+=1
        print(i/float(len(question_list)))
        string,final_num= choose_best(question)
        #string = question.option_1
        if question.get_right_option()==string:
            right_number+=1
            option[final_num]+=1
            print("------",option,"------")

    print(right_number/float(len(question_list)))
    print("final_option ： ",option)

'''
question_list = load_QA("data/train.txt")
for question in question_list:
    print(question.get_question().split(":",1))
    print(question.get_right_option().split(":",1))
    #print(question.option_1.split(":", 1))
    pass
'''
