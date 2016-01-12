# ClassifyLanguage
Language Classifier

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


##What each file name means:

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


##What terms in XLSX file mean:

###About essays or speeches
|Term|Meaning|
|:----:|:-------:|
Code| File code
PTJ (wds)| The number of words in one essay or speech
SMK (wds)|The number of words in one essay or speech

###About participants' background
|Term|Meaning|
|:----:|:-------:|
Country| Participant's country or area
Sex | Participant's sex
Age| Participant's age
Grade| Participant's school grade (1, 2, 3, 4|)
Major (Occupation)| In case of students, their major at colleges; in case of employed people, their job.
Academic Genres| Only for students: Humanities, Social Sciences, Science and Technology, and Life Science

###About participants' proficiency
|Term|Meaning|
|:----:|:-------:|
Proficiency Test| Test name such as TOEIC or TOEFL
Score| Score in the test above
VST| Score in the vocabulary size test (full mark is 50) This test measures participants' L2 lexical knowledge with a ceiling of 5,000 words.
CEFR| CEFR levels: A2, B1_1, B1_2, B2+. Estimated from participants' scores in the proficiency test or in the vocabulary size test

###About participants' motivation
|Term|Meaning|
|:----:|:-------:|
INTM| Integrative Motivation Score
INSM| Instrumental Motivation Score
INTM+INSM| Strength of Motivation
INTM-INSM| Integrative Motivation Orientation Score

###About participants' L2 learning experiences
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


###Done :

1.	Average Sentence Length

2.	Grammar Check

3.	Spelling Check

4.	Word Count

5.	Function Words Count

6.	POS Bigrams and Trigrams

###TODO:

1.	Read documents and detect distinct features

2.	<strong>Parallelism</strong> is a similarity of form in words, phrases, or clauses that have similar functions in a sentence or a paragraph. Faulty parallelism is the lack of parallel structure—it creates sentences without a sense of balance. Readers expect parallel word structures especially when there is some underlying parallelism of meaning. Below are some guidelines for when to use parallelism:

	1. Items in Lists: Words, phrases, or clauses in a list or series should all have the same grammatical structure. (Ex: Erin likes surfing the net, working out, and visiting her family.)

	2. Items Joined by Coordinating Conjunctions: Words or phrases joined by coordinating conjunctions should have the same structure. (Ex: Chocolate and peanut butter taste great together.)

	3. Elements joined by correlative conjunctions, such as "either . . . or" and not "only . . .but also," should be parallel. (Ex: We could go fishing or go bicycling.)

	4. Two elements that are compared or contrasted should be expressed in parallel structures. (Ex: I like blue cars as opposed to red cars.) 

3.	Wordiness is taking more words than necessary to make your point. It may take the form of redundant expressions or phrases. To be sure, longer expressions may be appropriate at times as a matter of style or to avoid ambiguity. But some business writers clutter their sentences and paragraphs with words, phrases, and expressions that needlessly distract the reader. Consistent elimination of wordiness results in a stronger, more concise writing style that is easier to read and provides fewer opportunities for misinterpretation. In contrast, a wordy style makes reading laborious and, thus, encourages skimming and leads to inattention. Do you wish the reader to carefully consider your message? If so, reduce wordiness to the extent possible. The examples below provide guidance for avoiding general forms of wordiness.

4.	Passive and active voice usage

5.	Word order: Most English sentences (clauses) conform to the SVO word order. This means that the Subject comes before the Verb, which comes before the Object.

6.	Word choice refers to a writer's selection of words as determined by a number of factors, including meaning (both denotative and connotative), specificity, level of diction, tone, and audience. Another term for word choice is diction. Word choice is an essential ingredient of style.

7.	Punctuation guidelines. Complex and compound sentence punctuation

8.	An important role in English grammar is played by determiners – words or phrases that precede a noun or noun phrase and serve to express its reference in the context. The most common of these are the definite and indefinite articles, the and a(n). Other determiners in English include demonstratives such as this and that, possessives such as my and the boy's, and quantifiers such as all, many and three. In many contexts the presence of some determiner is required in order to form a complete noun phrase. However, in some cases complete noun phrases are formed without any determiner (sometimes referred to as "zero determiner" or "zero article"), as in the sentence Apples are fruit. Determiners can also be used in certain combinations, as in my many friends or all the chairs.

9.	Study Grammar and common grammatical mistakes. Makes machines on those and your job is done.