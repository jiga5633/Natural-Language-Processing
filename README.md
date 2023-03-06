
1.1 PRE-PROCESSING
Prior to training, the following pre-processing steps were completed:

Each sentence in the training and test corpora was padded with start and end symbols (<s> and </s>, respectively).
All words in the training and test corpora were converted to lowercase. Note that the data had already been tokenized (i.e. punctuation had been split off words).
All words occurring in the training data once were replaced with the token <unk>. Every word in the test data not seen in training was treated as <unk>.
1.2 TRAINING THE MODELS
The following language models were trained using train.txt:

Unigram maximum likelihood model.
Bigram maximum likelihood model.
Bigram model with Add-One smoothing.
1.3 QUESTIONS

The following questions were answered:

(5 points) How many word types (unique words) are there in the training corpus? Please include the end-of-sentence padding symbol </s> and the unknown token <unk>. Do not include the start of sentence padding symbol <s>.
Answer: There are 83046 unique words in the training corpus, including </s> and <unk>.

(5 points) How many word tokens are there in the training corpus? Do not include the start of sentence padding symbol <s>.
Answer: There are 2368210 word tokens in the training corpus, excluding <s>.

(10 points) What percentage of word tokens and word types in the test corpus did not occur in training (before you mapped the unknown words to <unk> in training and test data)? Please include the padding symbol </s> in your calculations. Do not include the start of sentence padding symbol <s>.
Answer: The percentage of word tokens and word types in the test corpus that did not occur in the training corpus is 33.74% and 0.71%, respectively, including </s>.

(15 points) Now replace singletons in the training data with <unk> symbol and map words (in the test corpus) not observed in training to <unk>. What percentage of bigrams (bigram types and bigram tokens) in the test corpus did not occur in training (treat <unk> as a regular token that has been observed)? Please include the padding symbol </s> in your calculations. Do not include the start of sentence padding symbol <s>.
Answer: The percentage of bigram types and tokens in the test corpus that did not occur in the training corpus is 42.935%, including </s>.

(15 points) Compute the log probability of the following sentence under the three models (ignore capitalization and pad each sentence as described above). Please list all of the parameters required to compute the probabilities and show the complete calculation. Which of the parameters have zero values under each model? Use log base 2 in your calculations. Map words not observed in the training corpus to the <unk> token.
• I look forward to hearing your reply.

Answer:
Parameters:

Unigram: P(w) = count(w) / N
Bigram: P(wi | wi-1) = count(wi-1, wi) / count(wi-1)
Bigram with Add-One smoothing: P(wi | wi-1) = (count(wi-1, wi) + 1) / (count(wi-1) + V)
Unigram log probability: -175.64740857118326
Bigram log probability: -149.4867642699313 (Undefined)
Bigram Add-One log probability: -63.67526919319887
