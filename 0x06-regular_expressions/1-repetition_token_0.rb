#!/usr/bin/env ruby

# puts: Dislpays the searched list
# /h, b & t: The chararacters to search
# .: Search all the matching characters apart from newline characters
# scan: searches the required characters in the search string
# {2,5}: Matches at least 2 and at most 5 occurrences of the previous character(t).
# join: Provides convenient join for the search string and returns the result

puts ARGV[0].scan(/hbt{2,5}n/).join
