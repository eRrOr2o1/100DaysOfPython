from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name) --> title
# print(soup.title.string) --> Angela's Personal Site
# print(soup.prettify()) --> It will prettify the code

all_anchor_tags = soup.find_all(name="a")  # Used to find the all the specified tag
# print(all_anchor_tags)

# It will print the text in all the anchor tags
# for tag in all_anchor_tags:
    # print(tag.getText())
    # get is used to get the links from href attribute
    # print(tag.get("href"))

# To find a particular tag using id
# heading = soup.find(name="h1", id="name")
# print(heading)

# To find a particular tag using id
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# To select a tag within a tag
# comapny_url = soup.select_one(selector="p a")  # Here p is paragraph and a is anchor tag
# print(comapny_url)

# To select a tag within a tag using id

# name = soup.select_one(selector="#name")
# print(name)

# To select a tag within a tag using class
headings = soup.select(".heading")
print(headings)