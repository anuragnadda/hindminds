from django.test import TestCase

# Create your tests here.
from spam_data import training_spam_docs, training_doc_tokens, training_labels
from sklearn.naive_bayes import MultinomialNB
from preprocessing import preprocess_text

# Add your email text to test_text between the triple quotes:
test_text = """
UNITED STATES DISTRICT COURT FOR THE NORTHERN DISTRICT OF CALIFORNIA
If you have previously had either the Google “Web & App Activity” control or the “Supplemental Web & App Activity” sub-setting turned off or “paused,” you could be included in an ongoing class action lawsuit.

For more information about the lawsuit, read below or visit www.GoogleWebAppActivityLawsuit.com.

Para una notificacion en Español, visitar www.GoogleWebAppActivityLawsuit.com.

A federal Court authorized this Notice. This is not a solicitation from a lawyer.
"""
test_tokens = preprocess_text(test_text)

def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary

def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector

bow_sms_dictionary = create_features_dictionary(training_doc_tokens)
training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]
test_vectors = [tokens_to_bow_vector(test_tokens, bow_sms_dictionary)]

spam_classifier = MultinomialNB()
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.predict(test_vectors)

print("Looks like a normal email!" if predictions[0] == 0 else "You've got spam!")









?????

from preprocessing import preprocess_text
# Define text_to_bow() below:

def text_to_bow(some_text):
  bow_dictionary = {}
  tokens = preprocess_text(some_text)
  for token in tokens:
    if token in bow_dictionary:
      bow_dictionary[token] += 1
    else:
      bow_dictionary[token] = 1

  return bow_dictionary

print(text_to_bow("I love fantastic flying fish. These flying fish are just ok, so maybe I will find another few fantastic fish..."))