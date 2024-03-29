html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.select("title"))

print(soup.select("p:nth-of-type(3)"))

print(soup.select("body a"))

print(soup.select("html head title"))

print(soup.select("head > title"))

print(soup.select("p > a"))

print(soup.select("p > a:nth-of-type(2)"))

print(soup.select("p > #link1")) # #은 id

print(soup.select("body > a"))

print(soup.select(".sister")) # .은 class

print(soup.select("#link1, #link2"))

print(soup.select('a[href]'))