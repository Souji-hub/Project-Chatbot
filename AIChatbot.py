#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import StorageAdapter
from chatterbot.logic import LogicAdapter

#Defining the chatbot
mybot = ChatBot('Vision',storage_adapter='chatterbot.storage.SQLStorageAdapter', #read_only=True, #Used when chatbot is not in learning phase
    logic_adapters=['chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter'
         
    ], preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    database_uri='sqlite:///database.sqlite3')

    #Training the chatbot
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(mybot)
greeting = [
    "Hello",
    "Hi",
    "Hello boss",
    "What is Your Name?",
    "My Name is Vision. I am a ChatBot.",
    "Where are you from?",
    "I am from Nepal. Wbu?",
    "I am from another universe.",
    "I love you",
    "I love you too, mwahh",
    "What's up?",
    "All good",
    "How are you?",
    "I'm fine, you?",
    "Thats good to hear",
    "Thank you.",
    "You're welcome."
]
trainer.train(greeting)

conversation = ["Tell me a joke",
                "A horse walks into a bar. The bartender says, 'Why the long face?'",
                "What do kids play when their mom is using the phone? Bored games.",
                " How does the ocean say hi? It waves!",
                "What do you call a guy who’s really loud? Mike.",
                "Who will win the world cup?",
                "I vote for Argentina.",
                "Do a simple math addition"]
trainer.train(conversation)
nepali = [
    "Namaste.",
    "Namaste Hajur.",
    "Khana Khayeu?",
    "Khana Khaye, Tmile khayeu?",
    "Maile pani khaye.",
    "Very good. Syabaas."
    "weather kasto xa?"
    "Laaastai jaado xa yar"
]
trainer.train(nepali)

#training from corpus
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(mybot)
trainer.train(
    "chatterbot.corpus.english.ai",
    "chatterbot.corpus.english.food",
    "chatterbot.corpus.english.humor",
    "chatterbot.corpus.english.sports",
    "chatterbot.corpus.english.movies"
    )

#Generating response
print ("Soujanya Subedi's Chatbot")
flag= True
while(flag==True):
  response = input('>')
  response = response.lower()
  exit_conditions = ["bye","exit","goodbye"]
  if (response in exit_conditions):
    flag=False
    print("Bot: Goodbye")
   
  else:
     print (mybot.get_response('Bot:'+response))