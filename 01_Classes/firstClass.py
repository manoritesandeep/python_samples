class llms:
    token_size = 100

    def __init__(self, query):
        self.query = query

    # Methods 
    def openai(self):
        print(f"I am OpenAI. \nYour query was: {self.query}")

    def claude(self):
        print(f"I am Claude. \nYour query was: {self.query}")

    def llama(self):
        print(f"I am llama. \nYour query was: {self.query}")

# obj1 = llms("Hey OpenAI! Hello World!!!")
# obj1.openai()

# obj2 = llms("Hey Claude! Hello World!!!")
# obj2.claude()

if __name__ == "__main__":
    print("Running __main__ from original file: firstClass.py")
    obj1 = llms("Hey OpenAI! Hello World!!!")
    obj1.openai()