##  https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

## https://regexr.com

import re

pattern = r"[A-Z]+anley"
text = '''
Stanley Green (1915–1993) was a sandwich man who became a well-known figure in London during the latter part of the 20th century. For 25 years Green patrolled Oxford Street, carrying a placard that advocated "Less Lust, By Less Protein: Meat Fish Bird; Egg Cheese; Peas Beans; Nuts. And Sitting", with the wording and punctuation changing over the years. Arguing that protein made people lustful and aggressive, his solution was "protein wisdom", a low-protein diet for "better, kinder, happier people". For a few pence, passers-by could buy his 14-page pamphlet, Eight Passion Proteins with Care, which reportedly sold 87,000 copies over 20 years. He became one of London's much-loved eccentrics, though his campaign was not invariably popular, leading to two arrests for obstruction and the need to wear green overalls to protect himself from spit. When he died at the age of 78, his pamphlets, placards, and letters were passed to the Museum of London.
'''
match = re.search(pattern, text)          # will stop after one search
print(match)
# matches = re.finditer(pattern, text)
# for match in matches :
#     print(text[match.span()[0]:match.span()[1]])
#     print(match.span())
