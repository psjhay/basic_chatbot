chatbot = [ {"user_input":"hello", "bot_resp":"Hello!"},
  {"user_input":"how are", "bot_resp":"I'm doing good. You?"},
  {"user_input":"fine", "bot_resp":"That's good"},
  {"user_input":"help",
   "bot_resp":" I could teach you to program JavaScript or Python. Which do you choose?"},
   {"user_input":"javascript",
    "bot_resp":"Thank you for signing up for my JavaScript tutorial"},
  {"user_input":"python",
   "bot_resp":"Great! You've just signed up for my python tutorial"},
  {"user_input":"thanks","bot_resp":"You're Welcome!"},
  {"user_input":"bye", "bot_resp":"Goodbye! Hope to see you some other time"} ]

while True:
    user_input = input("You: ")
    loc_answer = False
    for dialogue in chatbot:
        match = True
        for word in dialogue["user_input"].split():
            if word not in user_input.lower():
                match = False
        if match:
            print("Bot:", dialogue["bot_resp"])
            loc_answer = True
            break
        
    if not loc_answer:
        print("Bot: ","Could you please rephrase that? ")
            
