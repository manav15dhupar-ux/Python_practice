# name=input("Eneter your name:")
# date=input("Eneter today's date:")

# letter=f"""Dear {name},
# You are selected!
# {date}"""
# print(letter)

#or


letter=f"""Dear <|Name|>,
You are selected!
<|Date>|"""

print(letter.replace("<|Name|>","manav"))
print(letter.replace("<|Date>|","24 october 2025"))


#or

letter=f"""Dear <|Name|>,
You are selected!
<|Date>|"""

print(letter.replace("<|Name|>","manav").replace("<|Date>|","24 october 2025"))
