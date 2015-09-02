
with open('EnglishAuxiliaryVerbs.txt','r') as f:
	lines = f.read().split('\n')
	auxverbs = [line for line in lines if not "//" in line] 

with open('EnglishConjunctions.txt','r') as f:
	lines = f.read().split('\n')
	conjunctions = [line for line in lines if not "//" in line] 

with open('EnglishDeterminers.txt','r') as f:
	lines = f.read().split('\n')
	determiners = [line for line in lines if not "//" in line] 

with open('EnglishPrepositions.txt','r') as f:
	lines = f.read().split('\n')
	prepositions = [line for line in lines if not "//" in line] 

with open('EnglishPronouns.txt','r') as f:
	lines = f.read().split('\n')
	pronouns = [line for line in lines if not "//" in line] 

with open('EnglishQuantifiers.txt','r') as f:
	lines = f.read().split('\n')
	quantifiers = [line for line in lines if not "//" in line] 

allwords = auxverbs + conjunctions + determiners +prepositions+pronouns+quantifiers
print allwords

def WordCount(filename):
	with open(filename,'r') as f:
		return len(f.read().split(' '))

def FunctionWordCount(filename):
	with open(filename,'r') as f:
		filewords = f.read().split(' ')
	auxcount = 0
	concount = 0
	detcount = 0
	prepcount = 0
	procount = 0
	quantcount = 0
	for i in filewords:
		if i in auxverbs:
			auxcount += 1
		elif i in conjunctions:
			concount += 1
		elif i in determiners:
			detcount += 1
		elif i in prepositions:
			prepcount += 1
		elif i in pronouns:
			procount += 1
		elif i in quantifiers:
			quantcount += 1

		count = auxcount + concount + detcount + prepcount + procount + quantcount

	return count


 # For reference purposes, a succinct description of each class of function words follows.

 #    Auxiliary Verbs are verbs whose function is to characterize the main verbs they accompany with shades of meaning pertaining to tense and/or modality. Regarding tense, the core meaning of the verb can be modified to express perfect, progressive, or passive voices. Regarding modality, the main verb is altered to denote judgement or opinion in terms of ability, advice, expectation, intention/willingness, likelihood, necessity, permission/prohibition, or degrees of politeness.

 #    Auxiliary verbs are necessary to form questions and negatives in English. If auxiliary verbs are used only to serve these functions, they are referred to as dummy auxiliaries. Additionally, the auxiliaries 'do', 'does', and 'did' can be inserted preceding the main verb for emphasis. Modal verbs are distinguished from other auxiliary verbs by their inability to function as main verbs and their lack of complete conjugations (infinitive for example).

 #    Conjunctions are uninflected function words that serve to conjoin words, clauses, phrases, or sentences. There are three basic forms: single word (however), compound (as long as), and correlative (so ... that). In terms of function, conjunctions can be grouped into additive (so, thus), adversative (but, instead), causative (so, because), and temporal (after, then).

 #    Conjunctions are not structural elements in a clause. Rather, they are external elements that establish grammatical relations (coordination, correlation, subordination) between clauses. Certain adverbial and prepositional phrases can also act as conjunctions (subsequently, in addition to that).

 #    Determiners are inflected function words employed as noun modifiers and that serve to alter the referents of noun phrases in terms of amount, location, possession, and general versus specific. In terms of form, determiners are simple (two, their, the) or compound (a number of, one half, a little). Also, possessive and demonstrative adjectives are considered determiners.

 #    The determiner class is often divided into articles (a, an, the), determiners (both, neither, whichever), and quantifiers (much, various, little).

 #    Prepositions are uninflected function words that combine with nouns, pronouns, or noun phrases to form prepositional phrases that can have, in turn, adverbial or adjectival relationships with other words. Prepositions can be simple (as, of) or compound (next to, in view of) forms. In terms of function, at least the following types of preposition can be distinguished: time (until, circa), location (along, amid), logical (since, given), possession (including, pertaining to), and movement (toward, to).

 #    Prepositions can also occur in post position with: nouns (interest in, need for), adjectives (familiar with, sure of), participles (married to, made of), and verbs (give up, look forward). In this situation, the composite can be thought of as a unit.

 #    Pronouns are inflected function words employed in place of nouns or noun phrases. In terms of form, pronouns are simple (nothing, herself) and compound (each other, one another). Also, some pronoun composites are used in relative clauses (all of whom, several of which).

 #    Pronouns are classified into the following classes: subject personal (I, he, we), object personal (me, him, us), possessive (mine, his, ours), reflexive (myself, himself, ourselves), demonstrative (this, these, such), relative (who, all, that), indefinite (each, anybody, none), reciprocal (each other, one another), and interrogative (how, who, why). Additionally, reflexives also operate as so-called intensive pronouns when they are employed to emphasize an antecedent noun or pronoun (as in, "The boss himself prepared the coffee" or "I myself could not believe it").
