import torch
import pickle
train_data_path='./CoNLL-2003/eng.train'
file = open(train_data_path,'r')

def process_line(text_line):
    word,POStag,SYNtag,NEtag = text_line.split()  #syntactic chunk tag and the fourth the named entity tag.
    print(word,POStag,SYNtag,NEtag)
    if word == "-DOCSTART-":
        return

temp_word_list=[]
temp_NEtag_list=[]
result_list=[]
NEtag_set=set()
try:
    while True:
        text_line = file.readline()
        if text_line:
            if text_line=="\n":
                continue
            #print(text_line.split())
            word,POStag,SYNtag,NEtag = text_line.split()
            #print(word)
            if word == "": 
                continue
            elif word =="-DOCSTART-":
                result_list.append((temp_word_list,temp_NEtag_list))
                temp_word_list.clear()
                temp_NEtag_list.clear()
            else:
                temp_word_list.append(word)
                temp_NEtag_list.append(NEtag)
                NEtag_set.add(NEtag)
        else:
            break
finally:
    file.close()
print(NEtag_set)
result_list.pop(0)
f=open('train_data.pkl','wb')
pickle.dump(result_list,f)
