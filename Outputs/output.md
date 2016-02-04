#Linear regression Relation equation
      0.0028 * CC +
      0.0094 * CD +
      0.009  * DT +
      0.0069 * EX +
      0.0066 * IN +
      0.0058 * JJ +
      0.0131 * JJR +
      0.0154 * MD +
      0.0128 * NN +
      0.009  * NNS +
      0.0065 * NNP +
     -0.0321 * NNPS +
      0.0361 * PDT +
      0.0673 * POS +        Maybe
      0.0133 * PRP +
      0.0127 * PRPD +
      0.0024 * RB +
      0.0121 * RBR +
      0.018  * RBS +
     -0.2105 * SYM +            Quite
      0.0051 * TO +
      0.0079 * VB +
      0.0046 * VBG +
     -0.0033 * VBN +
      0.0037 * VBP +
      0.006  * VBZ +
      0.0218 * WP +
      0.0139 * WRB +
     -0.0026 * SentenceLength +
     -0.0047 * WordCount +
     -0.0065 * FunctionWordCount +
      0.0059 * count_errors +
     -0.0075 * Sentiment +
     -0.0585 * Polarity +         Kindof
      1.7553


      Correlation coefficient                  0.4166
Mean absolute error                      0.1439
Root mean squared error                  0.2379
Relative absolute error                107.554  %
Root relative squared error             90.9688 %
Total Number of Instances             1680 



#MultiLayer Perceptron


=== Classifier model (full training set) ===

Linear Node 0
    Inputs    Weights
    Threshold    -1.0539430774021439
    Node 1    2.041582967465451
    Node 2    2.178789808456167
    Node 3    1.8852250247830957
    Node 4    1.8965718208557338
    Node 5    1.9277326432206814
    Node 6    2.1436867544524074
    Node 7    2.4946377140396985
    Node 8    2.2328374934245643
    Node 9    0.30750496832198976
    Node 10    -2.1744485816729533
    Node 11    1.9709178083322176
    Node 12    2.5693230936084688
    Node 13    0.11389722180961162
    Node 14    2.728723492368364
    Node 15    1.9841610555027005
    Node 16    2.6705048190724874
    Node 17    1.7245902841673992
    Node 18    2.215365230234076
    Node 19    2.6529032375316928
    Node 20    1.851427296964324
    Node 21    -2.175169983540904
Sigmoid Node 1
    Inputs    Weights
    Threshold    -3.0878028695506066
    Attrib CC    -8.434400281696298
    Attrib CD    2.75055927757364
    Attrib DT    1.709101297283541
    Attrib EX    0.9997383341416665
    Attrib FW    4.476553750591863
    Attrib IN    3.6099818911226613
    Attrib JJ    5.702425940686859
    Attrib JJR    -8.598552954642416
    Attrib JJS    2.547517052535013
    Attrib LS    -0.008461847366320087
    Attrib MD    2.765179956646502
    Attrib NN    -3.3216087951525237
    Attrib NNS    -11.217867696476961
    Attrib NNP    -0.657996691202375
    Attrib NNPS    -1.9397707015206593
    Attrib PDT    -7.652072378112516
    Attrib POS    1.603152164840972
    Attrib PRP    -2.662361601174499
    Attrib PRPD    -1.5169279807671616
    Attrib RB    -6.698704783047356
    Attrib RBR    0.8382082581929217
    Attrib RBS    -4.874793179560628
    Attrib RP    8.725675788261107
    Attrib SYM    2.3366953646596196
    Attrib TO    3.9936221989251965
    Attrib UH    2.7990840233595558
    Attrib VB    1.6462089272286955
    Attrib VBD    -0.6967350235759391
    Attrib VBG    2.080429854112798
    Attrib VBN    2.006181915449753
    Attrib VBP    -0.152727182437949
    Attrib VBZ    -8.828929733491288
    Attrib WDT    3.3883248715255934
    Attrib WP    5.7763267229277995
    Attrib WPD    -0.802094468304978
    Attrib WRB    -2.5946125355147176
    Attrib SentenceLength    27.579265998867957
    Attrib WordCount    -3.9539840070991397
    Attrib FunctionWordCount    -6.669585388410366
    Attrib count_errors    -0.3525915825933806
    Attrib Sentiment    3.0703090317073323
    Attrib Polarity    -0.27858309188224434
Sigmoid Node 2
    Inputs    Weights
    Threshold    -7.1443301406037945
    Attrib CC    7.900972304399978
    Attrib CD    -1.0841364064792247
    Attrib DT    7.421919915562412
    Attrib EX    -9.124937512660093
    Attrib FW    -4.1457735297919545
    Attrib IN    -1.771013080096092
    Attrib JJ    1.8434637848825002
    Attrib JJR    1.0717451505075577
    Attrib JJS    3.752714898251158
    Attrib LS    -0.03715380956424044
    Attrib MD    4.231240303161838
    Attrib NN    -6.476056218466233
    Attrib NNS    -11.87828172917261
    Attrib NNP    1.8613243314455865
    Attrib NNPS    4.0926841720787275
    Attrib PDT    -3.171448141253695
    Attrib POS    6.177368135051465
    Attrib PRP    10.071611343509442
    Attrib PRPD    0.5533339799924637
    Attrib RB    -10.261193183537925
    Attrib RBR    3.1448941483847017
    Attrib RBS    1.3479428464300318
    Attrib RP    -4.68863180692003
    Attrib SYM    4.455589893837327
    Attrib TO    -3.1519100714417183
    Attrib UH    3.69455957222893
    Attrib VB    -0.5674706112255357
    Attrib VBD    -0.508103861597723
    Attrib VBG    4.920580911171463
    Attrib VBN    3.840436462549315
    Attrib VBP    -2.3399234177267427
    Attrib VBZ    1.83530313020233
    Attrib WDT    -3.2226246663287506
    Attrib WP    -2.9372232532285634
    Attrib WPD    3.0626214186508363
    Attrib WRB    -6.13386987474698
    Attrib SentenceLength    3.8402620886843915
    Attrib WordCount    -4.951605990413353
    Attrib FunctionWordCount    3.8513835349257763
    Attrib count_errors    1.9989255341045076
    Attrib Sentiment    5.062672733070135
    Attrib Polarity    -3.379112661376416
Sigmoid Node 3
    Inputs    Weights
    Threshold    -1.9177185331309634
    Attrib CC    -2.3639879737018217
    Attrib CD    1.6000039636566419
    Attrib DT    1.638641979879693
    Attrib EX    -1.5921701252854257
    Attrib FW    0.5581688571394675
    Attrib IN    -3.3140418568277976
    Attrib JJ    -3.0527119109735135
    Attrib JJR    -2.4596151256289085
    Attrib JJS    4.945665505925791
    Attrib LS    -0.03256681339813686
    Attrib MD    -4.9125416907955275
    Attrib NN    -2.504861421637636
    Attrib NNS    -0.03622181476053144
    Attrib NNP    -1.139883535516222
    Attrib NNPS    4.5653153900350665
    Attrib PDT    -0.6541038080488385
    Attrib POS    0.19995952932167502
    Attrib PRP    -1.2398649450957353
    Attrib PRPD    3.005894558834363
    Attrib RB    5.955592358729088
    Attrib RBR    0.11035346518665204
    Attrib RBS    -1.123009489713
    Attrib RP    -6.06148729251527
    Attrib SYM    1.2763375915101862
    Attrib TO    1.5456901819818267
    Attrib UH    2.2900853724378782
    Attrib VB    -2.6203434570521558
    Attrib VBD    6.059123131043881
    Attrib VBG    6.072985585739278
    Attrib VBN    4.539689878425552
    Attrib VBP    -0.5500202206862607
    Attrib VBZ    -1.8269968177544622
    Attrib WDT    -1.1096482075280811
    Attrib WP    1.963547148806943
    Attrib WPD    0.4551760763914798
    Attrib WRB    3.41245859430389
    Attrib SentenceLength    1.402546534246831
    Attrib WordCount    -1.6228405015325091
    Attrib FunctionWordCount    -2.316543089214582
    Attrib count_errors    1.2398904753879825
    Attrib Sentiment    -0.6629536712499045
    Attrib Polarity    0.7736602450769102
