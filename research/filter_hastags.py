
tags="Hey guys! #stackoverflow really #rocks #rocks #announcement"
print {tag.strip("#") for tag in tags.split() if tag.startswith("#")}