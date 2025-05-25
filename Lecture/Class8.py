# Regular Expression

# regexp
# used for strings
# import re
# it validates the input

import re

pattern = "apple"

if re.match(pattern,"applepineapple"): # It is case-sensitive and take the string and match with first characters itself
    print("Match found") # won't work for apppineaple -> the pattern string should match with string with first characters itself
else:
    print("Not match")

# match() function

# match(pattern,string,flags)

import re

pattern = "apple"

if re.match(pattern,"appapple"): # It is case-sensitive and take the string and match with first characters itself
    print("Match found") # won't work for apppineaple -> the pattern string should match with string with first characters itself
else:
    print("Not match")

# findall() function

# findall(pattern,string,flags)

# Case 1:
if re.findall(pattern,"applepineapple"): print("Match found")
else: print("Not match")

# Case 2:
check1 = re.findall("p",pattern)
check2 = re.findall("a",pattern)
check3 = re.findall("btf",pattern)
print(check1)
print(check2)
print(check3)

# search() function

# search(pattern,string,flags)

if re.search(pattern,"pineapple"): print("Match found")
else: print("Not match")


# sub() function

# sub(pattern,repl,string,count,flags)

pat = "dog"
string = "It's a dog"

substitute = re.sub(pat,"cat",string, count=0,flags=0)

print(substitute)


# Character and character sequences

# ^ - Matches the beginning of a line
# $ - Matches the end of a line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non-digit
# \s - Matches whitespace
# \S - Matches any non-whitespace

"""

string1 = "It's a dog 75"
pattern1 = "^I"
pattern2 = "5$"
pattern3 = "."
pattern4 = "^I......"
pattern5 = ".....5$"
 # pattern6 = "\D"
 # pattern7 = "\d"
pattern8 = "\S"
pattern9 = "\s"
pattern10 = "^I."


print(re.findall(pattern1,string1))
print(re.findall(pattern2,string1))
print(re.findall(pattern3,string1))
print(re.findall(pattern4,string1))
print(re.findall(pattern5,string1))
print(re.findall(pattern6,string1))
print(re.findall(pattern7,string1))
print(re.findall(pattern8,string1))
print(re.findall(pattern9,string1))
print(re.findall(pattern10,string1))

"""


# * - Repeats character zero or more times
# + - Repeats character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression 0 to 1 time


mail = "From amit@gmal.com"

pat1 = r"^From (\S+@\S+)"

ex = re.findall(pat1,mail)
print(ex)


# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character
# [a-z 0-9] - Set of characters can include a range
# {}

