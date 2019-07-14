import pandas as pandas
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, GRU, Dense, Softmax, Embedding, GlobalMaxPool1D, GlobalAvgPool1D, Concatenate, Bidirectional, SpatialDropout1D

#Load Training Data from https://storage.googleapis.com/axelbrooke-public/data/sentiment-clf/reviews.tar.gz
df = pd.read_csv("reviews.tar.gz", compression='gzip')

#Load AWS Transcribed text file
with open('aws_transcribe.txt') as f:
    aws_text = [word for line in f for word in line.split()]

#Initialize Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df.text)

x = pad_squences(tokenizer.texts_to_sequences(df.text),50)
y = df.sentiment

#Build RNN
input = Input((50,), name='input')
embed = Embedding(len(tokenizer.word_index), 100)(input)
embed_dropout = SpatialDropout1D(0.5)(embed)
rnn = Bidirectional(GRI(50, return_sequences=True, recurrent_dropout=0.2))(embed_dropout)
max_pool = GlobalMaxPool1D()(rnn)
avg_pool = GlobalAvgPool1D()(rnn)
concat = Concatenate()([max_pool, avg_pool])
dense = Dense(3, activation='softmax')(concat)

#Train RNN
model = Model(input,dense)
model.compile('adam', 'sparse_categorical_crossentropy', ['sparse_categorical_accuracy'])
model.fit(x, y, batch_size=512, validation_split=0.2, epochs=25)

#Predict Sentiment
model.predict(pad_sequences(tokenizer.texts_to_sequences(aws_text), 50))


