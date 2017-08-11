import time
import random
vastaus = ["I'm sorry, you are gay.", "This world is an illusion.", 
    "the answer is... 42!", "Nigga stole my bike!", "Rather be dead than cool.", 
    "g33kz rule the world", "Eeh, what's up Doc?", "It will be legend,\nwait for it...\nDARY!", 
    "Say whaaat?", "All hail the glorius dead!", "Long live the king!", 
    "Yo man Chigago", "Keep on walking...", "Rollin they see me, hatin they be", 
    "You are l33t h4x0rr!", "Sad, that is just sad...", "Eat my shorts!", 
    "Travel the world and go fuck yourself", "Lol, who just said that?", "Yep, that's how I roll."]

while True:
    _ = input("Ask me a question. : ")
    time.sleep(2)
    print("Thinking...")
    time.sleep(2)
    print("\n")
    print(random.choice(vastaus))
    print("\n")
    time.sleep(1)
    uudestaan = input("Do you want to ask another question? [Y/N] : ").lower()
    if uudestaan == "n" or uudestaan == "no":
        break
    if uudestaan != "y" or uudestaan == "yes":
    	print("Now, now... Try to behave yourself.")
    	time.sleep(2)
    	print("\nOkay, go ahead and ask another question.")
    	time.sleep(1)