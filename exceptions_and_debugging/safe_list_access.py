"""
## 2. Safe List Access  *(Easy)*

=================================================
SAFE LIST ACCESS
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_get`
that takes a list and an index, and returns
the value at that index WITHOUT crashing the
program when the index is invalid.

The function must return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the value on success,
                         or an error string on
                         failure.

Handle these error cases:
   - IndexError      -> "Index out of range"
   - TypeError       -> "Index must be an int"
   - other Exception -> "Unexpected error: ..."

-------------------------------------------------
Instructions:
1. Define a function:
      def safe_get(items, index):
2. Use a try block that returns items[index].
3. Add a separate `except` block for each
   expected exception in the correct order
   (most specific first).
4. Add a final `except Exception as e:` block
   that includes str(e) in the error message.
5. Do NOT use:
   - the `in` operator to guess validity
     beforehand
   - if-checks like `if 0 <= index < len(items)`
     to AVOID the exception.
   The whole point is to LET the exception be
   raised and HANDLE it.

-------------------------------------------------
Debugging Skills to Practice:
- Use print(repr(index), type(index)) when the
  function misbehaves; `repr` shows quotes
  around strings so you can tell "3" from 3.
- Read the exception MESSAGE — IndexError on a
  list of length 5 tells you the index that
  was rejected.
- Try `import traceback; traceback.print_exc()`
  inside the except block to print the full
  traceback while still handling the error.

-------------------------------------------------
Input Example 1:
safe_get([10, 20, 30, 40], 2)

Output Example 1:
('ok', 30)

-------------------------------------------------
Input Example 2:
safe_get([10, 20, 30], 7)

Output Example 2:
('error', 'Index out of range')

-------------------------------------------------
Input Example 3:
safe_get([10, 20, 30], "1")

Output Example 3:
('error', 'Index must be an int')

=================================================

"""
def safe_get(items, index):
    try:
        return ("ok", items[index])
    except IndexError:
        return ("error", "Index out of range")
    except TypeError:
        return ("error", "Index must be an int")
    except Exception as e:
        return ("error", f"Unexpected error: {str(e)}")
    
if __name__ == "__main__":
    print("=== Safe List Access ===\n")
    print("Options:")
    print("1. Run test cases")
    print("2. Input custom list and index")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "2":
        # Custom input
        print("\nEnter a list of integers separated by commas.")
        print("Example: 10, 20, 30, 40")
        list_input = input("Enter list: ").strip()
        
        try:
            items = [int(x.strip()) for x in list_input.split(",")]
            print(f"  ✓ List created: {items}")
        except ValueError:
            print("  ✗ Invalid input. Please enter integers separated by commas.")
            exit()
        
        print("\nEnter an index (can be an integer, string, float, etc.)")
        index_input = input("Enter index: ").strip()
        
        # Try to convert to int, but also test other types
        try:
            index = int(index_input)
        except ValueError:
            # Keep as string or try other conversions
            if index_input.replace(".", "", 1).isdigit():
                index = float(index_input)
            else:
                index = index_input  # Keep as string
        
        print(f"  Testing with index: {repr(index)} (type: {type(index).__name__})")
        result = safe_get(items, index)
        print(f"\nResult: {result}")
    else:
        # Test cases
        print("\nRunning test cases...\n")
        test_cases = [
            ([10, 20, 30, 40], 2, "('ok', 30)"),
            ([10, 20, 30], 7, "('error', 'Index out of range')"),
            ([10, 20, 30], "1", "('error', 'Index must be an int')"),
            (None, 0, "('error', 'Unexpected error: ...')"),
            ([10, 20, 30], -1, "('ok', 30)"),
            ([10, 20, 30], 1.5, "('error', 'Index must be an int')"),
            ([10, 20, 30], 0, "('ok', 10)"),
            ([10, 20, 30], 3, "('error', 'Index out of range')"),
        ]
        
        for items, index, expected in test_cases:
            result = safe_get(items, index)
            status = "✓" if expected in str(result) else "✗"
            print(f"{status} safe_get({items}, {repr(index)}) = {result}")

    
