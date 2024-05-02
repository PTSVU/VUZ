# # E101 - indentation contains mixed spaces and tabs
# def mixed_spaces_and_tabs():
#     a = 1
#     b = 2  # This line contains a mix of spaces and tabs
#
# # E111 - indentation is not a multiple of four
# def indentation_not_multiple_of_four():
#     a = 1  # Incorrect indentation, not a multiple of four
#
# # E112 - expected an indented block
# def expected_indented_block():
#     if True:  # No indented block following the if statement
#     print("Indented block expected")
#
# # E121 - continuation line under-indented for hanging indent
# def continuation_line_under_indented():
#     a = [
#         1,
#         b  # Continuation line is under-indented for hanging indent
#     ]
#
# # E201 - whitespace after '('
# def whitespace_after_parenthesis():
#     func( 1)  # Whitespace after '('
#
# # E202 - whitespace before ')'
# def whitespace_before_parenthesis():
#     func(1 )  # Whitespace before ')'
#
# # E203 - whitespace before ',', ';', or ':'
# def whitespace_before_comma():
#     a = 1 , b = 2  # Whitespace before ',' and '='
#
# # E211 - whitespace before '('
# def whitespace_before_parenthesis():
#     func (1)  # Whitespace before '('
#
# # E221 - multiple spaces before operator
# def multiple_spaces_before_operator():
#     result  = 1  + 2  # Multiple spaces before operator
#
# # E222 - multiple spaces after operator
# def multiple_spaces_after_operator():
#     result = 1   + 2   # Multiple spaces after operator
#
# # E223 - tab before operator
# def tab_before_operator():
#     result = 1   + 2   # Tab before operator
#
# # E224 - tab after operator
# def tab_after_operator():
#     result = 1 +   2  # Tab after operator
#
# # E225 - missing whitespace around operator
# def missing_whitespace_around_operator():
#     result = 1+2  # Missing whitespace around operator
#
# # E226 - missing whitespace around arithmetic operator
# def missing_whitespace_around_arithmetic_operator():
#     result = 1+2  # Missing whitespace around arithmetic operator
#
# # E227 - missing whitespace around bitwise or shift operator
# def missing_whitespace_around_bitwise_operator():
#     result = 1|2  # Missing whitespace around bitwise operator
#
# # E228 - missing whitespace around modulo operator
# def missing_whitespace_around_modulo_operator():
#     result = 1%2  # Missing whitespace around modulo operator
#
# # E231 - missing whitespace after ',', ';', or ':'
# def missing_whitespace_after_comma():
#     a = 1, b = 2  # Missing whitespace after ','
#
# # E241 - multiple spaces after ','
# def multiple_spaces_after_comma():
#     a = 1  , b = 2  # Multiple spaces after ','
#
# # E242 - tab after ','
# def tab_after_comma():
#     a = 1   , b = 2  # Tab after ','
#
# # E251 - unexpected spaces around keyword / parameter equals
# def unexpected_spaces_around_equals():
#     func( a = 1 )  # Unexpected spaces around '='
#
# # E261 - at least two spaces before inline comment
# def spaces_before_inline_comment():
#     result = 1  #  Inline comment should have at least two spaces before it
#
# # E262 - inline comment should start with '# '
# def inline_comment_without_space():
#     result = 1  #Inline comment should start with '# '
#
# # E265 - block comment should start with '# '
# def block_comment_without_space():
#     """
#     Block comment should start with '# '
#     """
#     result = 1
#
# # E266 - too many leading '#' for block comment
# def too_many_leading_hashes():
#     """
#     ### Too many leading '#' for block comment
#     """
#     result = 1
#
# # E271 - multiple spaces after keyword
# def multiple_spaces_after_keyword():
#     if  True:  # Multiple spaces after keyword 'if'
#
# # E272 - multiple spaces before keyword
# def multiple_spaces_before_keyword():
#     if   True:  # Multiple spaces before keyword 'if'
#
# # E273 - tab after keyword
# def tab_after_keyword():
#     if	True:  # Tab after keyword 'if'
#
# # E274 - tab before keyword
# def tab_before_keyword():
#     if True:  # Tab before keyword 'if'
#
# # E275 - missing whitespace after keyword
# def missing_whitespace_after_keyword():
#     ifTrue:  # Missing whitespace after keyword 'if'
#
# # E301 - expected 1 blank line, found 0
# def expected_one_blank_line():
#     a = 1
#     b = 2  # Expected 1 blank line, found 0
#
# # E302 - expected 2 blank lines, found 0
# def expected_two_blank_lines():
#     a = 1
#     b = 2  # Expected 2 blank lines, found 0
#
# # E303 - too many blank lines (3)
# def too_many_blank_lines():
#     a = 1
#
#
#     b = 2  # Too many blank lines (3)
#
# # E304 - blank lines found after function decorator
# @decorator
#
# def function_with_blank_lines():
#     a = 1  # Blank lines found after function decorator
#
# # E305 - expected 2 blank lines after end of function or class
# class ClassWithBlankLines:
#
#     def method_with_blank_lines(self):
#         a = 1
#
#     b = 2  # Expected 2 blank lines after end of class
#
# # E306 - expected 1 blank line before a nested definition
# def function_with_nested_definition():
#     a = 1
#
#     def nested_function():
#         b = 2  # Expected 1 blank line before a nested definition
#
# # E401 - multiple imports on one line
# import module1, module2  # Multiple imports on one line
#
# # E402 - module level import not at top of file
# def function_with_import():
#     import module  # Module level import not at top of file
#     a = 1
#
# # E501 - line too long (82 > 79 characters)
# def long_line():
#     result = "This is a very long line that exceeds the maximum length allowed by PEP 8, which is 79 characters."
#
# # E502 - the backslash is redundant between brackets
# def redundant_backslash():
#     result = [1, \
#               2]  # The backslash is redundant between brackets
#
# # E701 - multiple statements on one line (colon)
# def multiple_statements_on_one_line():
#     a = 1; b = 2  # Multiple statements on one line (colon)
#
# # E702 - multiple statements on one line (semicolon)
# def multiple_statements_on_one_line_semicolon():
#     a = 1; b = 2  # Multiple statements on one line (semicolon)
#
# # E703 - statement ends with a semicolon
# def statement_ends_with_semicolon():
#     a = 1;  # Statement ends with a semicolon
#
# # E704 - multiple statements on one line (def)
# def multiple_statements_on_one_line_def(): a = 1; b = 2  # Multiple statements on one line (def)
#
# # E711 - comparison to None should be 'if cond is None:'
# def comparison_to_None():
#     if a == None:  # Comparison to None should be 'if cond is None:'
#         pass
#
# # E712 - comparison to True should be 'if cond is True:' or 'if cond:'
# def comparison_to_True():
#     if a == True:  # Comparison to True should be 'if cond is True:' or 'if cond:'
#         pass
#
# # E713 - test for membership should be 'not in'
# def test_for_membership():
#     if a not in b:  # Test for membership should be 'not in'
#         pass
#
# # E714 - test for object identity should be 'is not'
# def test_for_object_identity():
#     if a != b:  # Test for object identity should be 'is not'
#         pass
#
# # E721 - do not compare types, use 'isinstance()'
# def do_not_compare_types():
#     if type(a) == int:  # Do not compare types, use 'isinstance()'
#         pass
#
# # E722 - do not use bare except, specify exception instead
# def do_not_use_bare_except():
#     try:
#         a = 1 / 0
#     except:  # Do not use bare except, specify exception instead
#         pass
#
# # E731 - do not assign a lambda expression, use a def
# f = lambda x: x * 2  # Do not assign a lambda expression, use a def
#
# # E741 - do not use variables named 'l', 'O', or 'I'
# l = 1  # Do not use variables named 'l', 'O', or 'I'
#
# # E742 - do not define classes named 'l', 'O', or 'I'
# class l:  # Do not define classes named 'l', 'O', or 'I'
#     pass
#
# # E743 - do not define functions named 'l', 'O', or 'I'
# def l():  # Do not define functions named 'l', 'O', or 'I'
#     pass
#
# # W191 - indentation contains tabs
# def indentation_with_tabs():
#     a = 1
#     b = 2  # Indentation contains tabs
#
# # W291 - trailing whitespace
# def trailing_whitespace():
#     a = 1   # Trailing whitespace
#
# # W292 - no newline at end of file
# def no_newline_at_end_of_file():
#     a = 1  # No newline at end of file
#
# # W293 - blank line contains whitespace
# def blank_line_contains_whitespace():
#
#     a = 1
#     # There is whitespace on this line
#
# # W391 - blank line at end of file
# def blank_line_at_end_of_file():
#     a = 1
#
# # There is a blank line after this function, which is at the end of the file
#
# # W503 - line break before binary operator
# def line_break_before_binary_operator():
#     result = 1 \
#              + 2  # Line break before binary operator
#
# # W504 - line break after binary operator
# def line_break_after_binary_operator():
#     result = 1
#     + 2  # Line break after binary operator
#
# # W505 - doc line too long (82 > 79 characters)
# def doc_line_too_long():
#     """
#     This is a very long docstring line that exceeds the maximum length allowed by PEP 8, which is 79 characters.
#     """
#
# # W605 - invalid escape sequence 'x'
# def invalid_escape_sequence():
#     path = "C:\Users\ptsvu\Documents"  # Invalid escape sequence 'x'