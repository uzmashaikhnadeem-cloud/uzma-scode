import datetime
import time
name=input("Wat's your name:")
hour= datetime.datetime.now().hour
if  5<= hour<=12:
    print("Good Morning🌅:",name)
elif 12<=hour<=17:
    print("Good Afternoon🕛:",name)
elif 17<=hour<=21:
    print("Good Evening🌆:",name)
else:
    print("Good Night🌃:",name)

print("WELCOME SIR/MAM💛")
print("Iam your mini ai chatbot 🤖")
print("you can ask me anything,but make sure to type bye while exit")

QnAdict={ "HELLO":"hi! how are you",
          "I AM FINE":"Good to hear that,How can i help you",
          "HAPPY":"Great to here that",
          "ARE YOU A.I":"Yes i am ai autommated mini chat bot",
          "EMOTIONS":"I thing you want to discuss about EMOTIONS in deep?",
          "SAD":"okayy!NO worries i am always there with uh,WHAT HAPPENNED? "
          }
def func(user):
    user=user.upper()
    for a in QnAdict:
        if a in user:
            return QnAdict[a]
    return ("SORRY 🙏🏻 !I dont know,but iam learning soon")  
  
while True:
    user=input("Please Ask your Question:")
    if "bye" in user.lower():
        print("BYE!see you next time💛")
        break
    print("Chatbot ANS:",func(user))    
       