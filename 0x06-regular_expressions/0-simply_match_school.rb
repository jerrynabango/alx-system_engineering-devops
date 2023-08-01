#!/usr/bin/env ruby

# puts: Dislpays the searched list
# /h, b & c: The chararacters to search
# .: The chararacters to search apart of the new line
# scan: searches the required characters in the search string
# {2,5}: Matches at least 2 and at most 5 occurrences of the previous character or group.
# join: Provides a convenient join for the search string and returns the result
puts ARGV[0].scan(/hbt{2,5}n/).join
