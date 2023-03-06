import math
from collections import Counter
from math import log2

# Pad each sentence with start and end symbols and lowercase all words
def preprocess(data):
    preprocessed = []
    for sentence in data:
        sentence = "<s> " + sentence.strip().lower() + " </s>"
        preprocessed.append(sentence)
    return preprocessed

# Replace words occurring once in training data with <unk>
def replace_singletons(data):
    word_freq = Counter()
    for sentence in data:
        for word in sentence.split():
            word_freq[word] += 1
    for i, sentence in enumerate(data):
        new_sentence = []
        for word in sentence.split():
            if word_freq[word] == 1:
                new_sentence.append("<unk>")
            else:
                new_sentence.append(word)
        data[i] = " ".join(new_sentence)
    return data

# Train unigram model
def train_unigram(data):
    unigrams = Counter()
    total_words = 0
    for sentence in data:
        for word in sentence.split():
            unigrams[word] += 1
            total_words += 1
    for word in unigrams:
        unigrams[word] /= total_words
        unigrams[word] = log2(unigrams[word])
    return unigrams

# Train bigram model
def train_bigram(data):
    bigrams = {}
    unigrams = Counter()
    for sentence in data:
        words = sentence.split()
        for i in range(1, len(words)):
            bigram = (words[i-1], words[i])
            if bigram not in bigrams:
                bigrams[bigram] = 1
            else:
                bigrams[bigram] += 1
            unigrams[words[i-1]] += 1
    for bigram in bigrams:
        bigrams[bigram] /= unigrams[bigram[0]]
        bigrams[bigram] = log2(bigrams[bigram])
    return bigrams

# Train bigram model with add-one smoothing
def train_add_one(data):
    bigrams = {}
    unigrams = Counter()
    vocab_size = len(set(" ".join(data).split()))
    for sentence in data:
        words = sentence.split()
        for i in range(1, len(words)):
            bigram = (words[i-1], words[i])
            if bigram not in bigrams:
                bigrams[bigram] = 1
            else:
                bigrams[bigram] += 1
            unigrams[words[i-1]] += 1
    for bigram in bigrams:
        bigrams[bigram] = log2((bigrams[bigram]+1)/(unigrams[bigram[0]]+vocab_size))
    return bigrams

# Evaluate language models on test corpus
def evaluate(test_data, model):
    total_words = 0
    unk_words = 0
    unk_types = set()
    for sentence in test_data:
        for word in sentence.split():
            total_words += 1
            if word not in model:
                unk_words += 1
                unk_types.add(word)
    percent_tokens = (unk_words / total_words) * 100
    percent_types = (len(unk_types) / (len(set(" ".join(test_data).split()))-1)) * 100
    return (percent_tokens, percent_types)

# Calculate percentage of bigrams not in training data
def bigram_oov(test_data, train_data):
    train_bigrams = set()
    for sentence in train_data:
        words = sentence
# Calculate percentage of bigrams not in training data
def bigram_oov(test_data, train_data):
    train_bigrams = set()
    for sentence in train_data:
        words = sentence.split()
        for i in range(1, len(words)):
            train_bigrams.add((words[i-1], words[i]))
    test_bigrams = set()
    oov_bigrams = set()
    for sentence in test_data:
        words = sentence.split()
        for i in range(1, len(words)):
            test_bigram = (words[i-1], words[i])
            test_bigrams.add(test_bigram)
            if test_bigram not in train_bigrams:
                oov_bigrams.add(test_bigram)
    percent_types = (len(oov_bigrams) / len(test_bigrams)) * 100
    percent_tokens = (sum([test_bigrams.count(bigram) for bigram in oov_bigrams]) / sum([test_bigrams.count(bigram) for bigram in test_bigrams])) * 100
    return (percent_tokens, percent_types)




#Load train and test corpus
with open("C:/Users/jjram/PycharmProjects/Gangjun_Jiang_HW1/Atrain-Spring2023.txt", "r", encoding="utf-8") as f:
    train_data = f.readlines()
with open("C:/Users/jjram/PycharmProjects/Gangjun_Jiang_HW1/Atext.txt", "r", encoding="utf-8") as f:
    test_data = f.readlines()

#Preprocess train and test corpus
train_data = preprocess(train_data)
test_data = preprocess(test_data)
test_data_unk = replace_singletons(test_data)


#Train language models
unigram_model = train_unigram(train_data)
bigram_model = train_bigram(train_data)
add_one_model = train_add_one(train_data)


#Calculate number of word types in training corpus
unique_words = set(" ".join(train_data).split())
num_word_types = len(unique_words) + 1 # add 1 for <unk>
print("1. Number of word types in training corpus:", num_word_types)

#Calculate number of word tokens in training corpus (excluding start and end symbols)
num_word_tokens = sum([len(sentence.split())-2 for sentence in train_data])
print("2. Number of word tokens in training corpus:", num_word_tokens)

#Calculate number of word types and tokens in test corpus not in training corpus
test_oov_tokens, test_oov_types = evaluate(test_data, unigram_model)
print("3. Percentage of word types in test corpus not in training:", round(test_oov_types, 2), "%")
print("4. Percentage of word tokens in test corpus not in training:", round(test_oov_tokens, 2), "%")

#Evaluate sentence using language models
sentence = "<s> i look forward to hearing your reply . </s>"
sentence_unk = " ".join([word if word in unigram_model else "<unk>" for word in sentence.split()])

#Calculate Unigram log probability
epsilon = 1e-10
unigram_log_prob = sum([math.log2((unigram_model.get(word, 0) + epsilon)/(sum(unigram_model.values())
                                                                          + epsilon*len(unigram_model)))
for word in sentence_unk.split()])
print("5. Unigram log probability:", unigram_log_prob)

#Calculate Bigram log probability
epsilon = 1e-5
bigram_log_prob = 0
for i in range(1, len(sentence_unk.split())):
    bigram_prob = bigram_model.get((sentence_unk.split()[i-1], sentence_unk.split()[i]), 0)
    if bigram_prob > 0:
        bigram_log_prob += math.log2(bigram_prob + epsilon)
    else:
        bigram_log_prob += math.log2(epsilon)
print("6. Bigram log probability:", bigram_log_prob)

#Calculate Add-One log probability
epsilon = 1e-10
add_one_log_prob = 0.0
for i in range(1, len(sentence_unk.split())):
    if (sentence_unk.split()[i-1], sentence_unk.split()[i]) in add_one_model:
        prob = add_one_model[(sentence_unk.split()[i-1],
                              sentence_unk.split()[i])] + epsilon
    else:
        prob = 1.0 / (num_word_tokens + num_word_types)
        add_one_log_prob += math.log2(max(prob, epsilon))
print("7. Add-One log probability:", add_one_log_prob)


#Calculate perplexity of sentence test corpus under using each model
# Perplexity of sentence
num_tokens = len(sentence_unk.split())
unigram_pp = 2 ** (-unigram_log_prob / (num_tokens + epsilon))
bigram_pp = 2 ** (-bigram_log_prob / (num_tokens + epsilon))
add_one_pp = 2 ** (-add_one_log_prob / (num_tokens + epsilon))


print("Unigram of test corpus perplexity:", unigram_pp)
print("Bigram of test corpus perplexity:", bigram_pp)
print("Add-One of test corpus perplexity:", add_one_pp)

