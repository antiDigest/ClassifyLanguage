import win32com.client, os


def GrammarCheck(filename):
	wdDoNotSaveChanges = 0
	path = os.path.abspath(filename)

	app = win32com.client.gencache.EnsureDispatch('Word.Application')
	doc = app.Documents.Open(path)
	errors = doc.GrammaticalErrors.Count
	print "Grammar: %d" % (errors,)

	app.Quit(wdDoNotSaveChanges)

	return errors

def SpellCheck(filename):
	wdDoNotSaveChanges = 0
	path = os.path.abspath(filename)

	app = win32com.client.gencache.EnsureDispatch('Word.Application')
	doc = app.Documents.Open(path)
	errors = doc.SpellingErrors.Count
	print "Spelling: %d" % (errors,)

	app.Quit(wdDoNotSaveChanges)

	return errors