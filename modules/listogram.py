import random

def sample_word():

	word_array = "one fish two fish green fish blue fish".split()

	# create a dictionary which will store the word as the key and the frequency as the value
	histogramm = {}
	for word in word_array:
		if word in histogramm.keys():
			histogramm[word] += 1
		else:
			histogramm[word] = 1

	# BETTER implementation cr.Jackson
	count = 0
	random_number = random.random()
	for key, value in histogramm.items():
		count += (value / len(word_array))
		if count >= random_number:
			return key



def test_sample_word():

	histogram = {}

	for i in range(0, 10000):
		sample = sample_word()
		# append the word count found by one or add to the word count found
		if sample in histogram:
			histogram[sample] += 1
		else:
			histogram[sample] = 1

	return histogram

	

if __name__ == "__main__":
	print(sample_word())
	print(test_sample_word())
