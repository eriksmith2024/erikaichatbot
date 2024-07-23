#AI Chatbot
import random
greetings = [ "Welcome please enter a topic I can assist you on", "Good to see you, enter a topic you want to discuss", "How may I help", "Anything I can support you with",]
bye = ["Goodbye", "Hope I have helped", "Don't hesitate if you need anything else"]

keywords = ["policies", "template", "bonus", "payroll", "benefits"]
responses = ["Here is a link your new company policies", "Here is a list of templates for common management meetings", "Here is a link to our bonus structure", "Please check your pay details are correct", "Here are link to your new benfits Pension, Group Income Protection, Private Mecial Insurance, Company Car Allowance, Sick Pay, "]

print(random.choice(greetings))

#take input from user

user_input = input("policy template bonus payroll benefits, Type topic? (type bye to quit):")

while (user_input != "bye"):
    keyword_found = False
    for index in range(len(keywords)):
        if (keywords[index] in user_input):
            print("Bot: "+ responses[index])
            keyword_found = True

    if(keyword_found == False):
        new_keyword = input("I don't understand your keyword. What keyword is it? ")
        keywords.append(new_keyword)
        new_response = input ("For the new keyword what response would you like? ")
        responses.append(new_response)

    user_input = input("How can I help you? (type bye to quit): ")
    user_input = user_input.lower()

print(random.choice(bye))