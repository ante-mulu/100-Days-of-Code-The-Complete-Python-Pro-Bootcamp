# Python Primitive Data Types

Python has four primary primitive data types: **String**, **Integer**, **Float**, and **Boolean**. Understanding these types is crucial as they form the foundation for handling data in Python.

## 1. String
A **string** is a sequence of characters, such as words or sentences. Strings are written within quotation marks (`" "` or `' '`).

### a. Subscripting
Subscripting is a way to access specific characters in a string by using their index positions.

- **Example:** `print("subscripting"[0])`  
  - Output: `s` (the first character of "subscripting")
  - **Note:** In Python, indexing starts at `0`, so `"subscripting"[0]` refers to the first character.

- **Negative Indexing:** Use a negative index to access characters from the end of the string.
  - **Example:** `print("Hello"[-1])`  
    - Output: `o` (the last character of "Hello")
  - **Note:** `[-1]` means "start from the end." This can be helpful for reversing strings or accessing the last elements.

### b. String Concatenation
When numbers are written inside quotation marks, they are treated as strings and can be joined, or **concatenated**.

- **Example:** `print("12" + "345")`  
  - Output: `12345` (combines "12" and "345" without adding them numerically)
  - **Note:** Concatenation joins strings without spaces. Use `+` to combine them.

## 2. Integer
An **integer** is a whole number without any decimal point. In Python, integers are written as they are without quotes.

- **Example:** `print(1000)`  
  - Output: `1000`

- **Using Underscores for Readability:** Large integers can be separated by underscores (`_`) to improve readability.
  - **Example:** `1_000_000` (is the same as 1000000 in Python)
  - **Note:** Underscores are ignored by Python and do not affect the value.

## 3. Float
A **float** is a number with a decimal point, often used for more precise values, like measurements.

- **Example:** `print(3.14159)`  
  - Output: `3.14159`
  - **Note:** Floats are useful for representing fractional values or precise measurements.

## 4. Boolean
A **Boolean** is a data type with only two possible values: `True` or `False`.

- **Example:**  
  ```python
  is_active = True
  is_logged_in = False
  print(is_active)  # Output: True
