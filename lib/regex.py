import re

my_pattern = r"[A-Z]\w\'?\w+\s\w+\'?\w\s\w+\'?\w?\w?\s\w+\s\w+\,?\s\w+\W"
my_regex = re.compile(my_pattern)

