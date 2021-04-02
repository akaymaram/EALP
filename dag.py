# dag.py 1.0.2

import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import numpy as np
import sys


import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

graph = nx.DiGraph()

myfile = open("input2.txt", "r")
content = myfile.read()
myfile.close()


## removing stop words and Lemmatization
stop_words = set(stopwords.words('english'));
word_tokens = word_tokenize(content)
lemmatizer = WordNetLemmatizer()
filtered_sentence = []
for w in word_tokens:
	if w.lower() not in stop_words:
		filtered_sentence.append(lemmatizer.lemmatize(w))
final_sentence= ' '.join(filtered_sentence)



list_of_sentences = [sentence for sentence in final_sentence.split(".") if len(sentence) > 0]

list_count =[]

for i in range(0, len(list_of_sentences)):
	set_of_words_in_the_sentence = {word for word in list_of_sentences[i].split()}

	for j in range(i+1, len(list_of_sentences)):
		count = 0
		for word_in_next_sentence in list_of_sentences[j].split():
			if word_in_next_sentence in set_of_words_in_the_sentence and word_in_next_sentence != ",":
				count+=1
		list_count.append(count)
		j = j + 1
	i+= 1


row_numbers = [-1]
for x in range(len(list_of_sentences)):
	row_numbers.append(x)

matrix = np.array(row_numbers)

max_count = max(list_count)
k=0
for i in range(0, len(list_of_sentences)):
	row_list = [i]

	for j in range(len(list_of_sentences)):
		if j == i:
			row_list.append(1)
			continue
		if j < i+1:
			row_list.append(0)
			continue

		count=list_count[k]
		row_list.append(round(count/max_count,3))
		graph.add_edges_from([(i, j)], weight=count/max_count)
		k=k+1
		j = j + 1
	matrix = np.vstack([matrix,row_list])
	i += 1

print(matrix)
print(matrix[2, 3])

pos = nx.spring_layout(graph, seed=7)

# the commented code below will eventually be removed
# plt.tight_layout()
# nx.draw_networkx_nodes(graph, pos, node_size=700)
# nx.draw_networkx_edges(graph, pos, width=6)
# nx.draw_networkx_edges(graph,pos,edge_color='b',alpha = 0.6)
# nx.draw_networkx_edge_labels(graph,pos,edge_labels = nx.get_edge_attributes(graph,'weight'))
# nx.draw_networkx(graph, pos,arrows=False)
# plt.show()
# plt.savefig("g.png", format="PNG")
# plt.clf()