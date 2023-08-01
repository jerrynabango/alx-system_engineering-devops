#!/usr/bin/env ruby

# puts: Dislpays the searched list
# .: Search all the matching characters apart from newline characters
# scan: searches the required characters in the search string
# school: The chararacters to search
# join: Provides a convenient join for the search string and returns the result

puts ARGV[0].scan(/School/).join
