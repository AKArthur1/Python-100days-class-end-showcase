### Python Showcase String Methods ###
print("Beginning of the Python String Methods Showcase\n\n\n")

Capitalize_def = "Capitalize: The capitalize() method returns a string where the first character is upper case, and the rest  is lower case."
Capitalize_txt = 'hello, and welcome to my world.'
print(f"\n{Capitalize_def}\n    Capitalize_txt = 'hello, and welcome to my world.'\n        Capitalize_txt.capitalize() = {Capitalize_txt.capitalize()}")




Casefold_def = "Casefold: The casefold() method returns a string where all the characters are lower case. This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method."
Casefold_txt = 'Hello, And Welcome To My World!'
print(f"\n{Casefold_def}\n    Casefold_txt = 'Hello, And Welcome To My World!'\n        Casefold_txt.casefold() = {Casefold_txt.casefold()}")




Center_def = "Center: The center() method will center align the string, using a specified character (space is default) as the fill character."
Center_txt = 'banana'
print(f"\n{Center_def}\n    Center_txt = 'banana'\n        print(Center_txt.center(20)) = {Center_txt.center(20)}\n        print(Center_txt.center(20, 'O')) = {Center_txt.center(20, 'O')}")




Count_def = "Count: The count() method returns the number of times a specified value appears in the string."
Count_txt = 'I love apples, apple are my favorite fruit'
print(f"\n{Count_def}\n    Count_txt = 'I love apples, apple are my favorite fruit'\n        print(Count_txt.count('apple')) = {Count_txt.count('apple')}\n        print(Count_txt.count('apple', 10, 24)) = {Count_txt.count("apple", 10, 24)}")




Encode_def = "Encode: The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used. An optional String specifying the error method can be used. They are; 'backslashreplace', 'ignore', 'namereplace', 'strict', 'replace', 'xmlcharrefreplace'."
Encode_txt = 'My name is Ståle'
print(f"\n{Encode_def}\n    Encode_txt = 'My name is Ståle'\n        print(Encode_txt.encode()) = {Encode_txt.encode()}\n        "
      f"print(Encode_txt.encode(encoding='ascii', errors='backslashreplace')) = {Encode_txt.encode(encoding='ascii', errors='backslashreplace')}\n        "
      f"print(Encode_txt.encode(encoding='ascii', errors='ignore')) = {Encode_txt.encode(encoding='ascii', errors='ignore')}\n        "
      f"print(Encode_txt.encode(encoding='ascii', errors='namereplace')) = {Encode_txt.encode(encoding='ascii', errors='namereplace')}\n        "
      f"print(Encode_txt.encode(encoding='ascii', errors='replace')) = {Encode_txt.encode(encoding='ascii', errors='replace')}\n        "
      f"print(Encode_txt.encode(encoding='ascii', errors='xmlcharrefreplace')) = {Encode_txt.encode(encoding='ascii', errors='xmlcharrefreplace')}")




EndsWith_def = "Ends With: The endswith() method returns True if the string ends with the specified value, otherwise False. Can have an optional integer in the parameters to show start & end points of search."
EndsWith_txt = 'Hello, welcome to my world.'
EndsWith_txt.endswith('.')
print(f"\n{EndsWith_def}\n    EndsWith_txt = 'Hello, welcome to my world.'\n        print(EndsWith_txt.endswith('.')) = {EndsWith_txt.endswith('.')}"
      f"\n        print(EndsWith_txt.endswith('my world.')) = {EndsWith_txt.endswith('my world.')}"
      f"\n        print(EndsWith_txt.endswith('my world.', 5, 11)) = {EndsWith_txt.endswith('my world.', 5, 11)}"
      f"\n        print(EndsWith_txt.endswith(('world.', 'castle.'))) = {EndsWith_txt.endswith(('world.', 'castle.'))}")




ExpandTabs_def = "Expand Tabs: The expandtabs() method sets the tab size to the specified number of whitespaces."
ExpandTabs_txt = 'H\te\tl\tl\to'
print(f"\n{ExpandTabs_def}"
      f"\n    ExpandTabs_txt = 'H\te\tl\tl\to'"
      f"\n        print(ExpandTabs_txt.expandtabs(2)) = {ExpandTabs_txt.expandtabs(2)}"
      f"\n        print(ExpandTabs_txt.expandtabs()) = {ExpandTabs_txt.expandtabs()}"
      f"\n        print(ExpandTabs_txt.expandtabs(4)) = {ExpandTabs_txt.expandtabs(4)}"
      f"\n        print(ExpandTabs_txt.expandtabs(10)) = {ExpandTabs_txt.expandtabs(10)}")




