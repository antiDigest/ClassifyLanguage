#Information Gain

CC (array([ 19.]), 0.11355641135283567)
CD (array([ 2.]), 0.07555363305303804)  --removed
DT (array([ 20.]), 0.07295702517937869) --removed
EX (array([ 1.]), 0.07330542496398129)  --removed
<!-- FW (array([ 1.]), 0.05378142337834613)  --removed -->
IN (array([ 30.]), 0.07752847662646795) --removed
JJ (array([ 7.]), 0.09339036684668192)
JJR (array([ 1.]), 0.0732343276271773)  --removed
JJS (array([ 4.]), 0.15610749145421676)
<!-- LS (array([ 0.]), 0.00253896593607697) -- LS remove -->
MD (array([ 5.]), 0.09129233010736015)
<!-- NN (array([ 22.]), 0.4549163803562972)
NNS (array([ 31.]), 0.12742732618815328)
NNP (array([ 2.]), 0.13015500069496885)
NNPS (array([ 1.]), 0.1369983760422812) -->
PDT (array([ 1.]), 0.05874844972959438) --removed
<!-- POS (array([ 1.]), 0.039807449263420516)    --removed -->
PRP (array([ 6.]), 0.07701716630713448) --removed
PRPD (array([ 4.]), 0.07296286216734431)    --removed
RB (array([ 21.]), 0.1148501546127606)
RBR (array([ 2.]), 0.08474203262779006)
RBS (array([ 3.]), 0.10246328348918518)
<!-- RP (array([ 2.]), 0.12421824003182455) -->
SYM (array([ 1.]), 0.335670926915516)
<!-- TO (array([ 27.]), 1.0023017646508678) -->
<!-- UH (array([ 1.]), 0.14526650417856538) -->
VB (array([ 14.]), 0.07454838987730196) --removed
<!-- VBD (array([ 6.]), 0.1374456625403684)
VBG (array([ 19.]), 0.25235552177189446)
VBN (array([ 15.]), 0.5023196745441756)
VBP (array([ 6.]), 0.08404026480255412)
VBZ (array([ 1.]), 0.15610749145421676)
WDT (array([ 4.]), 0.09762577528582848)
 -->WP (array([ 1.]), 0.07204900141249901)  --removed
WPD (array([ 1.]), 0.13226099054534157)
WRB (array([ 1.]), 0.07381605275041404) --removed
SentenceLength (array([ 25.]), 0.31255570352297046)
WordCount (array([ 215.]), 0.07579487809152596)
FunctionWordCount (array([ 143.]), 0.09339036684668192)
count_errors (array([ 1.]), 0.062218031322894635)
Sentiment (array([ 9.]), 0.18951061158115468)
Polarity (array([ 0.2784]), 0.09414791290733326)


#Chi Square analysis for numerical data

CC  CD  [ 0.03028981]
CD  DT  [ 0.05746658]
DT  EX  [ 0.08059035]
EX  FW  [-0.01185738]
FW  IN  [-0.00805927]
IN  JJ  [ 0.19408779]
JJ  JJR     [ 0.07136081]
JJR     JJS     [ 0.03230049]
JJS     LS  [ nan]
LS  MD  [ nan]
MD  NN  [ 0.04830167]
NN  NNS     [-0.08945958]
NNS     NNP     [ 0.02846717]
NNP     NNPS    [ 0.03863486]
NNPS    PDT     [ 0.04181721]
PDT     POS     [ 0.01445064]
POS     PRP     [-0.00360324]
PRP     PRPD    [ 0.24266024]
PRPD    RB  [ 0.01085641]
RB  RBR     [ 0.02723843]
RBR     RBS     [ 0.02827191]
RBS     RP  [ 0.04313636]
RP  SYM     [-0.0032751]
SYM     TO  [ 0.02728276]
TO  UH  [ 0.01767321]
UH  VB  [ 0.01381217]
VB  VBD     [-0.16961888]
VBD     VBG     [-0.01241256]
VBG     VBN     [ 0.16185623]
VBN     VBP     [-0.09854964]
VBP     VBZ     [-0.18183454]
VBZ     WDT     [ 0.13659542]
WDT     WP  [ 0.02126728]
WP  WPD     [-0.01055812]
WPD     WRB     [ 0.01097461]
WRB     SentenceLength  [ 0.02644872]
SentenceLength  WordCount   [ 0.10506515]
WordCount   FunctionWordCount   [ 0.80535607]
FunctionWordCount   count_errors    [-0.01962353]
count_errors    Sentiment   [-0.05662559]
Sentiment   Polarity    [ 0.61287312]
Polarity    Result  [ 0.05250223]


#Correlation with Result

CC  Result  [ 0.07859384]
CD  Result  [-0.01915808]
DT  Result  [-0.00609128]
EX  Result  [-0.0135004]
FW  Result  [-0.01917642]
IN  Result  [ 0.04428308]
JJ  Result  [-0.03021291]
JJR     Result  [-0.02239018]
JJS     Result  [ 0.05213688]
LS  Result  [ nan]
MD  Result  [-0.10105218]
NN  Result  [-0.20903547]
NNS     Result  [ 0.01948529]
NNP     Result  [-0.09404096]
NNPS    Result  [ 0.03996233]
PDT     Result  [-0.07148321]
POS     Result  [-0.01156557]
PRP     Result  [-0.00617003]
PRPD    Result  [-0.03341579]
RB  Result  [ 0.11368613]
RBR     Result  [ 0.01692208]
RBS     Result  [-0.01105208]
RP  Result  [ 0.08328936]
SYM     Result  [ 0.02844188]
TO  Result  [ 0.08073882]
UH  Result  [ 0.01197757]
VB  Result  [-0.02528915]
VBD     Result  [ 0.06038694]
VBG     Result  [ 0.04667799]
VBN     Result  [ 0.08677467]
VBP     Result  [-0.02616994]
VBZ     Result  [-0.0606741]
WDT     Result  [ 0.04947475]
WP  Result  [-0.03718173]
WPD     Result  [ 0.02281576]
WRB     Result  [-0.0341386]
SentenceLength  Result  [ 0.19725895]
WordCount   Result  [-0.05516646]
FunctionWordCount   Result  [ 0.07258952]
count_errors    Result  [-0.06537713]
Sentiment   Result  [ 0.09570062]
Polarity    Result  [ 0.05250223]
Result  Result  [ 1.]
