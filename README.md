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
||W: Writing 	CHN, ENS, HKG, IDN, JPN,TWN 	|SMK: non-smoking||B1_1: B1 Lower|
|S: Speech|KOR, PAK, PHL, SIN, THA,|0 Essay|001-999|B1_2: B1 Upper|
|||1 Speech (Trial 1)||B2_0: B2 +|
|||2 Speech (Trial 2)||For NS|
|||||XX_1 Students|
|||||XX_2 Teachers|
|||||XX_3 Others|


###Done :

1.	Average Sentence Length

2.	Grammar Check

3.	Spelling Check

4.	Word Count

5.	Function Words Count

6.	POS Bigrams and Trigrams

###TODO:

1.	Brill Tag

2.	Sentence Chunk Boundary detector

3.	Read documents and detect distinct features