"""
Here's a **Beginner to Pro Tutorial for Regular Expressions (RegEx) in Python**, structured in a step-by-step, digestible format.

---

# 📘 Regular Expressions (RegEx) in Python – Beginner to Pro

---

## 🔹 What is RegEx?

**Regular Expressions (RegEx)** are patterns used to match character combinations in strings.

In Python, RegEx is supported by the **`re`** module.

```python
import re
```

---

## 🔰 Level 1: Basics of RegEx

### ▶️ Match a Pattern with `re.search()`

```python
import re
pattern = r"cat"
text = "The cat is on the roof"
match = re.search(pattern, text)
print(match)  # <re.Match object>
```

### ▶️ `re.findall()`

Returns all matches.

```python
 # re.findall(r"\d+", "There are 24 apples and 35 bananas")  # ['24', '35']
```

### ▶️ `re.match()` vs `re.search()`

* `match()` checks only at the beginning.
* `search()` checks the whole string.

---

## 🔡 Basic Metacharacters

| Metacharacter | Meaning                      | Example                                      |
| ------------- | ---------------------------- | -------------------------------------------- |
| `.`           | Any character except newline | `a.b` matches `acb`, `axb`                   |
| `^`           | Start of string              | `^hello` matches `hello world`               |
| `$`           | End of string                | `world$` matches `hello world`               |
| `*`           | 0 or more times              | `go*gle` matches `ggle`, `google`, `gooogle` |
| `+`           | 1 or more times              | `go+gle` matches `google` but not `ggle`     |
| `?`           | 0 or 1 time                  | `go?gle` matches `ggle` and `gogle`          |
| `{n}`         | Exactly n times              | `a{3}` matches `aaa`                         |
| `{n,}`        | n or more                    | `a{2,}` matches `aa`, `aaa`, `aaaa`          |
| `{n,m}`       | Between n and m              | `a{2,4}` matches `aa`, `aaa`, `aaaa`         |

---

## 🔤 Character Sets

| Pattern  | Description                    |
| -------- | ------------------------------ |
| `[abc]`  | Match one of: a, b, or c       |
| `[a-z]`  | Match lowercase letters a to z |
| `[A-Z]`  | Match uppercase letters A to Z |
| `[0-9]`  | Match any digit                |
| `[^0-9]` | Match anything *except* digits |

---

## 🧩 Special Sequences

| Code | Meaning                            |
| ---- | ---------------------------------- |
| `\d` | Digit (0–9)                        |
| `\D` | Not a digit                        |
| `\s` | Whitespace                         |
| `\S` | Not whitespace                     |
| `\w` | Word character (a-z, A-Z, 0–9, \_) |
| `\W` | Not a word character               |
| `\b` | Word boundary                      |
| `\B` | Not word boundary                  |

Example:

```python
re.findall(r"\bcat\b", "A cat is not a scatter")  # ['cat']
```

---

## 🧠 Level 2: Grouping and Capturing

### ▶️ Parentheses `()` capture groups

```python
text = "John, 25; Amy, 30"
pattern = r"(\w+), (\d+)"
matches = re.findall(pattern, text)
print(matches)  # [('John', '25'), ('Amy', '30')]
```

### ▶️ Named Groups

```python
pattern = r"(?P<name>\w+), (?P<age>\d+)"
match = re.search(pattern, "John, 25")
print(match.group("name"))  # John
```

---

## 🧪 Level 3: Advanced Techniques

### ▶️ Substitution with `re.sub()`

```python
re.sub(r"\d+", "XX", "There are 123 apples")  # "There are XX apples"
```

### ▶️ Splitting Strings with `re.split()`

```python
re.split(r"[,.!?]", "Hello, world! How are you?")  
# ['Hello', ' world', ' How are you', '']
```

### ▶️ Lookahead & Lookbehind

| Syntax     | Description         |
| ---------- | ------------------- |
| `(?=...)`  | Positive lookahead  |
| `(?!...)`  | Negative lookahead  |
| `(?<=...)` | Positive lookbehind |
| `(?<!...)` | Negative lookbehind |

```python
re.findall(r"\w+(?=\.)", "filename.txt")  # ['filename']
```

---

## ✅ Level 4: Compilation and Flags

### ▶️ Using `re.compile()`

```python
pattern = re.compile(r"\d+")
pattern.findall("I am 25 and she is 30")  # ['25', '30']
```

### ▶️ Common Flags

| Flag                      | Use                              |
| ------------------------- | -------------------------------- |
| `re.IGNORECASE` or `re.I` | Case-insensitive matching        |
| `re.DOTALL` or `re.S`     | `.` matches newline too          |
| `re.MULTILINE` or `re.M`  | `^` and `$` match line start/end |

```python
re.findall(r"^start", "start here\nstart again", re.M)
```

---

## 📊 Pro Tips

* **Test your patterns** at: [https://regex101.com/](https://regex101.com/)
* **Verbose Mode** for readability:

```python
pattern = re.compile(r"""
  #  (\w+)      # name
  #  ,\s+       # comma and space
   # (\d+)      # age
""", re.VERBOSE)
```

---

## 🧪 Practice Challenges

1. Extract all emails from text.
2. Validate a phone number: `(XXX) XXX-XXXX`
3. Match a valid date: `dd/mm/yyyy`
4. Replace HTML tags from a string.
5. Validate passwords: 8+ chars, 1 digit, 1 uppercase, 1 special.

---
"""

ptrn = r"cat"
txt = "The cat is on the roof"
mtch = re.search(ptrn, txt)
print(mtch)  # <re.Match object>


print(re.findall(r"\d+", "There are 24 apples and 35 bananas"))  # ['24', '35']


print(re.findall(r"\bcat\b", "A cat is not a scatter"))


txt1 = "John, 25; Amy, 30"
ptrn1 = r"(\w+), (\d+)" # Parentheses `()` capture groups
mtchs = re.findall(ptrn1, txt1)
print(mtchs)  # [('John', '25'), ('Amy', '30')]


