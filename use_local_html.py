from bs4 import BeautifulSoup

# open the html doc in read mode and save it as file f
with open('index.html', 'r') as f:
    # save the file f as doc, and parse it as an HTML document
    document = BeautifulSoup(f, 'html.parser')

# print(doc.prettify())

# find things by tag name - this shows first item with this tag
title_tag = document.title
print(title_tag)
print(title_tag.string)
# modify the tag string in the document:
title_tag.string = "This is the New Title"
print(title_tag)

print('\n')
print('\n')

p_tag = document.find('p')
print(p_tag)

print('\n')
print('\n')

# print all p tags, added to a list, with everything inside them
all_p_tags = document.find_all('p')
print(all_p_tags)

print('\n')
print('\n')

# access the nested tags inside the list of p tags, and save them as a list
# here we access all the b tags
first_p_tag = all_p_tags[0]
all_b_tags_in_first_p = first_p_tag.find_all('b')
print(all_b_tags_in_first_p)