Sigmoid Node 4
    Inputs    Weights
    Threshold    -1.2726392282511385
    Attrib CC    2.977122532404136
    Attrib CD    -0.5285420759268754
    Attrib DT    0.27680962397812847
    Attrib EX    -0.020324523573522636
    Attrib FW    0.8862843900246861
    Attrib IN    3.9129859270799234
    Attrib JJ    -3.5356297266409
    Attrib JJR    1.314855795891836
    Attrib JJS    5.330169661910129
    Attrib LS    0.001479814806517113
    Attrib MD    -0.07137364431212113
    Attrib NN    -0.23837827542841342
    Attrib NNS    3.091184302450953
    Attrib NNP    1.3406058401609755
    Attrib NNPS    -1.1655787611066073
    Attrib PDT    3.1055699012303912
    Attrib POS    0.26540268004810774
    Attrib PRP    -1.7928772419775827
    Attrib PRPD    -2.427928006160279
    Attrib RB    0.17878986008300257
    Attrib RBR    -1.334138070338945
    Attrib RBS    0.034026765880070295
    Attrib RP    -1.5290576370729765
    Attrib SYM    0.4408349933749667
    Attrib TO    -2.6191375795968694
    Attrib UH    1.1725747102988628
    Attrib VB    -1.7754135233465678
    Attrib VBD    2.1632231552719525
    Attrib VBG    -3.2715170505263633
    Attrib VBN    2.3196359283275196
    Attrib VBP    -0.9582227990635486
    Attrib VBZ    -2.1177002403973355
    Attrib WDT    2.815509734930973
    Attrib WP    -1.4586253582380353
    Attrib WPD    0.27634835931449847
    Attrib WRB    0.6853173622459565
    Attrib SentenceLength    4.58055903370997
    Attrib WordCount    -0.705480862602411
    Attrib FunctionWordCount    1.2612652905248782
    Attrib count_errors    1.3535928193083866
    Attrib Sentiment    0.5894917954457501
    Attrib Polarity    2.437395432029162
Sigmoid Node 5
    Inputs    Weights
    Threshold    -1.274603056730769
    Attrib CC    3.033447489198256
    Attrib CD    -0.0411035218744918
    Attrib DT    -0.4887936648315819
    Attrib EX    0.13722476351156004
    Attrib FW    -0.3760529738755414
    Attrib IN    2.2751635750555885
    Attrib JJ    5.930670317210652
    Attrib JJR    5.632679326496753
    Attrib JJS    1.2298559921481218
    Attrib LS    0.01415922613522086
    Attrib MD    -0.6339877534060986
    Attrib NN    -1.4147400023288237
    Attrib NNS    4.671851578263839
    Attrib NNP    -1.2005588127076745
    Attrib NNPS    0.563299463254397
    Attrib PDT    -1.477721754636138
    Attrib POS    0.3459681148560867
    Attrib PRP    4.32428495203616
    Attrib PRPD    4.674274291532383
    Attrib RB    0.6258545564625776
    Attrib RBR    0.03527570446765647
    Attrib RBS    0.22640211108934952
    Attrib RP    -2.4210392529213953
    Attrib SYM    0.5952836633743839
    Attrib TO    1.1215283327347432
    Attrib UH    1.4931626658774255
    Attrib VB    0.5853694225279031
    Attrib VBD    4.853693800534822
    Attrib VBG    -0.04816476798124035
    Attrib VBN    -3.887781773791068
    Attrib VBP    3.699000318272206
    Attrib VBZ    1.5648357187223105
    Attrib WDT    -0.5915097449112829
    Attrib WP    -3.2476422040503232
    Attrib WPD    0.8225247572253538
    Attrib WRB    1.6667931790419404
    Attrib SentenceLength    0.6256533220786573
    Attrib WordCount    2.530167768835649
    Attrib FunctionWordCount    2.918926618519381
    Attrib count_errors    -1.120959776932045
    Attrib Sentiment    1.0201758194000452
    Attrib Polarity    -0.23254614657202374
Sigmoid Node 6
    Inputs    Weights
    Threshold    -8.433907281261403
    Attrib CC    8.93000834736839
    Attrib CD    0.02991498227607681
    Attrib DT    1.5847503617565288
    Attrib EX    -0.30300298700518313
    Attrib FW    -5.311613532098839
    Attrib IN    -2.8960836464379
    Attrib JJ    -6.477580914091762
    Attrib JJR    -6.2215400628344515
    Attrib JJS    1.8669233427489003
    Attrib LS    0.03466321424627167
    Attrib MD    5.386503275450511
    Attrib NN    0.02499675959168977
    Attrib NNS    0.18386205796794478
    Attrib NNP    2.474260183404152
    Attrib NNPS    4.128769049656002
    Attrib PDT    5.287825036329203
    Attrib POS    -0.09906779045442955
    Attrib PRP    6.379322221938857
    Attrib PRPD    0.48704194108902366
    Attrib RB    -1.0574387823712492
    Attrib RBR    -2.1397638243277224
    Attrib RBS    2.953970881743529
    Attrib RP    -1.0751874606222867
    Attrib SYM    3.088704281251621
    Attrib TO    0.8284966570239588
    Attrib UH    4.487795039861526
    Attrib VB    -8.33368364535461
    Attrib VBD    -2.997781016289884
    Attrib VBG    4.284636294804436
    Attrib VBN    -6.623126578186645
    Attrib VBP    0.7383873294912238
    Attrib VBZ    3.232061213075141
    Attrib WDT    -3.915311084653547
    Attrib WP    -5.562639735347138
    Attrib WPD    1.9565633630333288
    Attrib WRB    0.007153866791572714
    Attrib SentenceLength    -0.7376088767191504
    Attrib WordCount    -4.67525230460669
    Attrib FunctionWordCount    1.4057639891606097
    Attrib count_errors    3.718895867652713
    Attrib Sentiment    4.750496565463029
    Attrib Polarity    -0.1743783985972638