"""
✅ * – Zero or More Times
Pattern: go*gle

Explanation:

o* means zero or more occurrences of o.

So, it will match:

"ggle" (0 o)

"gogle" (1 o)

"google" (2 o)

"gooogle" (3 o)

and so on...

Visual Breakdown:

Input	Matches go*gle?	Why
ggle	✅ Yes	o appears 0 times → valid
gogle	✅ Yes	o appears once → valid
google	✅ Yes	o appears twice → valid
gooogle	✅ Yes	o appears 3 times → valid
ggogle	❌ No	Extra g breaks the pattern

✅ + – One or More Times
Pattern: go+gle

Explanation:

o+ means at least one occurrence of o.

So, it will match:

"gogle" (1 o)

"google" (2 o)

"gooogle" (3 o)

It will NOT match "ggle" (0 o).

Visual Breakdown:

Input	Matches go+gle?	Why
ggle	❌ No	o appears 0 times → invalid
gogle	✅ Yes	o appears once → valid
google	✅ Yes	o appears twice → valid
gooogle	✅ Yes	o appears 3 times → valid

✅ ? – Zero or One Time
Pattern: go?gle

Explanation:

o? means optional o — it can appear once or not at all.

So, it will match:

"ggle" (0 o)

"gogle" (1 o)

It will NOT match "google" (2 o).

Visual Breakdown:

Input	Matches go?gle?	Why
ggle	✅ Yes	o appears 0 times → valid
gogle	✅ Yes	o appears once → valid
google	❌ No	o appears twice → invalid

🎯 Summary Table
Quantifier	Meaning	Example	Matches
*	0 or more	go*gle	ggle, gogle, google, gooogle
+	1 or more	go+gle	gogle, google, gooogle
?	0 or 1	go?gle	ggle, gogle


"""

ptrn2 = r"(?P<name>\w+), (?P<age>\d+)" # the P in (?P<name>...) stands for "Python-style named group".
mtch2 = re.search(ptrn2, "John, 25")
print(mtch2.group("name"))  # John

"""
(?P<name>...) is a named capturing group in Python’s regular expression syntax.

?P<name>: This tells Python to name this group name.

# \w+: This part matches one or more word characters (i.e., [A-Za-z0-9_])

\d+: Matches one or more digits.

So, the full pattern:


(?P<name>\w+), (?P<age>\d+)
matches a string like:

John, 25

And extracts:

"John" as the group named "name"

"25" as the group named "age"


Instead of referencing groups by number like match.group(1) or match.group(2), you can use:
match.group("name")  # easier to understand
match.group("age")

🔁 Equivalent Without Named Groups:
This pattern:

python
Copy
Edit
pattern = r"(?P<name>\w+), (?P<age>\d+)"
is functionally equivalent to:

python
Copy
Edit
pattern = r"(\w+), (\d+)"
But then you'd access with:

python
Copy
Edit
match.group(1)  # name
match.group(2)  # age
Less clear, especially in big patterns.

"""

print(re.sub(r"\d+", "56", "There are 123 apples"))  # "There are XX apples"

print(re.split(r"[,.!?]", "Hello, world! How are you?")) # This is a character class, defined by the square brackets [ ].

"""
Inside the class: [,.!?] means "match any one of these characters":

, → comma

. → period (dot)

! → exclamation mark

? → question mark

So this regex will match any one of those punctuation marks.

🧪 The Input: "Hello, world! How are you?"
This string has:

a comma ,

an exclamation mark !

a question mark ?

📤 What re.split() does here:
It splits the string whenever it sees one of those characters.

📘 Why the last empty string?
Because the string ends with a ?, and there’s nothing after it, Python returns an empty string '' as the last element.
"""

parts = [s.strip() for s in re.split(r"[,.!?]", "Hello, world! How are you?") if s.strip()]
print(parts)

"""
🔎 1. Positive Lookahead: (?=...)
Checks if something comes after your pattern — but doesn’t include it in the match.

python
Copy
Edit
import re
re.findall(r"\w+(?=\d)", "item1 item2 itemX")
📤 Output:
python
Copy
Edit
['item', 'item']
✅ Explanation:

Match any word (\w+) followed by a digit ((?=\d))

Only the word part is returned (item), digit is just checked but not included.

❌ 2. Negative Lookahead: (?!...)
Checks if something does NOT come after your pattern.

python
Copy
Edit
re.findall(r"apple(?!\sjuice)", "apple apple juice apple pie")
📤 Output:
python
Copy
Edit
['apple', 'apple']
✅ Explanation:

Match apple only if not followed by " juice" (with space).

Skips "apple juice", matches other instances.

🔙 3. Positive Lookbehind: (?<=...)
Checks if something comes before your pattern — but doesn’t include it in the match.

python
Copy
Edit
re.findall(r"(?<=\$)\d+", "Price: $20, not $5, or 30")
📤 Output:
python
Copy
Edit
['20', '5']
✅ Explanation:

Match numbers that are preceded by a dollar sign $.

$ is not included in result.

❌ 4. Negative Lookbehind: (?<!...)
Checks if something does NOT come before your pattern.

python
Copy
Edit
re.findall(r"(?<!\$)\d+", "Price: $20, not $5, or 30")
📤 Output:
python
Copy
Edit
['30']
✅ Explanation:

Match number not preceded by $

Ignores $20, $5, matches only 30

🧠 Summary Visual
php-template
Copy
Edit
Positive Lookahead     A(?=B)   ⇒ match A only if followed by B
Negative Lookahead     A(?!B)   ⇒ match A only if NOT followed by B
Positive Lookbehind    (?<=B)A  ⇒ match A only if preceded by B
Negative Lookbehind    (?<!B)A  ⇒ match A only if NOT preceded by B


"""

