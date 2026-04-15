Output 

Starts with Email
First email found: test123@gmail.com
All emails: ['test123@gmail.com', 'user456@yahoo.com']
Email: test123@gmail.com | Position: 7 - 24
Email: user456@yahoo.com | Position: 34 - 51
Split parts: ['Email:', 'test123@gmail.com', 'backup:', 'user456@yahoo.com']
Hidden emails: Email: ***@gmail.com, backup: ***@yahoo.com


Algorithm

1. re.match()
Algorithm:

Step 1: Start
Step 2: Import re module
Step 3: Store a sentence in variable text
Step 4: Use re.match("python", text) to check match at the beginning
Step 5: If match is found → go to Step 6
Step 6: Print "Python"
Step 7: Else → go to Step 8
Step 8: Print "No match"
Step 9: End

2. re.search()

Algorithm:

Step 1: Start
Step 2: Import re module
Step 3: Store sentence in text
Step 4: Use re.search("hot", text) to find word anywhere
Step 5: If found → go to Step 6
Step 6: Print "Yes, it's hot"
Step 7: Else → go to Step 8
Step 8: Print "Not found"
Step 9: End

3. re.findall()

Algorithm:

Step 1: Start
Step 2: Import re module
Step 3: Store text containing numbers
Step 4: Use re.findall(r"\d+", text) to extract numbers
Step 5: Store result in numbers list
Step 6: Print all numbers
Step 7: End

4. re.finditer()

Algorithm:

Step 1: Start
Step 2: Import re module
Step 3: Store text with repeated words
Step 4: Use re.finditer("apple", text)
Step 5: Loop through each match
Step 6: For each match:
  - Print matched word using match.group()
  - Print starting position using match.start()
  - Print ending position using match.end()
Step 7: End loop
Step 8: End

5. re.split()

Algorithm:

Step 1: Start
Step 2: Import re module
Step 3: Store text with multiple separators
Step 4: Use re.split("[,;|]", text) to split
Step 5: Store result in languages list
Step 6: Print list of languages
Step 7: End

6. re.sub()

Algorithm:

Step 1: Start
Step 2: Import re module
Step 3: Store text with phone number
Step 4: Use re.sub(r"\d", "x", text)
Step 5: Replace all digits with "x"
Step 6: Store result in hidden
Step 7: Print modified text

Step 8: End
