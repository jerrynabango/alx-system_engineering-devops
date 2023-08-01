#!/usr/bin/env ruby

# puts: Dislpays the searched list
# .: Search all the matching characters apart from newline characters
# scan: searches the required characters in the search string
# *: Matches zero or more occurrences of the previous character(t).
# join: Provides convenient join for the search string and returns the result

puts ARGV[0].scan(/hbt*n/).join