Find_def = "Find: The find() method finds the first occurrence of the specified value, returns -1 if the value is not found, and is almost the same as the index() method, the only difference is that index() method raises an exception if the value is not found. "
Find_txt = 'Hello, welcome to my world.'
print(f"\n{Find_def}"
      f"\n    Find_txt = 'Hello, welcome to my world.'"
      f"\n        print(Find_txt.find('welcome')) = {Find_txt.find('welcome')}"
      f"\n        print(Find_txt.find('e', 5, 10)) = {Find_txt.find('e', 5, 10)}")




Format_def = "Format: The format() method formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: {}. The method returns the formatted string."
Format_txt = 'For only {price:.2f} dollars!'
Format_txt.format(price = 49)
print(f"\n{Format_def}")
print("    Format_txt = 'For only {price:.2f} dollars!'")
print(f"        print(Format_txt.format(price = 49)) = {Format_txt.format(price = 49)}")
print("    'My name is {fname}, I'm {age}'.format(fname = 'John', age = 36) = ")
print("    ",        "My name is {fname}, I'm {age}".format(fname = 'John', age = 36))



FormatMap_def = "Format Map: The format_map() method formats the specified values of a dictionary and insert them inside the string's placeholders. Returns the formatted string."
FormatMap_myvar = {'name': 'Jane', 'age': 36}
FormatMap_txt = 'Happy birthday {name} you are now on level {age}!'
print(f"\n{FormatMap_def}")
print("    FormatMap_myvar = {'name': 'Jane', 'age': 36}")
print("    FormatMap_txt = 'Happy birthday {name} you are now on level {age}!'")
print(f"        print(FormatMap_txt.format_map(FormatMap_myvar)) = {FormatMap_txt.format_map(FormatMap_myvar)}")




Index_def = "Index: The index() method finds the first occurrence of the specified value. Raises an exception if the value is not found. Is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found."
Index_txt = 'Hello, welcome to my world.'
print(f"\n{Index_def}"
      f"\n    Index_txt = 'Hello, welcome to my world.'"
      f"\n        print(Index_txt.index('welcome')) = {Index_txt.index('welcome')}")




IsAllNumbers_def = "Is All Numbers: The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)."
IsAllNumbers_txt = 'Company12'
print(f"\n{IsAllNumbers_def}"
      f"\n    IsAllNumbers_txt = 'Company12'"
      f"\n        print(IsAllNumbers_txt.isalnum()) = {IsAllNumbers_txt.isalnum()}")




IsAlpha_def = "Is Alphabet: The isalpha() method returns True if all the characters are alphabet letters (a-z)."
IsAlpha_txt = 'Company10'
print(f"\n{IsAlpha_def}"
      f"\n    IsAlpha_txt = 'Company10'"
      f"\n        print(IsAlpha_txt.isalpha()) = {IsAlpha_txt.isalpha()}")




IsAscii_def = "Is Ascii: The isascii() method returns True if all the characters are ascii characters (a-z)."
IsAscii_txt = 'Companyå123'
print(f"\n{IsAscii_def}"
      f"\n    IsAscii_txt = 'Companyå123'"
      f"\n        print(IsAscii_txt.isascii()) = {IsAscii_txt.isascii()}")




IsDecimal_def = "Is Decimal: The isdecimal() method returns True if all the characters are decimals (0-9). This methode can also be used on Unicode objects."
IsDecimal_txt = '1234'
print(f"\n{IsDecimal_def}"
      f"\n    IsDecimal_txt = '1234'"
      f"\n        print(IsDecimal_txt.isdecimal()) = {IsDecimal_txt.isdecimal()}")




IsDigit_def = "Is Digit: The isdigit() method returns True if all the characters are digits, otherwise False. Exponents, like ², are also considered to be a digit."
IsDigit_txt = '50800'
print(f"\n{IsDigit_def}"
      f"\n    IsDigit_txt = '50800'"
      f"\n        print(IsDigit_txt.isdigit()) = {IsDigit_txt.isdigit()}")




