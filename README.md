# Natural-Language-Processing
## Name: Gangjun Jiang
## Professor: Alla Rozovskaya
## date: 3/8/2023
## HW1
## 1.1 PRE-PROCESSING
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

 1.(5 points) How many word types (unique words) are there in the training corpus? Please include the end-of-sentence padding symbol </s> and the unknown token <unk>. Do not include the start of sentence padding symbol <s>.
Answer: There are 83046 unique words in the training corpus, including </s> and <unk>.

## 2. (5 points) How many word tokens are there in the training corpus? Do not include the start of sentence padding symbol <s>.
Answer: There are 2368210 word tokens in the training corpus, excluding <s>.

## 3.(10 points) What percentage of word tokens and word types in the test corpus did not occur in training (before you mapped the unknown words to <unk> in training and test data)? Please include the padding symbol </s> in your calculations. Do not include the start of sentence padding symbol <s>.

Answer: The percentage of word tokens and word types in the test corpus that did not occur in the training corpus is 33.74% and 0.71%, respectively, including </s>.

## 4.(15 points) Now replace singletons in the training data with <unk> symbol and map words (in the test corpus) not observed in training to <unk>. What percentage of bigrams (bigram types and bigram tokens) in the test corpus did not occur in training (treat <unk> as a regular token that has been observed)? Please include the padding symbol </s> in your calculations. Do not include the start of sentence padding symbol <s>.
 Answer: The percentage of bigram types and tokens in the test corpus that did not occur in the training corpus is 42.935%, including </s>.
## 5.(15 points) Compute the log probability of the following sentence under the three models (ignore capitalization and pad each sentence as described above). Please list all of the parameters required to compute the probabilities and show the complete calculation. Which of the parameters have zero values under each model? Use log base 2 in your calculations. Map words not observed in the training corpus to the <unk> token.
• I look forward to hearing your reply.
Answer:
Parameters:
Unigram: P(w) = count(w) / N
Bigram: P(wi | wi-1) = count(wi-1, wi) / count(wi-1)
Bigram with Add-One smoothing: P(wi | wi-1) = (count(wi-1, wi) + 1) / (count(wi-1) + V)

Unigram log probability: -175.64740857118326
Bigram log probability: -149.4867642699313 (Undefined)
Bigram Add-One log probability: -63.67526919319887

In the bigram model, the log probability is undefined


 6.(20 points) Compute the perplexity of the sentence above under each of the models.

Answer:
Perplexity is a measure of how well a language model predicts a sample of text. A lower perplexity indicates a better fit of the language model to the data.

The perplexity of the given sentence under each model is:

Unigram: 193871.45246448333
Bigram: Undefined
Bigram with Add-One smoothing: 82.56891939636107

For the bigram model, since the log probability is undefined, we cannot calculate perplexity. The perplexity of the unigram model is much higher than that of the bigram with Add-One smoothing, which indicates that the latter model is a better fit for the given sentence.


 7.(20 points) Compute the perplexity of the entire test corpus under each of the models. Discuss the differences in the results you obtained.

Answer:
The perplexity of the entire test corpus under each model is:

Unigram: 193871.45246448333
Bigram: Undefined
Bigram with Add-One smoothing: 31622.77659840716

The bigram log probability is undefined because one of the bigram tokens in the sentence ("hearing", "your") does not occur in the training corpus, so its count is zero. As a result, the probability of this bigram is zero, and the log of zero is undefined. Since the bigram model relies on the count of bigram tokens in the training corpus, if any bigram token in the test corpus is not observed in the training corpus, its probability will be zero, and the log probability will be undefined. This is a limitation of the bigram model, which does not handle unseen bigrams effectively.
The perplexity of the unigram model is much higher than that of the bigram with Add-One smoothing, which indicates that the latter model is a better fit for the test corpus. The bigram model remains undefined because it has a tuple with log probability of zero. Although the Add-one smoothing solved the zero probability tuples, it is still worse than the Bigram Model.

One possible explanation for the better performance of the bigram model with Add-One smoothing is that it accounts for some of the sparsity in the data and handles unseen bigrams more effectively. However, this comes at the cost of introducing some bias in the model towards overestimating the probability of some bigrams.

Overall, the choice of language model depends on the specific task and the data at hand. In this case, the bigram with Add-One smoothing seems to be a better choice for the given test corpus, while the unigram model is not a good fit at all.