Sigmoid Node 7
    Inputs    Weights
    Threshold    -1.9356144086367117
    Attrib CC    3.3377974867725695
    Attrib CD    0.6068784814081866
    Attrib DT    -0.263300910789604
    Attrib EX    3.859187478714638
    Attrib FW    0.46023160707099137
    Attrib IN    2.0281681440586117
    Attrib JJ    -0.2730371546839574
    Attrib JJR    0.15390560100583295
    Attrib JJS    1.182091803539732
    Attrib LS    -0.025751525529424103
    Attrib MD    -2.184479971432545
    Attrib NN    -3.1079985384479993
    Attrib NNS    0.1264654855940649
    Attrib NNP    -8.511793691733972
    Attrib NNPS    -1.3873398296819635
    Attrib PDT    -1.3263876022374992
    Attrib POS    -0.023989039564277673
    Attrib PRP    4.649492851096253
    Attrib PRPD    2.333606163341893
    Attrib RB    8.354857278240631
    Attrib RBR    3.616841911813659
    Attrib RBS    2.9768586293606742
    Attrib RP    0.71841046157707
    Attrib SYM    1.3565054567966877
    Attrib TO    8.311341660395955
    Attrib UH    2.365927129332874
    Attrib VB    -6.535197780079939
    Attrib VBD    0.08981394569951676
    Attrib VBG    -0.04099422839887926
    Attrib VBN    -1.1040046267771315
    Attrib VBP    -3.6337036501544753
    Attrib VBZ    6.261999765098464
    Attrib WDT    -0.014505466946720426
    Attrib WP    -0.002935176455346518
    Attrib WPD    1.0255241733731402
    Attrib WRB    -1.0621731088888344
    Attrib SentenceLength    2.722795674959978
    Attrib WordCount    -0.5439527104710447
    Attrib FunctionWordCount    0.6795184022285892
    Attrib count_errors    -1.547971506062166
    Attrib Sentiment    1.8383582610503963
    Attrib Polarity    -3.7556651725661654
Sigmoid Node 8
    Inputs    Weights
    Threshold    -3.089461955590551
    Attrib CC    -0.9436378405652116
    Attrib CD    0.5824434044878798
    Attrib DT    -0.5066533337507388
    Attrib EX    -1.4445049034849695
    Attrib FW    1.6387470499439911
    Attrib IN    3.81807988307661
    Attrib JJ    -1.9882837004166247
    Attrib JJR    -0.3422695150037698
    Attrib JJS    3.323933008213463
    Attrib LS    0.019248667876885256
    Attrib MD    0.611339190749104
    Attrib NN    -0.048178664541034526
    Attrib NNS    -3.1354433964211874
    Attrib NNP    4.274724797664943
    Attrib NNPS    -0.8630746106088042
    Attrib PDT    0.40742779975914944
    Attrib POS    2.172914310429995
    Attrib PRP    0.09984356867730083
    Attrib PRPD    2.5673344511292955
    Attrib RB    -1.9115787827548985
    Attrib RBR    -0.7108072716238852
    Attrib RBS    0.5419422614274015
    Attrib RP    -3.2642506980044663
    Attrib SYM    0.9195264384054201
    Attrib TO    4.433510169930196
    Attrib UH    6.001749794031578
    Attrib VB    0.26724084682310406
    Attrib VBD    -3.0459981560518066
    Attrib VBG    -1.1749833894078983
    Attrib VBN    7.962153654465494
    Attrib VBP    1.095366963748571
    Attrib VBZ    2.2450084426944596
    Attrib WDT    1.9719240773994307
    Attrib WP    3.210312997741887
    Attrib WPD    0.5057425260581592
    Attrib WRB    -2.8471443753568044
    Attrib SentenceLength    -0.7088517108577902
    Attrib WordCount    -0.45278485553329656
    Attrib FunctionWordCount    -1.580149795324019
    Attrib count_errors    -2.7683682059591166
    Attrib Sentiment    2.20395883270434
    Attrib Polarity    3.1689824799027018
Sigmoid Node 9
    Inputs    Weights
    Threshold    -4.604014978070512
    Attrib CC    -1.8407489455933754
    Attrib CD    2.017442162058232
    Attrib DT    -0.8879433311170623
    Attrib EX    0.37272188995059513
    Attrib FW    1.088920998474769
    Attrib IN    1.8383225410869903
    Attrib JJ    -0.24349015827831663
    Attrib JJR    1.998939852430987
    Attrib JJS    -0.5312836599058882
    Attrib LS    -0.01959232191974345
    Attrib MD    2.199883618998734
    Attrib NN    4.072744224034677
    Attrib NNS    -0.651794593593093
    Attrib NNP    -0.8833987605257398
    Attrib NNPS    -1.6216985396152364
    Attrib PDT    -0.18528790695381156
    Attrib POS    0.7420529629783419
    Attrib PRP    0.7417324762762173
    Attrib PRPD    0.531134360060488
    Attrib RB    -0.13304759137660496
    Attrib RBR    -0.7424766523428465
    Attrib RBS    -1.0022626621172364
    Attrib RP    -0.48794104490608337
    Attrib SYM    1.4921607995725048
    Attrib TO    1.183552747883895
    Attrib UH    -0.08396038609400158
    Attrib VB    0.5459310618795976
    Attrib VBD    -3.1008276559015235
    Attrib VBG    -0.24871753383342532
    Attrib VBN    0.5288100537192616
    Attrib VBP    1.863720023755771
    Attrib VBZ    1.4408892138841571
    Attrib WDT    -0.4938567011355111
    Attrib WP    0.7122792840376053
    Attrib WPD    -0.2844466482331974
    Attrib WRB    0.6296581617471066
    Attrib SentenceLength    -3.4541903290021327
    Attrib WordCount    -0.6492025395790211
    Attrib FunctionWordCount    -5.860739030794299
    Attrib count_errors    -0.6338462035219803
    Attrib Sentiment    -0.3553314315381465
    Attrib Polarity    -0.4965922481087925
Sigmoid Node 10
    Inputs    Weights
    Threshold    -3.7253752417127033
    Attrib CC    -3.3971567147354227
    Attrib CD    -8.398143341071059
    Attrib DT    2.580538819269546
    Attrib EX    -0.8291258978523088
    Attrib FW    1.1732533828612344
    Attrib IN    -3.4254080807799387
    Attrib JJ    1.6448938909565027
    Attrib JJR    4.265337998413974
    Attrib JJS    9.915498004252546
    Attrib LS    0.012283747163399361
    Attrib MD    3.9910817232209927
    Attrib NN    2.9871652199323413
    Attrib NNS    4.111659878517882
    Attrib NNP    1.5254142312771195
    Attrib NNPS    0.33418409829267304
    Attrib PDT    1.6558493794835683
    Attrib POS    2.252525747297735
    Attrib PRP    3.0530782761880944
    Attrib PRPD    -0.07474697115985118
    Attrib RB    11.20780832601081
    Attrib RBR    -4.10899459630463
    Attrib RBS    -1.523213062999422
    Attrib RP    -8.220541392849706
    Attrib SYM    6.007503247794812
    Attrib TO    5.815647547325891
    Attrib UH    3.8628699925737124
    Attrib VB    -0.28951281336073803
    Attrib VBD    -1.9893506625378146
    Attrib VBG    -0.5489360186167864
    Attrib VBN    11.255327449806018
    Attrib VBP    1.6427118190074355
    Attrib VBZ    5.660107849644966
    Attrib WDT    5.817599353641662
    Attrib WP    -7.736878888667732
    Attrib WPD    0.02437209078258642
    Attrib WRB    -1.8684491181518772
    Attrib SentenceLength    4.038644094979066
    Attrib WordCount    1.9864916626649622
    Attrib FunctionWordCount    -5.741133927284168
    Attrib count_errors    -2.169510981210735
    Attrib Sentiment    4.854241600716592
    Attrib Polarity    0.2515767189691842
