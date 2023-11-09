import random

(lambda x: print("Heads") if x==0 else print("Tails"))(random.randint(0,1))
