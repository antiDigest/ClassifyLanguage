import win32com.client, os


def GrammarCheck():
	wdDoNotSaveChanges = 0
	path = os.path.abspath('snippet.txt')

	snippet = 'How correct you are ? when no body liek yous !'
	snippet += 'This is a correct sentence.'
	file = open(path, 'w')
	file.write(snippet)
	file.close()

	app = win32com.client.gencache.EnsureDispatch('Word.Application')
	doc = app.Documents.Open(path)
	print "Grammar: %d" % (doc.GrammaticalErrors.Count,)
	print "Spelling: %d" % (doc.SpellingErrors.Count,)

	app.Quit(wdDoNotSaveChanges)


if __name__ == '__main__':
	GrammarCheck()