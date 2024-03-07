days = []
saywords = {
'':'',' ':' ', '   ':' ', '    ':'',
'what day today?': 'I don\' know. '
}
from time import ctime
import sys

def shr(a):
    s = "".join(map(str,a))
    return s
class Nstr1:
    def __init__(self, arg):
        self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"1")
        return c
class Nstr0:
    def __init__(self, arg):
        self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"0")
        return c
class Nstr:
    def __init__(self, arg):
        self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c
print(Nstr1(shr([False, True, False])))
kl = Nstr1('[False, True, False]')- Nstr1('[False, True, False]')
print(kl)

import numpy as np
def tf10(a):
    #l1 = eval(a)
    l1 = a
    #print("type:%s%s" %(type(l1),l1))
    bb = np.array(l1)
    yc = Nstr0(str(bb))
    yv = Nstr0('False')
    y0 = yc-yv
    yc = Nstr1(str(y0))
    yv = Nstr1('True')
    y1 = yc-yv
    yc = Nstr(str(y1))
    yv = Nstr(' ')
    y2 = yc-yv
    yc = Nstr(str(y2))
    yv = Nstr('[')
    y3 = yc-yv
    yc = Nstr(str(y3))
    yv = Nstr(']')
    y1 = yc-yv
    yc = Nstr(str(y1))
    yv = Nstr(',')
    y2 = yc-yv
    return y2
