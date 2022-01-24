zakupy={ "piekarnia": ["chleb", "paczek", "bulki"], "warzywniak": ["marchew", "seler", "rukola"]
}
print("Lista zakupów")
for sklep, produkty in zakupy.items():
    print("Idę do,", (sklep.capitalize()), "kupuję tu następujące rzeczy:", [i.title() for i in produkty])
print("W sumie kupuję", ((sum([len(zakupy[x]) for x in zakupy if isinstance(zakupy[x], list)]))), "produktów."