### Python Showcase Random Module ###
print("Beginning of the Python Random Module Showcase\n\n\n")

import random
print("Random Module: Python has a built-in module that you can use to make random numbers. The random module has a set of methods:")


Random_Seed_def = "Random Seed: The seed() method is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number. By default the random number generator uses the current system time. Use the seed() method to customize the start number of the random number generator. Note: If you use the same seed value twice you will get the same random number twice. See example below"
print(f"\n{Random_Seed_def}")
print("    random.seed(10)")
random.seed(10)
print(f"        print(random.random()) = {random.random()}")
print("    random.seed(10)")
random.seed(10)
print(f"        print(random.random()) = {random.random()}")


# Needed to run this because the above seed method froze the random module. The below unfreezes it.
random.seed()


Random_Getstate_def = "Random Getstate: The getstate() method returns an object with the current state of the random number generator. Use this method to capture the state, and use the setstate() method, with the captured state, to restore the state"
Random_Getstate_x = random.getstate()
print(f"\n{Random_Getstate_def}")
print("    Random_Getstate_x = random.getstate()")
print(f"        print(Random_Getstate_x) = {Random_Getstate_x}")




Random_Setstate_def = "Random Setstate: The setstate() method is used to restore the state of the random number generator back to the specified state. Use the getstate() method to capture the state"
print(f"\n{Random_Setstate_def}")
print("    #print a random number:")
print(f"    print(random.random()) = {random.random()}")
print("    #capture the state:")
print("    Random_Setstate_state = random.getstate()")
Random_Setstate_state = random.getstate()
print(f"    print(random.random()) = {random.random()}")
print("    #restore the state:")
random.setstate(Random_Setstate_state)
print("    random.setstate(Random_Setstate_state)")
print("    #and the next random number should be the same as when you captured the state:")
print(f"    print(random.random()) = {random.random()}")




Random_GetRandBits_def = "Random Get Random Bits: The getrandbits() method returns an integer in the specified size (in bits)."
print(f"\n{Random_GetRandBits_def}")
print(f"        print(random.getrandbits(8)) = {random.getrandbits(8)}")
print(f"        print(random.getrandbits(8)) = {random.getrandbits(8)}")
print(f"        print(random.getrandbits(8)) = {random.getrandbits(8)}")




Random_Randrange_def = "Random RandRange: The randrange() method returns a randomly selected element from the specified range."
print(f"\n{Random_Randrange_def}")
print(f"        print(random.randrange(3, 9)) = {random.randrange(3, 9)}")




Random_RandInt_def = "Random Random int: The randint() method returns an integer number selected element from the specified range."
print(f"\n{Random_RandInt_def}")
import random
print(f"        print(random.randint(3, 9)) = {random.randint(3, 9)}")




Random_Choice_def = "Random Choice: The choice() method returns a randomly selected element from the specified sequence. The sequence can be a string, a range, a list, a tuple or any other kind of sequence."
Random_Choice_mylist = ['apple', 'banana', 'cherry']
print(f"\n{Random_Choice_def}")
print("    Random_Choice_mylist = ['apple', 'banana', 'cherry']")
print(f"        print(random.choice(Random_Choice_mylist)) = {random.choice(Random_Choice_mylist)}")




Random_Choices_def = "Random Choices: The choices() method returns a list with the randomly selected element from the specified sequence. You can weigh the possibility of each result with the weights parameter or the cum_weights parameter. The sequence can be a string, a range, a list, a tuple or any other kind of sequence."
Random_Choices_mylist = ['apple', 'banana', 'cherry']
print(f"\n{Random_Choices_def}")
print("    Random_Choices_mylist = ['apple', 'banana', 'cherry']")
print("    sequence	Required. A sequence like a list, a tuple, a range of numbers etc.\n"
      "weights   	     Optional. A list were you can weigh the possibility for each value.Default None\n"
      "cum_weights	     Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated. Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].Default None\n"
      "k	             Optional. An integer defining the length of the returned list")
print(f"        print(random.choices(Random_Choices_mylist, weights = [10, 1, 1], k = 14)) = {random.choices(Random_Choices_mylist, weights = [10, 1, 1], k = 14)}")




Random_Shuffle_def = "Random Shuffle: The shuffle() method takes a sequence, like a list, and reorganize the order of the items. Note: This method changes the original list, it does not return a new list."
Random_Shuffle_mylist = ['apple', 'banana', 'cherry']
random.shuffle(Random_Shuffle_mylist)
print(f"\n{Random_Shuffle_def}")
print("    Random_Shuffle_mylist = ['apple', 'banana', 'cherry']")
print("    random.shuffle(Random_Shuffle_mylist)")
print(f"        print(Random_Shuffle_mylist) = {Random_Shuffle_mylist}")




Random_Sample_def = "Random Sample: The sample() method returns a list with a specified number of randomly selected items from a sequence.    Note: This method does not change the original sequence.    Note: The specified number (k=2) cannot be longer than the length of the original sequence."
Random_Sample_mylist = ['apple', 'banana', 'cherry']
print(f"\n{Random_Sample_def}")
print("    Random_Sample_mylist = ['apple', 'banana', 'cherry']")
print(f"        print(random.sample(Random_Sample_mylist, k=2)) = {random.sample(Random_Sample_mylist, k=2)}")




Random_Random_def = "Random Random: The random() method returns a random floating number between 0 and 1."
print(f"\n{Random_Random_def}")
print(f"        print(random.random()) = {random.random()}")




Random_Uniform_def = "Random Uniform: The uniform() method returns a random floating number between the two specified numbers (both included)."

print(random.uniform(20, 60))
print(f"\n{Random_Uniform_def}")
print(f"        print(random.uniform(20, 60)) = {random.uniform(20, 60)}")




Random_Triangular_def = "Random Triangular: The triangular() method returns a random floating number between the two specified numbers (both included), but you can also specify a third parameter, the mode parameter.   The mode parameter gives you the opportunity to weigh the possible outcome closer to one of the other two parameter values.   The mode parameter defaults to the midpoint between the two other parameter values, which will not weigh the possible outcome in any direction. "
print(f"\n{Random_Triangular_def}")
print("    random.triangular(low, high, mode)")
print(f"        print(random.triangular(20, 60, 30)) = {random.triangular(20, 60, 30)}")



print("\n\n\nEnd of the Python Random Module Showcase")

