import json
import random

dogFile = 'dog_facts.json'

with open(dogFile, 'r') as f:
    dogFacts = json.loads(f.read())
    factNumber = random.randint(0, len(dogFacts)-1)

print(dogFacts[factNumber]['fact'])