class ifthe:
    def __init__(self, ift):
        self.ret = ''
        self.ift = ift
        self.askname = [
        'what is you name',
        "what's you name",
        'what is your name',
        "what's your name",
        'who are you',
        "who're you"]
        self.day = [
        'today',
        'tomorrow'
        ]
        self.days = []
        self.byes = [
        'bye',
        'goodbye',
        'good bye',
        'seeyou',
        'see you',
        'bey',
        'exit',
        'quit'
        ]
        self.noun = [
        'morning',
        'afternoon',
        'evening',
        'CD',
        'english',
        'map',
        'ruler',
        'cup',
        'pencil',
        'orange',
        'jacket',
        'color',
        'red',
        'blue',
        'yello',
        'green',
        'black',
        'white',
        'purple',
        'brown',
        'name',
        'friend',
        'middle',
        'school',
        'library',
        'sister',
        'mom','mother',
        'dad','father',
        'grandparent','parent',
        'brother',
        'grandma','grandmother',
        'grandpa','grandfather',
        'son','daughter',
        'uncle',
        'aunt',
        'consin',
        'photo','picture',
        'gril','boy',
        'book',
        'dictionary','dictionaries',
        'box',
        'schoolbag',
        'bag',
        'teacher',
        'ring',
        'game',
        'watch',
        'help',
        'classroom',
        'room',
        'table',
        'bed',
        'chair',
        'desk',
        'tennis',
        'basketball',
        'baseball',
        'computer',
        'ping-pong',
        'bat',
        'ball',
        'tape',
        'player',
        'plane',
        'phone',
        'sport',
        'tv',
        'banana',
        'hamburger',
        'pear',
        'apple',
        'milk',
        'egg',
        'chiken',
        'rice',
        'store',
        't-shirt',
        'sock',
        'shoe',
        'short',
        'sweater',
        'dollar',
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'december',
        'november',
        'party',
        'stutent',
        'subject',
        'science',
        'p.e.',
        'music',
        'physical education',
        'math',
        'chinese',
        'geography',
        'history',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'firday',
        'saturday',
        'sunday',
        'lesson',
        'hour',
        'second'
        ]
        self.arti = [
        'the',
        'a','an'
        ]
        self.pron = [
        'you',
        'we',
        'that','this',
        'she',
        'he',
        'her',
        'his',
        'hers',
        'our',
        'ours',
        'yours','your',
        'i',
        'what'
        ]
        self.adje = [
        'good',
        'fine',
        'ok',
        'what',
        'green',
        'blue',
        'black',
        'red',
        'yello',
        'pink',
        'purple',
        'brown',
        'white',
        'nice',
        'no','yes',
        'first',
        'second',
        'last',
        'third',
        'middle',
        'next',
        'welcome',
        'some','any',
        'tidy',
        'not',
        'big','small',
        'tall','short',
        'long',
        'fun',
        'interesting',
        'boring',
        'relaxing',
        'difficult',
        'easy',
        'healthy',
        'much',
        'old',
        'young',
        'busy',
        'useful',
        'useless',
        'helpless',
        'helpful'
        ]
        self.num = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fifteen',
        'eighteen',
        'ninteen',
        'twenty',
        'thirty',
        'fouty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninty',
        'first',
        'second',
        'third',
        'fifth',
        'eighth',
        'ninth',
        'twelfth',
        'thirth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'twentieth'
        ]
        self.verb = [
        'am','is','are',
        'were',
        '\'s',
        '\'ve',
        'doing','did',
        'like','liked',
        'spell','spelled',
        'look','looked',
        'see',
        'put',
        'pull',
        'jump','jumping',
        'eat','eating',
        'jumping',
        'swim','swimming',
        'say','saied',
        'meet','meeting'
        ]
        self.adv = [
        'how',
        'now',
        'not',
        'too',
        'always',
        'only',
        'here'
        ]
        self.perp = [
        'in',
        'on',
        'under',
        'of',
        'by'
        ]
        self.conj = [
        'and',
        'or',
        'but',
        'because',
        'if',
        'when',
        ]
        self.inte = [
        'oh',
        'hello','hi',
        'well',
        'please',
        'okey'
        ]
        self.wh = [
        'how',
        'what',
        'who',
        'where',
        'whose',
        'why',
        'when'
        ]
        self.saynoun, self.sayadj, self.sayadv, self.saynum, self.sayverb, self.saypron = '', '', '', '', '', ''
        self.saywh = ''
        if any(word in self.ift.lower() for word in self.noun):
            self.saynoun = str([word in self.ift.lower() for word in self.noun])
            self.huce = (tf10(str(self.saynoun)).index('1'))
            #print(self.huce,self.saynoun,tf10(self.saynoun))
            self.saynoun = self.noun[int(self.huce)]
        if any(word in self.ift.lower() for word in self.verb):
            #self.sayverb = str([word in self.ift.lower() for word in self.verb])
            self.sayverb = str([word in self.ift.lower() for word in self.verb])
            self.huce = (tf10(str(self.sayverb)).index('1'))
            #print(self.huce,self.saynoun,tf10(self.saynoun))
            self.sayverb = self.verb[int(self.huce)]
        if any(word in self.ift.lower() for word in self.num):
            #self.saynum = str([word in self.ift.lower() for word in self.num])
            self.saynum = str([word in self.ift.lower() for word in self.num])
            self.huce = (tf10(str(self.saynum)).index('1'))
            #print(self.huce,self.saynoun,tf10(self.saynoun))
            self.saynum = self.num[int(self.huce)]
        if any(word in self.ift.lower() for word in self.adv):
            self.sayadv = str([word in self.ift.lower() for word in self.adv])
            self.huce = (tf10(str(self.sayadv)).index('1'))
            #print(self.huce,self.saynoun,tf10(self.saynoun))
            self.sayadv = self.adv[int(self.huce)]
            #self.sayadv = str([word in self.ift.lower() for word in self.adv])
        if any(word in self.ift.lower() for word in self.adje):
            self.sayadj = str([word in self.ift.lower() for word in self.adje])
            self.huce = (tf10(str(self.sayadj)).index('1'))
            #print(self.huce,self.saynoun,tf10(self.saynoun))
            self.sayadj = self.adje[int(self.huce)]
            #self.sayadj = str([word in self.ift.lower() for word in self.adj])
        if any(word in self.ift.lower() for word in self.pron):
            self.saypron = str([word in self.ift.lower() for word in self.pron])
            self.huce = (tf10(str(self.saypron)).index('1'))
            #print(self.huce,self.saypron,tf10(self.saypron))
            self.saypron = self.pron[int(self.huce)]
        if any(word in self.ift.lower() for word in self.wh):
            self.saywh = str([word in self.ift.lower() for word in self.wh])
            self.huce = (tf10(str(self.saywh)).index('1'))
            #print(self.huce,self.saynoun,tf10(self.saynoun))
            self.saywh = self.wh[int(self.huce)]
    #chat.b
    def hi(self):
        if any(word in self.ift.lower() for word in ['hi', 'hello', 'hey']):
            return 'Hi! '
        else:
            return ''
    def iname(self):
        if any(word in self.ift.lower() for word in self.askname):
            return 'I am 560A. '
        else:
            return ''
    def games(self):
        if 'game' in self.ift.lower():
            return 'OK! But I am sorry I cannot.'
        else:
            return ''
    def today(self):
        if 'today' in self.ift.lower():
            return 'Today is ' + ctime()[4:11] + '. '
        else:
            return ''
    def bye(self):
        if any(word in self.ift.lower() for word in self.byes):
            return 'See you! '
        else:
            return ''
    #chat.c
    '''
    def words(self):
        if any(word in self.ift.lower() for word in self.noun):
            self.saynoun = str([word in self.ift.lower() for word in self.noun])
            self.huce = self.saynoun.index('True')
            self.saynoun = self.noun[1]
        if any(word in self.ift.lower() for word in self.verb):
            self.sayverb = str([word in self.ift.lower() for word in self.verb])
        if any(word in self.ift.lower() for word in self.num):
            self.saynum = str([word in self.ift.lower() for word in self.num])
        if any(word in self.ift.lower() for word in self.adv):
            self.sayadv = str([word in self.ift.lower() for word in self.adv])
        if any(word in self.ift.lower() for word in self.adje):
            self.sayadj = str([word in self.ift.lower() for word in self.adj])'''
    def csay(self):
        '''
        if any(word in self.ift.lower() for word in self.verb):
            return 'yes. '#+'I do. '#+'I like '+str([word in self.ift.lower() for word in self.noun]) # self.saynoun
        if any(word in self.ift.lower() for word in self.verb):
        else:
            return ''
        '''
        if self.saynoun != '' and 'do' in self.ift:
            #I/ME
            if 'you' in self.saypron:#self.ift:;;;
                return f'Yes, I do. I {self.sayverb} {self.saynoun}. '
                #self.ret += f'Yes, I do. I {self.sayverb} {self.saynoun}. '
            elif 'she' in self.saypron:
                return f'Yes, she do. she {self.sayverb} {self.saynoun}. '
            elif 'he' in self.saypron:
                return f'Yes, he do. he {self.sayverb} {self.saynoun}. '

        return ''

