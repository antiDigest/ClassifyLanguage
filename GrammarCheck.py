import win32com.client, os


def GrammarCheck(filename):
	wdDoNotSaveChanges = 0
	path = os.path.abspath(filename)

	app = win32com.client.gencache.EnsureDispatch('Word.Application')
	doc = app.Documents.Open(path)
	errors_g = doc.GrammaticalErrors.Count
	errors_s = doc.SpellingErrors.Count
	# print "Grammar: %d" % (errors,)

	app.Quit(wdDoNotSaveChanges)

	return errors_g, errors_s

def SpellCheck(filename):
	wdDoNotSaveChanges = 0
	path = os.path.abspath(filename)

	app = win32com.client.gencache.EnsureDispatch('Word.Application')
	doc = app.Documents.Open(path)
	errors = doc.SpellingErrors.Count
	# print "Spelling: %d" % (errors,)

	app.Quit(wdDoNotSaveChanges)

	return errors

def parallelism(filename):