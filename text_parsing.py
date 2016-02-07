from textblob import TextBlob
from nltk.tag import pos_tag

def parse(text):

    CC = CD = DT = EX = FW = IN = JJ = JJR = JJS = LS = MD = NN = NNS = NNP = NNPS = PDT = POS = PRP = PRPD = \
    RB = RBR = RBS = RP = SYM = TO = UH = VB = VBD = VBG = VBN = VBP = VBZ = WDT = WP = WPD = WRB = 0

    tagged_sent = pos_tag(text.split())


    for word in tagged_sent:
        if word[1] == 'CC':
            CC = CC + 1
        if word[1] == 'CD':
            CD = CD + 1
        if word[1] == 'DT':
            DT = DT + 1
        if word[1] == 'EX':
            EX = EX + 1
        if word[1] == 'FW':
            FW = FW + 1
        if word[1] == 'IN':
            IN = IN + 1
        if word[1] == 'JJ':
            JJ = JJ + 1
        if word[1] == 'JJR':
            JJR = JJR + 1
        if word[1] == 'JJS':
            JJS = JJS + 1
        if word[1] == 'LS':
            LS = LS + 1
        if word[1] == 'MD':
            MD = MD + 1
        if word[1] == 'NN':
            NN = NN + 1
        if word[1] == 'NNS':
            NNS = NNS + 1
        if word[1] == 'NNP':
            NNP = NNP + 1
        if word[1] == 'NNPS':
            NNPS = NNPS + 1
        if word[1] == 'PDT':
            PDT = PDT + 1
        if word[1] == 'POS':
            POS = POS + 1
        if word[1] == 'PRP':
            PRP = PRP + 1
        if word[1] == 'PRP$':
            PRPD = PRPD + 1
        if word[1] == 'RB':
            RB = RB + 1
        if word[1] == 'RBR':
            RBR = RBR + 1
        if word[1] == 'RBS':
            RBS = RBS + 1
        if word[1] == 'RP':
            RP = RP + 1
        if word[1] == 'SYM':
            SYM = SYM + 1
        if word[1] == 'TO':
            TO = TO + 1
        if word[1] == 'UH':
            UH = UH + 1
        if word[1] == 'VB':
            VB = VB + 1
        if word[1] == 'VBD':
            VBD = VBD + 1
        if word[1] == 'VBG':
            VBG = VBG + 1
        if word[1] == 'VBN':
            VBN = VBN + 1
        if word[1] == 'VBP':
            VBP = VBP + 1
        if word[1] == 'VBZ':
            VBZ = VBZ + 1
        if word[1] == 'WDT':
            WDT = WDT + 1
        if word[1] == 'WP':
            WP = WP + 1
        if word[1] == 'WP$':
            WPD = WPD + 1
        if word[1] == 'WRB':
            WRB = WRB + 1

    past = VBN + VBD
    present = VBG + VBP + VBZ
    plural = NNS + NNPS
    singular = VBP + VBZ + NN + NNP

    return CC,CD,DT,EX,FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RBS,RP,SYM,\
    TO,UH,VB,VBD,VBG,VBN,VBP,VBZ,WDT,WP,WPD,WRB,past,present,plural,singular
    