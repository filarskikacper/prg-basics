translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

while True:
    word = input("Enter word to translate: ")
    if word in translations:
        print(translations[word])