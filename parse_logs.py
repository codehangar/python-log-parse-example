import os
import re

line_regex = re.compile(r".*fwd=\"12.34.56.78\".*$")

output_filename = os.path.normpath("output/parsed_lines.log")
with open(output_filename, "w") as out_file:
    out_file.write("")

with open(output_filename, "a") as out_file:
    with open("test_log.log", "r") as in_file:
        for line in in_file:
            if (line_regex.search(line)):
                print line
                out_file.write(line)