Sigmoid Node 11
    Inputs    Weights
    Threshold    -5.369040741420526
    Attrib CC    -0.7203933412852638
    Attrib CD    1.8865348215462352
    Attrib DT    4.931234473748555
    Attrib EX    -6.344375678568054
    Attrib FW    -0.461155609007211
    Attrib IN    -0.6578423045653964
    Attrib JJ    -2.3532147173441733
    Attrib JJR    -1.457270807746592
    Attrib JJS    1.329771555126091
    Attrib LS    0.034428892820551255
    Attrib MD    2.072244466649586
    Attrib NN    0.4895539309474687
    Attrib NNS    4.5552223941314605
    Attrib NNP    -0.14875783523447544
    Attrib NNPS    0.7750507336972321
    Attrib PDT    -0.7046500208841143
    Attrib POS    2.9857955572836268
    Attrib PRP    2.80972911552139
    Attrib PRPD    -2.7348857296206193
    Attrib RB    1.4931462604861407
    Attrib RBR    4.423800933623517
    Attrib RBS    -2.227431726313683
    Attrib RP    4.281061824107739
    Attrib SYM    4.060069877417071
    Attrib TO    -1.886019568407936
    Attrib UH    2.8302860263741443
    Attrib VB    0.6235280026138214
    Attrib VBD    1.5927622667666512
    Attrib VBG    1.7398936464716972
    Attrib VBN    -0.8030277980277155
    Attrib VBP    -2.7716619051218516
    Attrib VBZ    2.1554953880660137
    Attrib WDT    0.5484365157206356
    Attrib WP    -2.0259695388056884
    Attrib WPD    2.303124906636324
    Attrib WRB    -4.139183160245665
    Attrib SentenceLength    0.24814681229889748
    Attrib WordCount    -1.3932096604774566
    Attrib FunctionWordCount    -4.694755874220912
    Attrib count_errors    -1.5680182347564062
    Attrib Sentiment    -10.590760005697835
    Attrib Polarity    5.2407611889183086
Sigmoid Node 12
    Inputs    Weights
    Threshold    -1.8423751498586218
    Attrib CC    -1.7611631894731958
    Attrib CD    2.0142589111950016
    Attrib DT    3.0401157455605703
    Attrib EX    -1.4597858596898183
    Attrib FW    0.5259718927337121
    Attrib IN    -1.4705714800797378
    Attrib JJ    3.85376875507896
    Attrib JJR    4.455929505520896
    Attrib JJS    -2.4315629025679533
    Attrib LS    -0.042921455911752365
    Attrib MD    3.256165228199423
    Attrib NN    -1.8821784377432085
    Attrib NNS    -0.48030477021863754
    Attrib NNP    2.3001868858623418
    Attrib NNPS    -0.8165125270200612
    Attrib PDT    -1.7770923444126236
    Attrib POS    1.1677974629822025
    Attrib PRP    3.578274456289417
    Attrib PRPD    1.7176286180323148
    Attrib RB    -4.74248445600445
    Attrib RBR    5.847402130815282
    Attrib RBS    2.6742140249070836
    Attrib RP    -4.69074831060815
    Attrib SYM    1.455843068494444
    Attrib TO    0.10995914629234617
    Attrib UH    1.3014012161778155
    Attrib VB    -1.5976978181106862
    Attrib VBD    -4.1318111980488945
    Attrib VBG    0.2401030378317818
    Attrib VBN    4.445842553963517
    Attrib VBP    -0.3028078065138598
    Attrib VBZ    0.21403535609572136
    Attrib WDT    -1.1594939088910283
    Attrib WP    6.397746764495262
    Attrib WPD    3.051277768528736
    Attrib WRB    -0.6948347941076192
    Attrib SentenceLength    -0.17350801307921979
    Attrib WordCount    -0.4823180766624918
    Attrib FunctionWordCount    -2.677549953399328
    Attrib count_errors    -2.9046114257072495
    Attrib Sentiment    -0.050558003149693456
    Attrib Polarity    -3.380785042965586
Sigmoid Node 13
    Inputs    Weights
    Threshold    -0.9615623942941652
    Attrib CC    0.13367223801224762
    Attrib CD    -1.5649303366034082
    Attrib DT    0.19979650020783124
    Attrib EX    -3.607865019069143
    Attrib FW    0.7840184442207555
    Attrib IN    1.4860073722212122
    Attrib JJ    2.991553524094841
    Attrib JJR    -1.0334393944239364
    Attrib JJS    -0.5567700379014868
    Attrib LS    0.007384251072120519
    Attrib MD    -1.5522892117144205
    Attrib NN    -0.8537369574342983
    Attrib NNS    2.154467603185561
    Attrib NNP    -0.4329693913268223
    Attrib NNPS    1.8535033928806062
    Attrib PDT    -1.2521370863574
    Attrib POS    0.8337027692608662
    Attrib PRP    -1.7262794048494918
    Attrib PRPD    -0.5329079969780643
    Attrib RB    2.055636222599854
    Attrib RBR    1.6194516521421163
    Attrib RBS    0.9840010742772191
    Attrib RP    4.9088208963674065
    Attrib SYM    0.2231633223446532
    Attrib TO    0.7337692975128625
    Attrib UH    0.7709616708130229
    Attrib VB    -0.05402846607313651
    Attrib VBD    0.6858323116324913
    Attrib VBG    -0.34346206426859704
    Attrib VBN    -0.35870209842308753
    Attrib VBP    -0.5340157815569074
    Attrib VBZ    -1.8250821066217693
    Attrib WDT    4.897392036949286
    Attrib WP    0.5247651417111361
    Attrib WPD    0.10236263574475625
    Attrib WRB    -0.501812845144269
    Attrib SentenceLength    2.861395925370036
    Attrib WordCount    -0.006768548465266725
    Attrib FunctionWordCount    -0.5911533343968965
    Attrib count_errors    1.6964687439920187
    Attrib Sentiment    0.6588987944087995
    Attrib Polarity    1.0712754147521513
Sigmoid Node 14
    Inputs    Weights
    Threshold    -2.379365040589718
    Attrib CC    6.813951329216158
    Attrib CD    3.1609339211506184
    Attrib DT    -0.6828343472426189
    Attrib EX    -0.6343804587139276
    Attrib FW    -0.12201894330952633
    Attrib IN    -4.424828392452367
    Attrib JJ    -11.206699177139651
    Attrib JJR    -2.094599313786702
    Attrib JJS    -0.19656104113079917
    Attrib LS    -0.03698263931489069
    Attrib MD    0.625001818833584
    Attrib NN    -4.633761719140358
    Attrib NNS    -1.9675027143860142
    Attrib NNP    3.7988232629176153
    Attrib NNPS    1.331473080643041
    Attrib PDT    6.3319448217147425
    Attrib POS    1.6933863346463707
    Attrib PRP    5.2715611045302735
    Attrib PRPD    4.628549478425153
    Attrib RB    -4.180165254509464
    Attrib RBR    1.8600886691210141
    Attrib RBS    -0.34799742850821175
    Attrib RP    -5.155662822773963
    Attrib SYM    1.6965940067486023
    Attrib TO    0.8513740856100017
    Attrib UH    0.9439567551048313
    Attrib VB    6.065135562906697
    Attrib VBD    1.6172976296493247
    Attrib VBG    0.28196131932710927
    Attrib VBN    -6.05825193144975
    Attrib VBP    -5.031606665254362
    Attrib VBZ    3.033301692100716
    Attrib WDT    3.01468762785429
    Attrib WP    0.6456270545046338
    Attrib WPD    1.4797342686243404
    Attrib WRB    -0.16006427946788182
    Attrib SentenceLength    -2.1607635116831667
    Attrib WordCount    -2.9504129039088527
    Attrib FunctionWordCount    -2.423372945436543
    Attrib count_errors    4.396009759840112
    Attrib Sentiment    1.504890465428928
    Attrib Polarity    -4.505468427527705
