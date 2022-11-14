from sys import argv

script, user_name = argv 
prompt = '> '

print(f" Hi {user_name}, i'm the {script} script.")
print("i'd like you to ask you few questions.")
print (f"do you like me {user_name}?")
likes = input(prompt) 

print(f"where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do have?")
computer = input(prompt)

print (f"""
alright so you said {likes} about liking me.
you lives in {lives}. not sure where is that.
and you have {computer} computer. nice.
""")
