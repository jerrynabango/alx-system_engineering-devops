#!/usr/bin/env ruby

# puts: Dislpays the searched list
# /h, b & t: The chararacters to search
# .: Search all the matching characters apart from newline characters
# scan: searches the required characters in the search string
# ?: matches zero or one occurrence of the previous character(b).
# join: Provides convenient join for the search string and returns the result

puts ARGV[0].scan(/hb?tn/).join