IsIdentifier_def = "Is Identifier: The isidentifier() method returns True if the string is a valid identifier, otherwise False. A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces."
IsIdentifier_txt = 'Demo'
print(f"\n{IsIdentifier_def}"
      f"\n    IsIdentifier_txt = 'Demo'"
      f"\n        print(IsIdentifier_txt.isidentifier()) = {IsIdentifier_txt.isidentifier()}")




IsLowercase_def = "Is Lowercase: The islower() method returns True if all the characters are in lower case, otherwise False."
IsLowercase_txt = 'hello world!'
print(f"\n{IsLowercase_def}"
      f"\n    IsLowercase_txt = 'hello world!'"
      f"\n        print(IsLowercase_txt.islower()) = {IsLowercase_txt.islower()}")




IsNumeric_def = "Is Numeric: The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False. Exponents, like ² and ¾ are also considered to be numeric values. '-1' and '1.5' are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not."
IsNumeric_txt = '565543'
print(f"\n{IsNumeric_def}"
      f"\n    IsNumeric_txt = '565543'"
      f"\n        print(IsNumeric_txt.isnumeric()) = {IsNumeric_txt.isnumeric()}")




IsPrintable_def = "Is Printable: The isprintable() method returns True if all the characters are printable, otherwise False. Example of none printable character can be carriage return and line feed."
IsPrintable_txt = 'Hello! Are you #1?'
print(f"\n{IsPrintable_def}"
      f"\n    IsPrintable_txt = 'Hello! Are you #1?'"
      f"\n        print(IsPrintable_txt.isprintable()) = {IsPrintable_txt.isprintable()}")
print("        'Hello!  ***BACKSLASHn***  Are you #1?' = Is an example of a non printable string so it would return False")




IsSpace_def = "Is Space: The isspace() method returns True if all the characters in a string are whitespaces, otherwise False."
IsSpace_txt = '   s   '
print(f"\n{IsSpace_def}"
      f"\n    IsSpace_txt = '   s   '"
      f"\n        print(IsSpace_txt.isspace()) = {IsSpace_txt.isspace()}")




IsTitleCase_def = "Is Title Case: The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False."
IsTitleCase_txt = 'Hello, And Welcome To My World!'
print(f"\n{IsTitleCase_def}"
      f"\n    IsTitleCase_txt = 'Hello, And Welcome To My World!'"
      f"\n        print(IsTitleCase_txt.istitle()) = {IsTitleCase_txt.istitle()}")




IsUpper_def = "Is Upper: The isupper() method returns True if all the characters are in uppercase, otherwise False."
IsUpper_txt = 'THIS IS NOW!'
print(f"\n{IsUpper_def}"
      f"\n    IsUpper_txt = 'THIS IS NOW!'"
      f"\n        print(IsUpper_txt.isupper()) = {IsUpper_txt.isupper()}")




Join_def = "Join: The join() method takes all items in an iterable and joins them into one string."
Join_myTuple = ('John', 'Peter', 'Vicky')
print(f"\n{Join_def}"
      f"\n    Join_myTuple = ('John', 'Peter', 'Vicky')"
      f"\n        print('#'.join(Join_myTuple)) = {'#'.join(Join_myTuple)}")




L_Justified_def = "Left Justify: The ljust() method will left align the string, using a specified character (space is default) as the fill character."
L_Justified_txt = 'banana'
L_Justified_x = L_Justified_txt.ljust(20)
print(f"\n{L_Justified_def}"
      f"\n    L_Justified_txt = 'banana'"
      f"\n    L_Justified_x = L_Justified_txt.ljust(20)"
      f"\n        print(L_Justified_x, 'is my favorite fruit.') = {L_Justified_x + 'is my favorite fruit.'}")




LowerCase_def = "Lower Case: The lower() method returns a string where all characters are lower case."
LowerCase_txt = 'Hello my FRIENDS'
print(f"\n{LowerCase_def}"
      f"\n    LowerCase_txt = 'Hello my FRIENDS'"
      f"\n        print(LowerCase_txt.lower()) = {LowerCase_txt.lower()}")




