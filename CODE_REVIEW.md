# Code Review

## Initial Review of the Starter Script

1. **Unclear function and variable names.** Names such as `do_math_stuff`, `list_of_nums`, and `result` do not clearly describe the function's purpose or the data. Descriptive names reduce the effort needed to understand the code.
2. **Missing function documentation.** The function does not explain its purpose, input parameter, or return value. A docstring helps another developer use the function correctly.
3. **Manual list construction.** The original loop creates an empty list and appends each calculated value. For a simple transformation, a list comprehension can express the operation more concisely.
4. **Limited explanation of the calculation.** A brief comment can clarify the transformation when it is not immediately obvious from context.

## Final Review

1. **Naming:** Replaced generic names with `process_numbers`, `process_strings`, `numbers`, `words`, `processed_numbers`, and `processed_strings`. These names better communicate each item's role.
2. **Documentation:** Added a module docstring and function docstrings describing purpose, parameters, and return values.
3. **Refactoring:** Used list comprehensions to make each transformation concise. The string transformation explicitly identifies the words that should be uppercase.
4. **Comments:** Added a targeted comment explaining why the numeric transformation is expressed as a single comprehension.
5. **Verification:** Ran `python undocumented_script.py` and confirmed that it produced the expected output:

```text
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```

The program runs without syntax or runtime errors. The names, documentation, and compact transformations make the program easier to review and maintain.