#'''

#


#return self.pron[self.huce]      #self.pron[self.saypron]       #str(self.saypron)

class chat:
    def __init__(self, sr):
        self.sr = sr
        self.say = ''

    def b(self):
        self.say += ifthe(self.sr).hi()
        self.say += ifthe(self.sr).iname()
        self.say += ifthe(self.sr).today()
        self.say += ifthe(self.sr).bye()
        self.say += ifthe(self.sr).games()
        if any(word in self.sr.lower() for word in ['bye','goodbye','good bye','seeyou','see you','bey','exit','quit']):
            sys.exit()
        '''if '?' in self.sr:
            self.say += ifthe(self.sr).asks()'''
        '''
        if len(self.sr) - len(self.say) >= 18:
            self.say = "What're you say? "
        if self.say == '':
            self.say = "What're you say? "'''
        if self.sr.lower() in days:
            self.say += "Didn't you just say that? "
        return self.say
    def c(self):
        #ifthe(self.sr).words()
        self.say += ifthe(self.sr).csay()
        return self.say

while 1:
    abc = input('\033[35m>>> \033[0m')
    app = chat(abc)
    #print(app.b())
    prb = app.b()
    prc = app.c()
    if prc == '':
        if prb == '':
            try:
                prd = saywords[abc.lower()]
                if prd == '':
                    print('\033[32m>>>\033[0m\n')
                else:
                    print('\033[32m>>>',prd,'\033[0m\n')
            except Exception:
                print('\033[32m>>> Sorry, I do not quite understand whay you mean\033[0m\n')
        else:
            print('\033[32m>>>',prb,'\033[0m\n')
    else:
        print('\033[32m>>>',prc,'\033[0