Sigmoid Node 15
    Inputs    Weights
    Threshold    -6.689215406460197
    Attrib CC    2.518792309945486
    Attrib CD    4.6506808684974486
    Attrib DT    0.5182455012776511
    Attrib EX    2.32433904148913
    Attrib FW    0.30083679673797925
    Attrib IN    5.462919635815421
    Attrib JJ    -5.421436816194348
    Attrib JJR    -0.7550248533297876
    Attrib JJS    2.57695843835219
    Attrib LS    0.015724658582866355
    Attrib MD    1.911263016667331
    Attrib NN    -1.4474820327764348
    Attrib NNS    3.0387801839897044
    Attrib NNP    -3.0690965829338013
    Attrib NNPS    1.9375858078441057
    Attrib PDT    -1.2929323252255343
    Attrib POS    3.6274341224165023
    Attrib PRP    -4.6937940117776105
    Attrib PRPD    -0.174092359864664
    Attrib RB    1.3961353325921066
    Attrib RBR    1.2958576248494924
    Attrib RBS    -3.961038325066889
    Attrib RP    4.386136824686859
    Attrib SYM    2.5654888066512
    Attrib TO    -7.112535686654649
    Attrib UH    4.021170789354014
    Attrib VB    -1.5579348316374422
    Attrib VBD    1.2206288489796226
    Attrib VBG    -4.510151627310356
    Attrib VBN    4.317987303326009
    Attrib VBP    -0.2733113692284448
    Attrib VBZ    -7.1846000440729405
    Attrib WDT    -0.849517804159898
    Attrib WP    -2.9432309260655063
    Attrib WPD    1.6323304296018244
    Attrib WRB    -6.927815428913401
    Attrib SentenceLength    3.7057634738846263
    Attrib WordCount    -4.733947737946497
    Attrib FunctionWordCount    -3.501918868852928
    Attrib count_errors    3.411627037113006
    Attrib Sentiment    1.4012189322178132
    Attrib Polarity    -4.45459778050922
Sigmoid Node 16
    Inputs    Weights
    Threshold    -1.778563610852364
    Attrib CC    -0.08520206464119069
    Attrib CD    3.1939843554051905
    Attrib DT    5.927707706256061
    Attrib EX    1.8899394493418555
    Attrib FW    1.8570438234956066
    Attrib IN    -1.5994089656163086
    Attrib JJ    -6.067905142725519
    Attrib JJR    -0.858315344085962
    Attrib JJS    3.898145236749016
    Attrib LS    -0.008829412260180705
    Attrib MD    1.9835459755241005
    Attrib NN    -5.653017641608758
    Attrib NNS    5.296931644942171
    Attrib NNP    -3.670734864641672
    Attrib NNPS    -0.539708525954844
    Attrib PDT    0.15398204327078238
    Attrib POS    -0.5507572160998634
    Attrib PRP    10.172805225547782
    Attrib PRPD    -1.6097761449472354
    Attrib RB    0.414209040895775
    Attrib RBR    5.339361052300316
    Attrib RBS    0.3810310194786685
    Attrib RP    -0.231776613582399
    Attrib SYM    1.2724770917209878
    Attrib TO    -5.893707034403292
    Attrib UH    1.9129564110490767
    Attrib VB    -1.8911436960657368
    Attrib VBD    2.610634693915916
    Attrib VBG    0.7942678825072357
    Attrib VBN    -1.9367891890352658
    Attrib VBP    -3.4327905231549463
    Attrib VBZ    -3.48583475497202
    Attrib WDT    5.613874964377623
    Attrib WP    -0.3646537273867194
    Attrib WPD    0.8192221265364367
    Attrib WRB    -0.5958519819634946
    Attrib SentenceLength    0.30369565394298637
    Attrib WordCount    -1.774345021496452
    Attrib FunctionWordCount    0.7109389909645601
    Attrib count_errors    0.5269136916490632
    Attrib Sentiment    3.4813879191026738
    Attrib Polarity    3.7401442303969796
Sigmoid Node 17
    Inputs    Weights
    Threshold    -7.621621408327737
    Attrib CC    -3.8005765533179448
    Attrib CD    0.326717477348238
    Attrib DT    -4.149735643767012
    Attrib EX    -6.775838491055403
    Attrib FW    0.1456357590229292
    Attrib IN    -2.4073138076269185
    Attrib JJ    -6.612342250395958
    Attrib JJR    -2.2418113219431857
    Attrib JJS    7.294114653197981
    Attrib LS    -0.048258523006278066
    Attrib MD    2.2027076545716566
    Attrib NN    -7.419104901780372
    Attrib NNS    3.791752378906367
    Attrib NNP    -10.353462637374834
    Attrib NNPS    1.5107359042349884
    Attrib PDT    1.97313469868399
    Attrib POS    3.578275056404078
    Attrib PRP    -2.525639060832779
    Attrib PRPD    -4.706102869837329
    Attrib RB    11.339773630544888
    Attrib RBR    -4.235847043075539
    Attrib RBS    4.721335513711716
    Attrib RP    7.9235434497294035
    Attrib SYM    6.359429376190736
    Attrib TO    2.399810985854495
    Attrib UH    5.841422007436424
    Attrib VB    2.174262828887585
    Attrib VBD    1.8140195016522473
    Attrib VBG    8.930423411789404
    Attrib VBN    0.2919404244112121
    Attrib VBP    -0.6498624048641675
    Attrib VBZ    1.2792505693095981
    Attrib WDT    0.5160182477897627
    Attrib WP    4.808976651539027
    Attrib WPD    -1.1178560647029128
    Attrib WRB    -5.440095294518346
    Attrib SentenceLength    3.0550211759192956
    Attrib WordCount    -6.358008308144956
    Attrib FunctionWordCount    -5.93447638238857
    Attrib count_errors    0.8912292223964716
    Attrib Sentiment    -3.013697949746859
    Attrib Polarity    3.572656356897257
