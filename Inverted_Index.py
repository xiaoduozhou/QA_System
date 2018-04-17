import jieba
import math
class Inverted_index(object):
    line_dict = {}
    line_length =[]
    word_dic = {}
    real_word_dic={}
    def stopwordslist(self,filepath):
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
        return stopwords

    def seg_sentence(self,sentence):
        sentence_seged = jieba.cut_for_search(sentence.strip())
        stopwords = self.stopwordslist('data/stopword.txt')  # 这里加载停用词的路径
        outstr = ''
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr

    def load_KB(self,filename):
        file = open(filename,'r',encoding='utf-8')
        lines = file.readlines()
        for i,line in enumerate(lines):
            self.line_dict[i]=line
            wordlist = self.seg_sentence(line).split(" ")
            self.line_length.append(len(wordlist))##############
            for word in wordlist:
                #print(word)
                self.word_dic.setdefault(word,[]).append(i)
            for key,valuelist in self.word_dic.items():
                valueset = set(valuelist)
                self.real_word_dic[key]=valueset
        return 0

    def tf_idf(self,word,number):
        idf =  math.log(len(self.line_length)/float(len(self.real_word_dic[word])))
        count=0
        for i in self.word_dic[word]:
            if i == number:
                count+=1

        tf =  count/float(self.line_length[number])
        return tf*idf

    def search(self,sentence,num = 5):
        wordlist = self.seg_sentence(sentence).split(" ")
        passage_dic={}
        search_list=[]
        value_list=[]
        arr = [0] * 1000
        for word in wordlist:
            #print(word,self.real_word_dic[word])#######################################3
            try:
                for i in self.real_word_dic[word]:
                    if passage_dic.get(i)==None:
                        passage_dic.setdefault(i,self.tf_idf(word,i))
                    else:
                        passage_dic[i]=passage_dic.get(i)+self.tf_idf(word,i)
            except:
                pass
        passage_dic = sorted(passage_dic.items(), key=lambda d: d[1], reverse=True)
        #print(passage_dic)  #############################################################################
        i=1
        for key,value in  passage_dic:
            search_list.append(self.line_dict[key])
            value_list.append(value)
            i+=1
            if i>num:break
        return search_list,value_list

    def init(self):
        self.load_KB('data/knowledge1.txt')
        '''
        for key,value in self.word_dic.items():
            print(key,value)
        for key,value in self.real_word_dic.items():
            print(key,value)
        '''

if __name__=="__main__":
    inveted = Inverted_index()
    inveted.init()
    sentence = "深秋到第二年初春，晴朗的夜晚容易形成雾，这主要是因为晴朗的夜晚大气逆辐射弱，近地面降温快"
    print("文本：\n"+sentence)
    print("\n相似文本:")
    respone_list,value_list = inveted.search(sentence,5)
    for respone,value in zip(respone_list,value_list):
        print(respone,value)





