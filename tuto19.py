#dictionary = a changeable, unordered collection of unique key:value pairs
#fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'Russia':'Moscow',
            'China':'Beijing'}

print(capitals['Russia'])

print(capitals.get('Germany'))

print(capitals.keys())

print(capitals.values())

print(capitals.items())

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})

for key,value in capitals.items():
    print(key,value)

capitals.pop('China')
capitals.clear()
