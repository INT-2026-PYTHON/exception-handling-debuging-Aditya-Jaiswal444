"""
## 3. Process User Records with Mixed Exceptions  *(Medium)*

=================================================
PROCESS USER RECORDS WITH MIXED EXCEPTIONS
=================================================

Problem Statement:
You are given a LIST of DICTIONARIES, where
each dictionary is supposed to represent a
user record:
        {"name": str, "age": str, "score": str}

The data is messy — some records are missing
keys, some have non-numeric strings, and some
are not even dictionaries.

Write a Python program that processes the
list and returns a TUPLE:
        (clean_records, error_log)

   - clean_records -> list of dicts with
                       "name": str
                       "age":  int
                       "score": float
   - error_log     -> list of tuples:
                       (index, error_class_name,
                        message)

You must demonstrate FOUR exception-handling
techniques:
   1. Catching MULTIPLE exception types in
      ONE except block.
   2. Using `except ... as e` to inspect the
      exception object.
   3. Using `raise` to re-raise an exception
      after logging.
   4. Using `else` to run code only when the
      try block succeeded.

-------------------------------------------------
Instructions:
1. Define a function:
      def process_records(records):
2. Iterate over the list with an index counter.
3. For each record, use a try / except / else
   chain:
      try:
          - access record["name"], record["age"],
            record["score"]   -> may raise
            KeyError or TypeError
          - convert age to int and score to float
            -> may raise ValueError
      except (KeyError, TypeError) as e:
          - record the error with the class name
            from type(e).__name__
      except ValueError as e:
          - record the error with the message
            str(e)
      else:
          - this branch runs ONLY when no
            exception was raised; append the
            cleaned record to clean_records.
4. Write a SECOND function:
      def process_strict(records):
   that calls process_records, and if ANY
   error occurred, RE-RAISES a RuntimeError
   that contains the number of failures.
   Use the bare `raise` keyword inside an
   except block, OR
       raise RuntimeError(...) from None
   to suppress the original traceback chain.
5. Do NOT use:
   - bare `except:`
   - custom exception classes
   - any external library
6. Call both functions and print:
   - the clean_records list
   - the error_log list
   - the message from the RuntimeError
     (catch it with try/except in the driver)

-------------------------------------------------
Debugging Skills to Practice:
- `type(e).__name__` gives the exact exception
  class as a string — useful for log messages.
- Catching multiple exception types in ONE
  except block: `except (KeyError, TypeError):`
  avoids duplicate handler code.
- The `else` block makes the success path
  visually obvious and prevents accidentally
  catching exceptions raised AFTER the risky
  operation.
- When an exception is re-raised, the original
  traceback is preserved. Read it from the
  BOTTOM up: the last line names the exception,
  the lines above show where it came from.

-------------------------------------------------
Input Example:
records = [
   {"name": "Alice", "age": "25",   "score": "88.5"},
   {"name": "Bob",   "age": "abc",  "score": "70"},
   {"name": "Carol", "age": "30"},                       # missing "score"
   "not a dict",                                          # wrong type
   {"name": "Dan",   "age": "40",   "score": "55.5"},
]

Output Example:
Clean Records:
[
  {'name': 'Alice', 'age': 25, 'score': 88.5},
  {'name': 'Dan',   'age': 40, 'score': 55.5}
]
Error Log:
[
  (1, 'ValueError', "invalid literal for int() with base 10: 'abc'"),
  (2, 'KeyError',   'score'),
  (3, 'TypeError',  'string indices must be integers')
]
Strict mode raised: RuntimeError: 3 record(s) failed to process

-------------------------------------------------
Explanation:
- Record at index 1 ("Bob") has a non-numeric
  age, so int("abc") raises ValueError.
- Record at index 2 ("Carol") is missing the
  "score" key, so record["score"] raises
  KeyError.
- Record at index 3 ("not a dict") is a plain
  string, so record["name"] raises TypeError.
- Records at indices 0 and 4 succeed, so the
  `else` block runs and they are appended to
  clean_records.
- The strict version re-raises a RuntimeError
  summarising the total number of failures.
=================================================

"""
def process_records(records):
    clean_records = []
    error_log = []
    for index, record in enumerate(records):
        try:
            name = record["name"]
            age = int(record["age"])
            score = float(record["score"])
        except (KeyError, TypeError) as e:
            error_log.append((index, type(e).__name__, str(e)))
        except ValueError as e:
            error_log.append((index, type(e).__name__, str(e)))
        else:
            clean_records.append({"name": name, "age": age, "score": score})
    return clean_records, error_log

def process_strict(records):
    clean_records, error_log = process_records(records)
    if error_log:
        raise RuntimeError(f"{len(error_log)} record(s) failed to process") from None
    return clean_records

# Driver code
if __name__ == "__main__":
    print("=== User Record Processor ===\n")
    print("Options:")
    print("1. Use default test data")
    print("2. Input custom records")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "2":
        print("\nEnter records in JSON format (one per line).")
        print("Example: {\"name\": \"Alice\", \"age\": \"25\", \"score\": \"88.5\"}")
        print("Type 'done' when finished.\n")
        
        import json
        records = []
        while True:
            user_input = input("Enter record: ").strip()
            if user_input.lower() == "done":
                break
            try:
                record = json.loads(user_input)
                records.append(record)
                print("  ✓ Record added")
            except json.JSONDecodeError:
                print("  ✗ Invalid JSON format. Please try again.")
    else:
        # Default test data
        records = [
            {"name": "Alice", "age": "25",   "score": "88.5"},
            {"name": "Bob",   "age": "abc",  "score": "70"},
            {"name": "Carol", "age": "30"},                       # missing "score"
            "not a dict",                                          # wrong type
            {"name": "Dan",   "age": "40",   "score": "55.5"},
        ]
    
    print("\n" + "="*40)
    clean_records, error_log = process_records(records)
    print("Clean Records:")
    print(clean_records)
    print("\nError Log:")
    print(error_log)
    try:
        process_strict(records)
    except RuntimeError as e:
        print(f"\nStrict mode raised: {type(e).__name__}: {str(e)}")


