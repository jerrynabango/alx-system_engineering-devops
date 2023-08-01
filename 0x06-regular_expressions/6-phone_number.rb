#!/usr/bin/env ruby

# puts: Dislpays the searched list
# .: Search all the matching characters apart from newline characters
# scan: searches the required characters in the search string
# ^: Matches the start of a line(h).
# \d: Matches any digit character. It is equivalent to [0-9].
# {}: Matches exactly 10 occurrences of the previous character or group.
# $: Matches the end of a line.
# join: Provides convenient join for the search string and returns the result

puts ARGV[0].scan(/^(\d{10})$/).join
