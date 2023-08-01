#!/usr/bin/env ruby

# puts: Dislpays the searched list
# scan: searches the required characters in the search string
# school: The chararacters to search
# join: Provides a convenient join for the search string and returns the result

puts ARGV[0].scan(/School/).join
