'''names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
Unpack the first five countries and store them in a variable nordic_countries, 
store Estonia and Russia in es, and ru respectively.'''


names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

try:
    nordic_countries = names[:5]

    try:                # Try to store Estonia and Russia in variables es and ru
        es, ru = names[5], names[6]
        print("Nordic Countries:", nordic_countries)
        print("Estonia:", es)
        print("Russia:", ru)
    except IndexError:
        print("Error: Not enough elements in the list to unpack Estonia and Russia.")
except Exception as e:
    print(f"An error occurred: {e}")




