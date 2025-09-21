from firstClass import llms

class chatbot(llms):

  def __init__(self, model, query):
    self.model = model
    llms.__init__(self,query)

  def showme(self):
    print(f"Showing: I am calling - {self.model}")
    llms.openai()

# obj_inherit_openai = chatbot("openai", "Hello from inheritence!")
# print(obj_inherit_openai.openai())

obj_inherit_claude = chatbot("claude", "Hello Claude, from inheritence!")
print(obj_inherit_claude.claude())
