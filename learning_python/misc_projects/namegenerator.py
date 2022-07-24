import random
verbs = ['leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Lean-in', '30,000 foot']
adjectives = ['Freenium', 'Hyperlocal', 'Siloed', 'Cloud-based', 'API based', 'A/B Tested']
nouns = ['Albert Guo' , 'Kevin Kang', 'Alex Jiang', 'Pipeline', 'Tipping point', 'Paradigm']
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun
print(phrase) 