"""
Absolutely! Let’s go through each of your regex practice challenges with **step-by-step explanations** 🧠

---

## ✅ 1. **Extract all emails from text**

```python
import re

text = "Contact us at hello@example.com, support123@test.co.in or visit our site."

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)
```

### 🔍 Explanation:

* `[a-zA-Z0-9._%+-]+` → Local part before `@`
* `@` → Literal `@`
* `[a-zA-Z0-9.-]+` → Domain name
* `\.` → Dot before domain extension
* `[a-zA-Z]{2,}` → Top-level domain (like `.com`, `.co.in`)
* `re.findall()` → Returns **all matches** in a list.

### ✅ Output:

```
['hello@example.com', 'support123@test.co.in']
```

---

## ✅ 2. **Validate a phone number: `(XXX) XXX-XXXX`**

```python
import re

phone = "(123) 456-7890"

match = re.fullmatch(r"\(\d{3}\) \d{3}-\d{4}", phone)
print("Valid" if match else "Invalid")
```

### 🔍 Explanation:

* `\(` and `\)` → Match literal parentheses
* `\d{3}` → Exactly 3 digits
* Space ` ` after `)`
* `\d{3}` → Next 3 digits
* Hyphen `-`
* `\d{4}` → Last 4 digits
* `re.fullmatch()` → Ensures the **entire string** matches the pattern

### ✅ Output:

```
Valid
```

---

## ✅ 3. **Match a valid date: `dd/mm/yyyy`**

```python
import re

text = "Valid: 01/01/2020, 12/12/1999. Invalid: 32/13/2020"

dates = re.findall(
    r"\b(0[1-9]|[12][0-9]|3[01])/"   # Day: 01-31
    r"(0[1-9]|1[0-2])/"              # Month: 01-12
    r"(19|20)\d{2}\b",               # Year: 1900–2099
    text
)

# Join tuple results to full dates
print(["/".join(date) for date in dates])
```

### 🔍 Explanation:

* `(0[1-9]|[12][0-9]|3[01])` → Valid day: 01–31
* `(0[1-9]|1[0-2])` → Valid month: 01–12
* `(19|20)\d{2}` → Year starts with 19 or 20
* `\b` → Word boundary to ensure correct boundaries
* `re.findall()` → Returns list of tuples (day, month, year)

### ✅ Output:

```
['01/01/2020', '12/12/1999']
```

---

## ✅ 4. **Replace HTML tags from a string**

```python
import re

html = "<p>This is a <b>bold</b> move!</p>"

clean = re.sub(r"<.*?>", "", html)
print(clean)
```

### 🔍 Explanation:

* `<.*?>` → Matches **any HTML tag** (non-greedy):

  * `<` → Starts with `<`
  * `.*?` → Anything inside (non-greedy so it stops at the first `>`)
  * `>` → Ends with `>`
* `re.sub()` → Replaces all tags with an empty string (`""`)

### ✅ Output:

```
This is a bold move!
```

---

## ✅ 5. **Validate Passwords**

```python
import re

password = "Strong@123"

pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$"

if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid password")
```

### 🔍 Explanation:

* `^` → Start of string
* `(?=.*[A-Z])` → Must contain at least 1 uppercase letter
* `(?=.*\d)` → Must contain at least 1 digit
* `(?=.*[@#$%^&*!])` → Must contain at least 1 special character
* `.{8,}` → At least 8 characters in total
* `$` → End of string
* `re.fullmatch()` → Whole string must satisfy all rules

### ✅ Output:

```
Valid password
```

---

Would you like a **quiz or mini project** to test your skills now?

"""