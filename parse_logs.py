import os
import re

# Regex used to match relevant loglines (in this case, a specific IP address)
line_regex = re.compile(r".*fwd=\"12.34.56.78\".*$")

# Output file, where the matched loglines will be copied to
output_filename = os.path.normpath("output/parsed_lines.log")
# Overwrites the file, ensure we're starting out with a blank file
with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    with open("test_log.log", "r") as in_file:
        # Loop over each log line
        for line in in_file:
            # If log line matches our regex, print to console, and output file
            if (line_regex.search(line)):
                print line
                out_file.write(line)
