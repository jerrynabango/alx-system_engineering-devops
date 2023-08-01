#!/usr/bin/env ruby

# puts: Dislpays the searched list
# .: Search all the matching characters apart from newline characters
# scan: searches the required characters in the search string
# []: Represents a character class, matching any one of the characters inside the brackets.
#\: An escape character that matches any character in the search string
# *: Matches zero or more occurrences of the previous character.
# * ?: Matches zero or one occurrence of the previous character.
# join: Provides a convenient join for the search string and returns the result

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