LeadingCharStrip_def = "Leading Character Strip: The lstrip() method removes any leading characters (space is the default leading character to remove)"
LeadingCharStrip_txt = ',,,,,ssaaww.....banana'
print(f"\n{LeadingCharStrip_def}"
      f"\n    LeadingCharStrip_txt = ',,,,,ssaaww.....banana'"
      f"\n        print(LeadingCharStrip_txt.lstrip(',.asw')) = {LeadingCharStrip_txt.lstrip(',.asw')}"
      f"\n        print(LeadingCharStrip_txt.lstrip(',.sw')) = {LeadingCharStrip_txt.lstrip(',.sw')}")




MakeTranslate_def = "Make Translation mapping table: maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters. (MakeTranslate_x, MakeTranslate_y, z)"
MakeTranslate_txt = 'Hi Sam!'
MakeTranslate_x = 'mSa'
MakeTranslate_y = 'eJo'
MakeTranslate_mytable = str.maketrans(MakeTranslate_x, MakeTranslate_y)
print(f"\n{MakeTranslate_def}"
      f"\n    MakeTranslate_txt = 'Hi Sam!'"
      f"\n    MakeTranslate_x = 'mSa'"
      f"\n    MakeTranslate_y = 'eJo'"
      f"\n    MakeTranslate_mytable = str.maketrans(MakeTranslate_x, MakeTranslate_y)"
      f"\n        print(MakeTranslate_txt.translate(MakeTranslate_mytable)) = {MakeTranslate_txt.translate(MakeTranslate_mytable)}")




Partition_def = "Partition: The partition() method searches for a specified string, and splits the string into a tuple containing three elements. The first element contains the part before the specified string. The second element contains the specified string. The third element contains the part after the string."
Partition_txt = 'I could eat bananas all day'
print(f"\n{Partition_def}"
      f"\n    Partition_txt = 'I could eat bananas all day'"
      f"\n        print(Partition_txt.partition('bananas')) = {Partition_txt.partition('bananas')}")




Replace_def = "Replace: The replace() method replaces a specified phrase with another specified phrase."
Replace_txt = 'one one was a race horse, two two was one too.'
print(f"\n{Replace_def}"
      f"\n    Replace_txt = 'one one was a race horse, two two was one too.'"
      f"\n        print(Replace_txt.replace('one', 'three', 2)) = {Replace_txt.replace('one', 'three', 2)}")




RFind_def = "R Find: The rfind() method finds the last occurrence of the specified value. Method is almost the same as the rindex() method."
RFind_txt = 'Hello, welcome to my world.'
print(f"\n{RFind_def}"
      f"\n    RFind_txt = 'Hello, welcome to my world.'"
      f"\n        print(RFind_txt.rfind('e', 5, 10)) = {RFind_txt.rfind('e', 5, 10)}"
      f"\n        print(RFind_txt.rfind('e', 5, 30)) = {RFind_txt.rfind('e', 5, 30)}")




Rindex_def = "R Index: The rindex() method finds the last occurance of the specified value, raises an exception if the value is not found. It is almost the same as the same as the rfind() method."
Rindex_txt = 'Mi casa, su casa.'
print(f"\n{Rindex_def}"
      f"\n    Rindex_txt = 'Mi casa, su casa.'"
      f"\n        print(Rindex_txt.rindex('casa')) = {Rindex_txt.rindex('casa')}")




RJust_def = "R Just: The rjust() method will right align the string, using a specified character ( space is default) as the fill character."
RJust_txt = 'banana'
print(f"\n{RJust_def}"
      f"\n    RJust_txt = 'banana'"
      f"\n        print(RJust_txt.rjust(20, 'O')) = {RJust_txt.rjust(20, 'O')}")




RPartition_def = "R Partition: The rpartition() method searches for the last occurance of a specified string, and splits the string into a tuple containing three elements. The first element contains the part before the specified string. The second element contains the specified string. The third element contains the part after the string."
RPartition_txt = 'I could eat bananas all day, bananas are my favorite fruit'
print(f"\n{RPartition_def}"
      f"\n    RPartition_txt = 'I could eat bananas all day, bananas are my favorite fruit'"
      f"\n        print(RPartition_txt.rpartition('bananas')) = {RPartition_txt.rpartition('bananas')}")




