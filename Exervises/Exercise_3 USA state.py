# Using the package for name of state of the US
import us 
# Using Mapping methon to search the item 'abbr' and 'name'
# abbr = abbreviation 
us_state_to_abbrev = us.states.mapping('abbr', 'name')

# Using upper() method to make the words UPPERCSE.
for i in us_state_to_abbrev:
  print(us_state_to_abbrev[i].upper())
  
# Using lower() method to make the words lowercase.
for i in us_state_to_abbrev:
  print(us_state_to_abbrev[i].lower())