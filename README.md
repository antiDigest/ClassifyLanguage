# ClassifyLanguage
Language Classifier

# What ?

Every language has a different grammar pattern, and sometimes people mix the grammars while writing text in English. We would like to use this idea and extend our knowledge in machine learning and natural language processing to figure out if this is doable.

## Data Collected on ICNALE-Written
|Country Code 	|Country 	|Writers/Essays 	|  # of Tokens	|
|:--------------:|:---------:|:-----------------:|:-------------:|
|ENS*   			|USA, UK,CAN, AUS, NZ	|	200/ 400		|	88,792  	|
| HKG** 			|Hong Kong	| 	100/ 200  		|	46,111		|
| PAK** 			|Pakistan	|	 	200/ 400  	|	93,100		|
| PHL** 			|Philippines|  	200/ 400  		|	96,586		|
| SIN** 			|Singapore	|  	200/ 400  		|	96,733		|
| CHN***			|China 	 	|  	400/ 800  		|	194,613 	|
| IDN***			|Indonesia	| 	200/ 400   		|	92,316 		|
| JPN***			|Japan 	 	|		400/ 800  	|	176,537		|	 
| KOR***			|Korea 		|	300/ 600		|  	130,626 	|
| THA***			|Thailand 	|  	400/ 800  		|	176,936 	|
| TWN***			|Taiwan  	|	200/ 400  		|	89,736		| 
|Total 			|	--- 	|	2,800/ 5,600 	|	1,282,086*	|

*Inner Circle

**Outer Circle

***Expanding Circle


## What each file name means:

|S/W 	|Country| 	Topic/ Trial| 	Serial| 	CEFR|
|:--------------:|:---------:|:-----------------:|:-------------:|:-------------:|
|||||For NNS|
|||PTJ: part-time job||A2_0: A2|
|S: Speech|CHN, ENS, HKG, IDN, JPN,TWN 	|SMK: non-smoking||B1_1: B1 Lower|
|W: Writing|KOR, PAK, PHL, SIN, THA,|0 Essay|001-999|B1_2: B1 Upper|
|||1 Speech (Trial 1)||B2_0: B2 +|
|||2 Speech (Trial 2)||For NS|
|||||XX_1 Students|
|||||XX_2 Teachers|
|||||XX_3 Others|


## What terms in XLSX file mean:

### About essays or speeches
|Term|Meaning|
|:----:|:-------:|
Code| File code
PTJ (wds)| The number of words in one essay or speech
SMK (wds)|The number of words in one essay or speech

### About participants' background
|Term|Meaning|
|:----:|:-------:|
Country| Participant's country or area
Sex | Participant's sex
Age| Participant's age
Grade| Participant's school grade (1, 2, 3, 4|)
Major (Occupation)| In case of students, their major at colleges; in case of employed people, their job.
Academic Genres| Only for students: Humanities, Social Sciences, Science and Technology, and Life Science

### About participants' proficiency
|Term|Meaning|
|:----:|:-------:|
Proficiency Test| Test name such as TOEIC or TOEFL
Score| Score in the test above
VST| Score in the vocabulary size test (full mark is 50) This test measures participants' L2 lexical knowledge with a ceiling of 5,000 words.
CEFR| CEFR levels: A2, B1_1, B1_2, B2+. Estimated from participants' scores in the proficiency test or in the vocabulary size test

### About participants' motivation
|Term|Meaning|
|:----:|:-------:|
INTM| Integrative Motivation Score
INSM| Instrumental Motivation Score
INTM+INSM| Strength of Motivation
INTM-INSM| Integrative Motivation Orientation Score

### About participants' L2 learning experiences
|Term|Meaning|
|:----:|:-------:|
Primary| How much a participant studies English in their primary school days (1 to 6 points)
Secondary|How much a participant studies English in their secondary school days (1 to 6 points)
College|How much a participant studies English in their college days (1 to 6 points)
Inschool| How much a participant studies English in class (1 to 6 points)
Outschool| How much a participant studies English outside class, namely, at home, in the community etc (1 to 6 points)
Listening| How much a participant studies listening (1 to 6 points)
Reading| How much a participant studies reading (1 to 6 points)
Speaking| How much a participant studies speaking (1 to 6 points)
Writing| How much a participant studies writing (1 to 6 points)
NS| How much a participant has been taught by English native participant (1 to 6 points)
Pronunciation|How much a participant has been taught by English native participant (1 to 6 points)
Presentation|How much a participant has been taught presentation (1 to 6 points)
Essay Writing|How much a participant has been taught essay writing (1 to 6 points)


### Done :

1.	~~Average Sentence Length~~

2.	~~Grammar Check~~

3.	~~Spelling Check~~

4.	~~Word Count~~

5.	~~Function Words Count~~

6.	~~POS Bigrams and Trigrams~~

### TODO:

1.    Select more and different features. Use ngrams, tfidf etc

2.    Apply dimensionality reduction

3.    Check again on classifiers

4.    We first convert each of the essays in our training data to a list of parts of speech using Stanford’s parts of speech tagger [5]. For example, the sentence ”This is a paper” would be converted to (determiner, third person verb, determiner, singular noun). We then take consecutive 2-sequences of parts of speech, and count the frequency of each 2-sequence in all of the training essays for a language of origin. Thus, each language has its own model of parts of speech frequencies. Then, for each essay in our test data, we find the likelihood of the sequence of parts of speech from that essay appearing in each language based on our models. The prediction is the language that results in the highest likelihood.

5.   We also need to find the sentence structures (subject-verb-object kind of structures !). Search how to do that !

# Requirements:

1.	Install nltk, textblob, sklearn, pandas

## Outputs

*   First output : Logisitic Regression gives 44.9% f1 measure ! LOSER ! After removing just some features (--removed ones), f1 measure comes down to 36.36% !

*   Removed commented out features : 0.48087431694

*   Information Gain with best splits ready ! Either not working, or I did remove good features. Well, does work !

*   Principal component analysis studying.
