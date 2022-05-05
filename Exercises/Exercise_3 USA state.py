# use the package for name of state of the US
import us 
# use Mapping methon to search the item 'abbr' and 'name'
# abbr = abbreviation 
us_state_to_abbrev = us.states.mapping('abbr', 'name')

# use upper() method to make the words UPPERCSE and list it.
state_name_UP = [us_state_to_abbrev[i].upper() for i in us_state_to_abbrev]
  
# use lower() method to make the words lowercase and list it.
state_name_low = [us_state_to_abbrev[i].lower() for i in us_state_to_abbrev]

# list abbreviation
state_name_abbr = [i.upper() for i in us_state_to_abbrev]

# import pandas as pd
import pandas as pd

# call DataFrame constructor on list
# abbreviation + uppercase + lowercase Dataframe
df = pd.DataFrame(list(zip(state_name_abbr, state_name_UP,state_name_low)), index = list(range(1,len(state_name_UP) + 1)), columns =['abbreviation','UPPERCASE NAMES','lowercase names'])

# --------------------- Input Code is above this line.-----------------------------------
# --------------------- Output Code is below this line.-----------------------------------

# write DataFrame to CSV File with Default params.
df.to_csv('usa.csv', encoding='utf-8')