Sigmoid Node 18
    Inputs    Weights
    Threshold    -2.562571832391838
    Attrib CC    1.625780682785747
    Attrib CD    5.029947435032053
    Attrib DT    3.0852139600082755
    Attrib EX    0.7578209003132464
    Attrib FW    0.48237573825451757
    Attrib IN    -2.2631577013702255
    Attrib JJ    -7.86250907050265
    Attrib JJR    -4.829745785025867
    Attrib JJS    2.2765522779074847
    Attrib LS    -0.010802511751247523
    Attrib MD    5.0048939633199305
    Attrib NN    2.029301480305372
    Attrib NNS    4.2232435269830315
    Attrib NNP    -1.2186205039651214
    Attrib NNPS    2.1144425152887614
    Attrib PDT    1.0202947268194673
    Attrib POS    0.5707814195427917
    Attrib PRP    2.1455539356587034
    Attrib PRPD    0.14775613470094112
    Attrib RB    -7.556036078991608
    Attrib RBR    -3.203465319438065
    Attrib RBS    4.425371752459668
    Attrib RP    0.8216728946864573
    Attrib SYM    1.768268088191889
    Attrib TO    3.0389172275333927
    Attrib UH    1.3990269018121304
    Attrib VB    4.713768729784448
    Attrib VBD    1.1728676397913225
    Attrib VBG    -2.9409372017921593
    Attrib VBN    0.05983198326361822
    Attrib VBP    -0.6013628291497718
    Attrib VBZ    2.198840303946055
    Attrib WDT    -1.4680551191283833
    Attrib WP    5.121219497182971
    Attrib WPD    0.7179737078923156
    Attrib WRB    4.8203110214008
    Attrib SentenceLength    -2.2491073161636486
    Attrib WordCount    0.13903688922733484
    Attrib FunctionWordCount    -4.472033680717326
    Attrib count_errors    -6.063094079819644
    Attrib Sentiment    -3.0414506178461918
    Attrib Polarity    -1.2217403017356527
Sigmoid Node 19
    Inputs    Weights
    Threshold    -5.543561376731708
    Attrib CC    1.7665525291961541
    Attrib CD    1.0305625022834257
    Attrib DT    -3.1816361724734303
    Attrib EX    -5.8340362216033235
    Attrib FW    1.1916005294533998
    Attrib IN    -0.9170929532597502
    Attrib JJ    5.424744574701907
    Attrib JJR    -2.7635811925611375
    Attrib JJS    -1.2259677322060873
    Attrib LS    0.021159481200665492
    Attrib MD    1.5028533072346326
    Attrib NN    -5.532845885588307
    Attrib NNS    -0.5781219671473836
    Attrib NNP    -5.963164798570936
    Attrib NNPS    0.9601807202167876
    Attrib PDT    -1.2350012497170457
    Attrib POS    3.6066642483405804
    Attrib PRP    -4.151100962916272
    Attrib PRPD    -3.4929845277972857
    Attrib RB    3.618944604535877
    Attrib RBR    2.873928430706575
    Attrib RBS    -1.3233986244223204
    Attrib RP    4.811958970664163
    Attrib SYM    4.183992324970241
    Attrib TO    -1.4414201615038476
    Attrib UH    3.518279282918536
    Attrib VB    1.720232222746873
    Attrib VBD    -0.8758741044233971
    Attrib VBG    0.14838992099129208
    Attrib VBN    -2.3495468943845275
    Attrib VBP    -0.5660215238367021
    Attrib VBZ    1.7617919623723481
    Attrib WDT    7.725437401493215
    Attrib WP    -0.19116947643286605
    Attrib WPD    2.3109799498171566
    Attrib WRB    -0.9590986490012864
    Attrib SentenceLength    3.9323387103727394
    Attrib WordCount    -4.783066819544212
    Attrib FunctionWordCount    -7.044909998841481
    Attrib count_errors    4.2189582627197515
    Attrib Sentiment    -1.5311629705825986
    Attrib Polarity    2.6919725223761684
Sigmoid Node 20
    Inputs    Weights
    Threshold    8.75507781037071
    Attrib CC    -2.4183720255968173
    Attrib CD    9.138440674563517
    Attrib DT    1.9794392463724075
    Attrib EX    2.0076638474690096
    Attrib FW    -7.33309671338238
    Attrib IN    -12.100248831345247
    Attrib JJ    1.0165684192290922
    Attrib JJR    13.51362308404786
    Attrib JJS    -8.278711299775784
    Attrib LS    -0.04706245562822786
    Attrib MD    7.417533497110167
    Attrib NN    53.314332820780855
    Attrib NNS    13.65623181842519
    Attrib NNP    18.21536117935209
    Attrib NNPS    -7.177993418243846
    Attrib PDT    10.776231509738947
    Attrib POS    -4.4230853379144675
    Attrib PRP    16.38715048914341
    Attrib PRPD    10.91527974900271
    Attrib RB    -4.491175252119628
    Attrib RBR    2.9075577994074147
    Attrib RBS    10.388618383891949
    Attrib RP    -10.814838993957895
    Attrib SYM    -8.795469917155843
    Attrib TO    -9.618999151106916
    Attrib UH    -10.780469168028473
    Attrib VB    12.632417219441741
    Attrib VBD    -15.559735715904111
    Attrib VBG    -3.7851523836884473
    Attrib VBN    -5.309145905010951
    Attrib VBP    -7.863377279332157
    Attrib VBZ    2.0301661151509474
    Attrib WDT    -3.446752114080186
    Attrib WP    8.242604865807344
    Attrib WPD    -2.6431508180833685
    Attrib WRB    4.666387043449445
    Attrib SentenceLength    -67.50160677686186
    Attrib WordCount    25.229967720407892
    Attrib FunctionWordCount    -48.80288316166485
    Attrib count_errors    19.012873991076464
    Attrib Sentiment    -17.836953151661515
    Attrib Polarity    -2.5185037524831744
Sigmoid Node 21
    Inputs    Weights
    Threshold    -1.2132101232182326
    Attrib CC    3.4478170478160797
    Attrib CD    3.5849264566041543
    Attrib DT    -0.7794192595206714
    Attrib EX    -2.817266447224493
    Attrib FW    0.8215381625705888
    Attrib IN    1.9649217329106587
    Attrib JJ    -0.25496568564021577
    Attrib JJR    -1.1795075425075645
    Attrib JJS    -3.769240526653114
    Attrib LS    0.0026154933248371814
    Attrib MD    6.354731198579347
    Attrib NN    -1.3382731091012317
    Attrib NNS    4.9845527265020095
    Attrib NNP    2.487502389686007
    Attrib NNPS    1.6844777161032947
    Attrib PDT    -2.860269186783858
    Attrib POS    0.15205672060452002
    Attrib PRP    1.4771567624810582
    Attrib PRPD    -4.023895483346751
    Attrib RB    -0.4208321418919344
    Attrib RBR    -0.43757831588086615
    Attrib RBS    -0.5301911210117447
    Attrib RP    8.09077706386028
    Attrib SYM    1.5784197849533055
    Attrib TO    -1.4305154517684957
    Attrib UH    3.7141978331118097
    Attrib VB    0.806182748152151
    Attrib VBD    1.3395898294253075
    Attrib VBG    1.7733209724672687
    Attrib VBN    4.486160109102308
    Attrib VBP    4.262355542794677
    Attrib VBZ    -1.7073650455463838
    Attrib WDT    4.235740842333239
    Attrib WP    -7.038068504508648
    Attrib WPD    2.6866571198194475
    Attrib WRB    -0.955949647664177
    Attrib SentenceLength    2.721338377050385
    Attrib WordCount    1.4670492646902655
    Attrib FunctionWordCount    2.8327607580393064
    Attrib count_errors    -3.4954839828947115
    Attrib Sentiment    1.6816611836815347
    Attrib Polarity    -1.8823482525520334
Class 
    Input
    Node 0


Time taken to build model: 67.91 seconds

=== Evaluation on test set ===
=== Summary ===

