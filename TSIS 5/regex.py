#1
import re
string = "abbbabab"
pattern = "ab*"

if re.match(pattern, string):
    print("Match found")
    print(pattern)
else:
    print("Match not found")

#2
import re

string = "abbabb"
pattern = "ab{2,3}"

if re.match(pattern, string):
    print("Match found")
    print(pattern)
else:
    print("Match not found")

#3
import re

string = "hello_world_123"
pattern = "[a-z]+(_[a-z]+)*"

match = re.findall(pattern, string)
print(match)

#4
import re

string = "ThisIsATest"
pattern = "[A-Z][a-z]*"

match = re.findall(pattern, string)
print(match)


#5
import re

string = "abracadabra"
pattern = "a.*b$"

if re.match(pattern, string):
    print("Match found")
    print(pattern)
else:
    print("Match not found")


#6
import re

string = "Hello, world. This is a test."
pattern = "[ ,.]"

new_string = re.sub(pattern, ":", string)
print(new_string)

#7
import re

string = "hello_world_test"
pattern = "(_[a-z])"

new_string = re.sub(pattern, lambda x: x.group(1)[1:].upper(), string)
new_string = new_string.capitalize()

print(new_string)

#8
import re

string = "SplitThisStringAtUpperCaseLetters"
pattern = "(?=[A-Z])"

split_string = re.split(pattern, string)
print(split_string)

#9
import re

string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
pattern = "(?<!^)(?=[A-Z])"

new_string = re.sub(pattern, " ", string)
print(new_string)


#10
import re

string = "ConvertGivenCamelCaseStringToSnakeCase"
pattern = "(?<!^)(?=[A-Z])"

new_string = re.sub(pattern, "_", string).lower()
print(new_string)

