import textblob
text = "This is a text document"
content = textblob.TextBlob(text)
analysis = content.sentiment