RSplit_def = "R Split: The rsplit() method splits a string into a list, starting from the right. If no 'max' is specified, this method will return the same as the split() method."
RSplit_txt = 'apple, banana, orange, cherry'
print(f"\n{RSplit_def}"
      f"\n    RSplit_txt = 'apple, banana, orange, cherry'"
      f"\n        print(RSplit_txt.rsplit(', ')) = {RSplit_txt.rsplit(', ')}")




RStrip_def = "R Strip: The rstrip() method removes any trailing characters (characters at the end of a string), space is the default trailing character to remove."
RStrip_txt = '     banana     '
print(f"\n{RStrip_def}"
      f"\n    RStrip_txt = '     banana     '"
      f"\n        print('of all Append_fruits', x, 'is my favorite') = {'of all Append_fruits', RStrip_txt.rstrip(), 'is my favorite'}")




Split_def = "Split: The split() method splits a string into a list. You can specify the separator, default separator is any whitespace."
Split_txt = 'apple#banana#cherry#orange'
print(f"\n{Split_def}"
      f"\n    Split_txt = 'apple#banana#cherry#orange'"
      f"\n        print(Split_txt.split('#')) = {Split_txt.split('#')}")




SplitLines_def = "Split Lines: The splitlines() method splits a string into a list. The splitting is done at line breaks."
Split_txt = 'Thank you for the music\nWelcome to the jungle'
print(f"\n{SplitLines_def}"
      f"\n    Split_txt = 'Thank you for the music\nWelcome to the jungle'"
      f"\n        print(Split_txt.splitlines(True)) = {Split_txt.splitlines(True)}")




StartsWith_def = "Starts With: The startswith() method returns True if the string starts with the specified value, otherwise False."
StartsWith_txt = 'Hello, welcome to my world.'
print(f"\n{StartsWith_def}"
      f"\n    StartsWith_txt = 'Hello, welcome to my world.'"
      f"\n        print(StartsWith_txt.startswith('Hello')) = {StartsWith_txt.startswith('Hello')}")




Strip_def = "Strip: The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end. You can specify which characters to remove, if not, any whitespaces will be removed."
Strip_txt = '     banana     '
print(f"\n{Strip_def}"
      f"\n    Strip_txt = '     banana     '"
      f"\n        print('of all Append_fruits', Strip_txt.strip(), 'is my favorite') = {'of all Append_fruits', Strip_txt.strip(), 'is my favorite'}")




SwapCase_def = "Swap Case: The swapcase() method returns a string where all the upper case letters are lower case and vice versa."
SwapCase_txt = 'Hello My Name Is PETER'
print(f"\n{SwapCase_def}"
      f"\n    SwapCase_txt = 'Hello My Name Is PETER'"
      f"\n        print(SwapCase_txt.swapcase()) = {SwapCase_txt.swapcase()}")




Title_def = "Title: The title() method returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after that will be converted to upper case."
Title_txt = 'hello b2b2b2 and 3g3g3g'
print(f"\n{Title_def}"
      f"\n    Title_txt = 'hello b2b2b2 and 3g3g3g'"
      f"\n        print(Title_txt.title()) = {Title_txt.title()}")




Translate_def = "Translate: The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table. Use the maketrans() method to create a mapping table. If a character is not specified in the dictionary/table, the character will not be replaced. If you use a dictionary, you must use ascii codes instead of characters."
Translate_txt = 'Hello Sam!'
Translate_mytable = str.maketrans('S', 'P')
print(f"\n{Translate_def}"
      f"\n    Translate_txt = 'Hello Sam!'"
      f"\n    Translate_mytable = str.maketrans('S', 'P')"
      f"\n        print(Translate_txt.translate(Translate_mytable)) = {Translate_txt.translate(Translate_mytable)}")




Upper_def = "Upper: The upper() method returns a string where all characters are in upper case."
Upper_txt = 'Hello my friends'
print(f"\n{Upper_def}"
      f"\n    Upper_txt = 'Hello my friends'"
      f"\n        print(Upper_txt.upper()) = {Upper_txt.upper()}")




ZFill_def = "ZFill: The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length. If the value of the len parameter is less than the length of the string, no filling is done."
ZFill_txt = '50'
print(f"\n{ZFill_def}"
      f"\n    ZFill_txt = '50'"
      f"\n        print(ZFill_txt.zfill(10)) = {ZFill_txt.zfill(10)}")



print("\n\n\nEnd of the Python String Methods Showcase")