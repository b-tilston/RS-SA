import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import sentiment_mod as s
import csv
import re

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [sentence.strip() for sentence in sentences]
    return sentences

# with open('Breath of the Wild Reviews.csv', encoding="utf8", errors='ignore') as zelda:
#     reader = csv.reader(zelda)
#     textlist = list(reader)
    
#print(len(textlist)) #establishs the number of paragraphs that we can analyse with the sentiment module

# for paragraph in textlist:
#     line = split_into_sentences(str(paragraph))
#     #print(str(line))
#     for lineelement in line:
#         #print(str(lineelement))
#         sentiment_value, confidence = s.sentiment(str(lineelement))
#         print(lineelement, sentiment_value, confidence) #Prints the text, a pos/neg tag attributed by the algorithms in the module and a confidence in that rating (0-1.0)

#         output = open("Review Sentiment - BOTW.csv","a", encoding="utf-8")
#         output.write(str(lineelement))
#         output.write(", ")
#         output.write(sentiment_value)
#         output.write(", ")
#         output.write(str(confidence)) 
#         output.write('\n')
#         output.close()
    
stop_words = nltk.corpus.stopwords.words('english')
NEWstop_words = ['Hideo', 'Kojima', 'Sam', ';', '.', ',', 'Chiral', '"''"', "'s'",'``', "The", "I", ',\\n', 'game', 'you\\', 'It', 'bridges', 'it\\', "''", "'", "'s", ')', "'ll", '-', 'but', 'though', 'sam\\', '(', 'neg,1\\n', 'pos,1\\n', 'it\\', '\\', 'there\\', 'i\\', 'sam\\', 'stranding\\', "don\\'t", 'that\\', 'they\\', 'neg,0.8\\n', 'neg,0.6\\n', 'kojima\\', "isn\\'t", 'game\\', 'he\\', 'pos,0.8\\n', "doesn\\'t", 'you\\', "can\\'t", 'we\\', 'pos,0.6\\n', "aren\\'t", 'you\\', "'re", '\i', 'death', 'stranding', 'players', 'time', 'story', '--', 'gear', '\i', 'new', 'gameplay', 'hours', ':', 'delivery', 'characters', 'games', '?', "'ve", 'network', 'kojima\\', 'experience', 'delivering', 'terrain', 'narrative', 'player', 'life', 'timefall', 'character', 'cities', 'deliver', 'good', 'build', 'walking', 'combat', 'carry', 'want', 'map', 'human', 'connection', 'interesting', 'that', 'equipment', "'m", 'journey', "'d", 'online', 'mission', 'plot', 'building', 'living', 'playing', 'great', 'others', 'system', 'cast', 'stealth', 'man', 'baby', 'kind', 'hard', 'played', 'united', 'difficult', 'social', 'fun', 'vehicles', 'everyone', 'real', 'easy', 'balance', 'different', 'elements', 'simple', 'level', 'landscape', 'areas', 'job', 'weapons', 'travel', 'person', 'materials', 'important', 'body', 'tools', 'avoid', 'carrying', 'climbing', 'boss', 'unique', "won\\'t", "didn\\'t", 'also', 'even', 'things', 'one', 'like', 'as', 'something', 'way', 'make', 'much', 'around', 'back', 'across', 'Zelda', 'Breath', "n't", "'the" ]
stop_words.extend(NEWstop_words)
#print(stop_words)

data = [line.strip('[]') for line in open("Review Sentiment - BOTW.csv", 'r')]
#print(sent_tokenize(str(data)))
#texts = [[word.lower() for word in text.split()] for text in data]
#rint(word_tokenize(str(data)))
word_tokens = word_tokenize(str(data)) 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
newfilteredsentence = []

for w in word_tokens:
    if w not in stop_words:
        newfilteredsentence.append(w.lower())
        
#print(word_tokens)
#print(newfilteredsentence)

parsedsentence = nltk.FreqDist(newfilteredsentence)
print(parsedsentence.most_common(263))

commonwords = parsedsentence.most_common(263)
with open("BOTW-250MostCommon.csv","a", encoding="utf-8") as commonwordsave:
    for entry in commonwords:
        # print(str(entry[0]))
        commonwordsave.write(str(entry[0]))
        commonwordsave.write(", ")
        commonwordsave.write(str(entry[1]))
        commonwordsave.write('\n')

commonwordsave.close()


#for word in texts:
#    print(word)
#    strword = str(word)
 #   newword = strword.replace(",", "")
#    print(newword)
#print(len(str(texts)))


# ps = PorterStemmer()    
# for paragraph in textlist:
#     print(ps.stem(paragraph))
#     all_words = (ps.stem(paragraph))
#     fdist = FreqDist()
#     for word in word_tokenize(str(all_words)):
#     fdist[word.lower()] += 1
#     all_words = nltk.FreqDist(texts)


#word_features = list(all_words.keys())[:3000]
#print(word_features)