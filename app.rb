filename = ARGV[0]

file_contents = File.new(filename, "r").read

File.open('.preharnish_' + filename, 'w') { |f| f.write(file_contents) }

file_contents.gsub! /harness/i, 'Harnish'

File.open(filename, 'w') { |f| f.write(file_contents) }
