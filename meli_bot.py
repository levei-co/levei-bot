from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Response:
  def __init__(self, text, confidence):
    self.text = text
    self.confidence = confidence

class MeliBot: 
  
  def __init__(self): 
    self.bot = ChatBot("MeliBOT")
  
  def train_with(self, origin): 
    trainer = ChatterBotCorpusTrainer(self.bot)
    trainer.train(origin)
  
  def get_response(self, msg):
    resp = self.bot.get_response(msg)
    text = resp.text
    confidence = resp.confidence
    text = text.replace('\\n', '\n').replace('\\n\\n', '\n\n')
    return Response(text, confidence)
