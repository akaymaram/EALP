import fitz

doc = fitz.open("sample.pdf")
String_doc = ""
for page in doc:
	text = page.get_text('text')
	String_doc += text
count = 0
for sample in String_doc.split('.'):
	count+=1
	sample = sample.replace('\n', '')
	print(str(count)+" " + sample)

title = "African American Women's Economic Activism in Milwaukee"
list_of_words = title.split()
concepts = []
list_of_concept = ["African American Women's Economic Activism","Milwaukee"]
concepts.extend(list_of_concept)
for x in concepts:
	text = x
	for page in doc:
		text_instances = page.searchFor(text)
		for inst in text_instances:
			highlight = page.addHighlightAnnot(inst)


Adversative = ["however", "nevertheless", "in fact","actually", "instead", "contrary"]
Sequential = ["then", "next", "last", "finally", "up to now", "to sum up"]
Causal = ["therefore", "consequently", "then", "otherwise"]
Additive = ["in addition","moreover", "that is", "for instance"
"likewise","similarly"]

my_terms = ["this book", "conclu", "argue"
"thus", "therefore", "due to", "But not as boring as watching paint dry"]

for x in my_terms:
	text = x
	for page in doc:
		text_instances = page.searchFor(text)
		for inst in text_instances:
			highlight = page.addUnderlineAnnot(inst)




doc.save("output.pdf", garbage=4, deflate=True, clean=True)