Correlation coefficient                  0.3487
Mean absolute error                      0.1552
Root mean squared error                  0.3498
Relative absolute error                115.9807 %
Root relative squared error            133.7666 %
Total Number of Instances             1680     


#Regression By Discretization


=== Classifier model (full training set) ===

Regression by discretization

Class attribute discretized into 10 values

Classifier spec: weka.classifiers.trees.J48 -C 0.25 -M 2
J48 pruned tree
------------------

SentenceLength <= 17: '(1.9-inf)' (2755.0/44.0)
SentenceLength > 17
|   NN <= 32
|   |   VB <= 24
|   |   |   EX <= 2
|   |   |   |   NNS <= 15
|   |   |   |   |   SentenceLength <= 18
|   |   |   |   |   |   WDT <= 0: '(1.9-inf)' (8.0)
|   |   |   |   |   |   WDT > 0
|   |   |   |   |   |   |   MD <= 4: '(-inf-1.1]' (4.0)
|   |   |   |   |   |   |   MD > 4
|   |   |   |   |   |   |   |   VBD <= 5
|   |   |   |   |   |   |   |   |   JJS <= 0: '(1.9-inf)' (9.0)
|   |   |   |   |   |   |   |   |   JJS > 0
|   |   |   |   |   |   |   |   |   |   IN <= 25: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   |   |   IN > 25: '(-inf-1.1]' (2.0)
|   |   |   |   |   |   |   |   VBD > 5: '(-inf-1.1]' (2.0)
|   |   |   |   |   SentenceLength > 18
|   |   |   |   |   |   SentenceLength <= 46
|   |   |   |   |   |   |   TO <= 4
|   |   |   |   |   |   |   |   VBD <= 4: '(1.9-inf)' (5.0)
|   |   |   |   |   |   |   |   VBD > 4: '(-inf-1.1]' (2.0)
|   |   |   |   |   |   |   TO > 4
|   |   |   |   |   |   |   |   CC <= 2: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   CC > 2
|   |   |   |   |   |   |   |   |   PRPD <= 9
|   |   |   |   |   |   |   |   |   |   PDT <= 1
|   |   |   |   |   |   |   |   |   |   |   IN <= 18: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   |   |   |   IN > 18
|   |   |   |   |   |   |   |   |   |   |   |   MD <= 12
|   |   |   |   |   |   |   |   |   |   |   |   |   count_errors <= 1
|   |   |   |   |   |   |   |   |   |   |   |   |   |   DT <= 9
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   VBP <= 12: '(-inf-1.1]' (3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   VBP > 12: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   DT > 9: '(-inf-1.1]' (86.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   count_errors > 1
|   |   |   |   |   |   |   |   |   |   |   |   |   |   CC <= 8: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   CC > 8: '(-inf-1.1]' (3.0)
|   |   |   |   |   |   |   |   |   |   |   |   MD > 12: '(1.9-inf)' (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   PDT > 1
|   |   |   |   |   |   |   |   |   |   |   RBR <= 0: '(-inf-1.1]' (5.0)
|   |   |   |   |   |   |   |   |   |   |   RBR > 0: '(1.9-inf)' (6.0/1.0)
|   |   |   |   |   |   |   |   |   PRPD > 9: '(1.9-inf)' (4.0/1.0)
|   |   |   |   |   |   SentenceLength > 46: '(1.9-inf)' (3.0)
|   |   |   |   NNS > 15
|   |   |   |   |   CC <= 6: '(1.9-inf)' (10.0)
|   |   |   |   |   CC > 6
|   |   |   |   |   |   POS <= 0
|   |   |   |   |   |   |   JJR <= 1
|   |   |   |   |   |   |   |   VBP <= 9
|   |   |   |   |   |   |   |   |   VBG <= 7: '(1.9-inf)' (10.0)
|   |   |   |   |   |   |   |   |   VBG > 7: '(-inf-1.1]' (3.0/1.0)
|   |   |   |   |   |   |   |   VBP > 9
|   |   |   |   |   |   |   |   |   Sentiment <= -6: '(1.9-inf)' (4.0)
|   |   |   |   |   |   |   |   |   Sentiment > -6
|   |   |   |   |   |   |   |   |   |   SentenceLength <= 27
|   |   |   |   |   |   |   |   |   |   |   CD <= 3: '(-inf-1.1]' (17.0)
|   |   |   |   |   |   |   |   |   |   |   CD > 3
|   |   |   |   |   |   |   |   |   |   |   |   NNP <= 3: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   NNP > 3: '(-inf-1.1]' (2.0)
|   |   |   |   |   |   |   |   |   |   SentenceLength > 27: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   JJR > 1: '(1.9-inf)' (11.0/1.0)
|   |   |   |   |   |   POS > 0: '(1.9-inf)' (2.0)
|   |   |   EX > 2: '(1.9-inf)' (11.0/1.0)
|   |   VB > 24: '(1.9-inf)' (11.0)
|   NN > 32
|   |   NN <= 42
|   |   |   SentenceLength <= 22
|   |   |   |   NNPS <= 0
|   |   |   |   |   SentenceLength <= 18
|   |   |   |   |   |   WDT <= 2: '(1.9-inf)' (75.0/1.0)
|   |   |   |   |   |   WDT > 2
|   |   |   |   |   |   |   CC <= 9: '(1.9-inf)' (13.0)
|   |   |   |   |   |   |   CC > 9: '(-inf-1.1]' (3.0)
|   |   |   |   |   SentenceLength > 18
|   |   |   |   |   |   Sentiment <= 5
|   |   |   |   |   |   |   VB <= 13
|   |   |   |   |   |   |   |   PRPD <= 3
|   |   |   |   |   |   |   |   |   RP <= 0
|   |   |   |   |   |   |   |   |   |   Polarity <= 0.18427
|   |   |   |   |   |   |   |   |   |   |   NNP <= 6: '(1.9-inf)' (17.0)
|   |   |   |   |   |   |   |   |   |   |   NNP > 6: '(-inf-1.1]' (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   Polarity > 0.18427: '(-inf-1.1]' (3.0)
|   |   |   |   |   |   |   |   |   RP > 0: '(-inf-1.1]' (7.0/1.0)
|   |   |   |   |   |   |   |   PRPD > 3: '(1.9-inf)' (15.0)
|   |   |   |   |   |   |   VB > 13: '(1.9-inf)' (102.0/4.0)
|   |   |   |   |   |   Sentiment > 5
|   |   |   |   |   |   |   VBG <= 4: '(-inf-1.1]' (7.0/1.0)
|   |   |   |   |   |   |   VBG > 4
|   |   |   |   |   |   |   |   JJ <= 17: '(-inf-1.1]' (5.0/2.0)
|   |   |   |   |   |   |   |   JJ > 17: '(1.9-inf)' (17.0/1.0)
|   |   |   |   NNPS > 0
|   |   |   |   |   PDT <= 0
|   |   |   |   |   |   CD <= 0: '(1.9-inf)' (3.0)
|   |   |   |   |   |   CD > 0: '(-inf-1.1]' (5.0/1.0)
|   |   |   |   |   PDT > 0: '(1.9-inf)' (5.0)
|   |   |   SentenceLength > 22
|   |   |   |   PDT <= 1
|   |   |   |   |   POS <= 0
|   |   |   |   |   |   NNS <= 15
|   |   |   |   |   |   |   CC <= 5: '(1.9-inf)' (9.0/1.0)
|   |   |   |   |   |   |   CC > 5
|   |   |   |   |   |   |   |   PRPD <= 9
|   |   |   |   |   |   |   |   |   Sentiment <= 5
|   |   |   |   |   |   |   |   |   |   VBN <= 5
|   |   |   |   |   |   |   |   |   |   |   JJS <= 1
|   |   |   |   |   |   |   |   |   |   |   |   JJR <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   RBR <= 1
|   |   |   |   |   |   |   |   |   |   |   |   |   |   RBR <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   PDT <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   NNP <= 2
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   JJS <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   VBZ <= 5: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   VBZ > 5
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   EX <= 0: '(-inf-1.1]' (3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   EX > 0: '(1.9-inf)' (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   JJS > 0: '(-inf-1.1]' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   NNP > 2: '(1.9-inf)' (4.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   PDT > 0: '(-inf-1.1]' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   RBR > 0: '(1.9-inf)' (3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   RBR > 1: '(-inf-1.1]' (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   JJR > 0: '(1.9-inf)' (12.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   JJS > 1: '(-inf-1.1]' (3.0)
|   |   |   |   |   |   |   |   |   |   VBN > 5: '(-inf-1.1]' (7.0)
|   |   |   |   |   |   |   |   |   Sentiment > 5
|   |   |   |   |   |   |   |   |   |   JJS <= 1: '(-inf-1.1]' (16.0)
|   |   |   |   |   |   |   |   |   |   JJS > 1: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   PRPD > 9: '(1.9-inf)' (4.0)
|   |   |   |   |   |   NNS > 15
|   |   |   |   |   |   |   NNPS <= 0: '(1.9-inf)' (22.0/1.0)
|   |   |   |   |   |   |   NNPS > 0
|   |   |   |   |   |   |   |   JJ <= 16: '(1.9-inf)' (2.0)
|   |   |   |   |   |   |   |   JJ > 16: '(-inf-1.1]' (2.0)
|   |   |   |   |   POS > 0: '(1.9-inf)' (2.0)
|   |   |   |   PDT > 1: '(1.9-inf)' (9.0)
|   |   NN > 42
|   |   |   MD <= 5
|   |   |   |   WDT <= 1: '(1.9-inf)' (105.0/8.0)
|   |   |   |   WDT > 1
|   |   |   |   |   RBS <= 0
|   |   |   |   |   |   IN <= 30: '(1.9-inf)' (16.0)
|   |   |   |   |   |   IN > 30
|   |   |   |   |   |   |   WP <= 0: '(-inf-1.1]' (6.0)
|   |   |   |   |   |   |   WP > 0
|   |   |   |   |   |   |   |   VB <= 17: '(1.9-inf)' (22.0/1.0)
|   |   |   |   |   |   |   |   VB > 17: '(-inf-1.1]' (3.0)
|   |   |   |   |   RBS > 0: '(1.9-inf)' (6.0)
|   |   |   MD > 5: '(1.9-inf)' (375.0/9.0)

Number of Leaves  :   75

Size of the tree :  149


Time taken to build model: 0.35 seconds

=== Evaluation on test set ===
=== Summary ===

Correlation coefficient                  0.4502
Mean absolute error                      0.0864
Root mean squared error                  0.2562
Relative absolute error                 64.5366 %
Root relative squared error             97.991  %
Total Number of Instances             1680   


#Additive Regression


=== Classifier model (full training set) ===

Additive Regression

ZeroR model

ZeroR predicts class value: 1.9295918367346938

Base classifier weka.classifiers.trees.DecisionStump

10 models generated.

Model number 0

Decision Stump

Classifications

SentenceLength <= 19.5 : 0.042376667202318544
SentenceLength > 19.5 : -0.18059854814411064
SentenceLength is missing : -2.701920320133672E-16


Model number 1

Decision Stump

Classifications

NN <= 31.5 : -0.13733377305512984
NN > 31.5 : 0.02293666171001105
NN is missing : -1.8517288043054469E-16


Model number 2

Decision Stump

Classifications

MD <= 6.5 : -0.0274668354041823
MD > 6.5 : 0.026857077201466767
MD is missing : 4.684957070814587E-16


Model number 3

Decision Stump

Classifications

SentenceLength <= 43.5 : -0.00179830918760094
SentenceLength > 43.5 : 0.26933138371223586
SentenceLength is missing : 1.8211056245764685E-17


Model number 4

Decision Stump

Classifications

SentenceLength <= 15.5 : 0.020026468482944357
SentenceLength > 15.5 : -0.02670195797725913
SentenceLength is missing : 5.15460690004537E-18


Model number 5

Decision Stump

Classifications

NN <= 44.5 : -0.016749194131285818
NN > 44.5 : 0.030048269157837763
NN is missing : -6.641512736596919E-18


Model number 6

Decision Stump

Classifications

Sentiment <= 5.5 : 0.008634512809605643
Sentiment > 5.5 : -0.04992481281955289
Sentiment is missing : 1.2441773093644882E-16


Model number 7

Decision Stump

Classifications

WP <= 2.5 : -0.009160446256288481
WP > 2.5 : 0.04265621943584791
WP is missing : -8.273480398512039E-17


Model number 8

Decision Stump

Classifications

FunctionWordCount <= 87.5 : 0.02108702761263159
FunctionWordCount > 87.5 : -0.014177967370950147
FunctionWordCount is missing : 6.175615574477434E-17


Model number 9

Decision Stump

Classifications

SentenceLength <= 19.5 : -0.009914178888503152
SentenceLength > 19.5 : 0.042251701974492926
SentenceLength is missing : -6.948806609484239E-17



Time taken to build model: 0.49 seconds

=== Evaluation on test set ===
=== Summary ===

Correlation coefficient                  0.4859
Mean absolute error                      0.1268
Root mean squared error                  0.2286
Relative absolute error                 94.7488 %
Root relative squared error             87.4432 %
Total Number of Instances             1680     



#Conjugative Rule

=== Classifier model (full training set) ===



Single conjunctive rule learner:
--------------------------------
(SentenceLength <= 18.5) and (VBN <= 13.5) and (NN > 19) and (SYM <= 0.5) and (DT <= 39.5) and (RB <= 26.5) and (NNS <= 30.5) => Result = 1.978392

Time taken to build model: 0.66 seconds

=== Evaluation on test set ===
=== Summary ===

Correlation coefficient                  0.3587
Mean absolute error                      0.1229
Root mean squared error                  0.2441
Relative absolute error                 91.8238 %
Root relative squared error             93.3671 %
Total Number of Instances             1680     


#Decision Table
=== Classifier model (full training set) ===

Decision Table:

Number of training instances: 3920
Number of Rules : 209
Non matches covered by Majority class.
  Best first.
  Start set: no attributes
  Search direction: forward
  Stale search after 5 node expansions
  Total number of subsets evaluated: 344
  Merit of best subset found:    0.238
Evaluation (for feature selection): CV (leave one out) 
Feature set: 12,16,37,39,43

Time taken to build model: 5.11 seconds

=== Evaluation on test set ===
=== Summary ===

Correlation coefficient                  0.4553
Mean absolute error                      0.1098
Root mean squared error                  0.2331
Relative absolute error                 82.0786 %
Root relative squared error             89.1478 %
Total Number of Instances             1680  





