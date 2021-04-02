# dag.py 1.0.3

import numpy as np
import sys
import random


import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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

total = [i for i in range(len(list_of_sentences))]



def summary_matrix(summary):
	row_numbers = [-1]
	for x in summary:
		row_numbers.append(x)
	matrix = np.array(row_numbers)

	for i in summary:
		row = [i]
		sentence = list_of_sentences[i]
		set_of_words = {word for word in sentence.split()}
		sentence_size = len(set_of_words)
		for j in summary:
			if j < i:
				row.append(0)
				continue
			elif j == i:
				row.append(1)
				continue

			second_sentence = list_of_sentences[j]
			second_set_of_words = {word for word in second_sentence.split()}
			second_sentence_size = len(second_set_of_words)

			count = len(set_of_words.intersection(second_set_of_words))

			edge_weight = round(count/(sentence_size+second_sentence_size),3)


			row.append(edge_weight)

		matrix = np.vstack([matrix,row])
	return matrix





max_matrix = summary_matrix(total)

print(max_matrix)
print(max_matrix[2, 3])


print(summary_matrix([0,3,5,6]))
sys.exit()

 
def function(summary):
	row_numbers = [-1]
	for x in summary:
		row_numbers.append(x)
	matrix = np.array(row_numbers)


	total = 0
	start_sentence = 0
	end_sentence = 1
	while  end_sentence < len(summary):
		total+= matrix[start_sentence+1, end_sentence+1]
		start_sentence+=1
		end_sentence+=1

	return total

 
# tournament selection
def selection(population, scores, k=3):
	# first random selection
	selection_ix = randint(len(population))
	for ix in randint(0, len(population), k-1):
		# check if better (e.g. perform a tournament)
		if scores[ix] > scores[selection_ix]:
			selection_ix = ix
	return population[selection_ix]
 
 
# mutation operator
def mutation(summary, r_mut, doc_length):
	num_sentences_to_change = max(int(r_mut*len(summary)),1)

	lowest_edge_weight = 1
	lowest_edge_weight_vertices = (0,0)
	start_sentence = 0
	end_sentence = 1
	while  end_sentence < len(summary):
		weight = matrix[start_sentence+1, end_sentence+1]
		if weight < lowest_edge_weight:
			lowest_edge_weight = weight
			lowest_edge_weight_vertices = (start_sentence,end_sentence)
		start_sentence+=1
		end_sentence+=1

	summary.remove(lowest_edge_weight_vertices[-1])
	summary.add(randint(0, doc_length))



	for i in range(len(summary)):
		# check for a mutation
		if rand() < r_mut:
			# flip the bit
			summary[i] = 1 - summary[i]
 

def genetic_algorithm(function, doc_length, summary_length, number_of_iterations, population_size, r_cross, r_mut):

	
	population = []
	for _ in range(population_size):
		summary = set()
		i = 0
		while i < summary_length:
			sample_index = randint(0, doc_length)
			if sample_index not in summary:
				summary.add(sample_index)
			else:
				i-=1
			i+=1
		population.append(sorted(summary))

	print(population)

	best_summary, best_score = 0, 0
	for gen in range(number_of_iterations):

		scores = [function(p) for p in population]
		for i in range(population_size):
			if scores[i] > best_score:
				best_summary, best_score = population[i], scores[i]
				print(">%d, new best f(%s) = %f" % (gen,  best_summary, best_score))

		# select parents
		selected = [selection(population, scores) for _ in range(population_size)]
		# create the next generation
		children = list()
		for i in range(0, population_size, 2):
			# get selected parents in pairs
			p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
			# for c in crossover(p1, p2, r_cross):
			# 	# mutation
			# 	mutation(c, r_mut)
			# 	# store for next generation
			# 	children.append(c)


			
		population = children
	return [best_summary, best_score]
 


doc_length = len(matrix)-1

summary_length = 5

num_iterations = 100

population_size = 10

r_cross = 0.9

mutation_coefficient = .1


best, score = genetic_algorithm(function, doc_length, summary_length, num_iterations, population_size, r_cross, mutation_coefficient)
print('Done!')
print('f(%s) = %f' % (best, score))

