import os 
import pprint 
  
# Get the list of user's 
env_var = os.environ 
  
# Print the list of user's 
print("User's Environment variable:") 
pprint.pprint(dict(env_var)) 
print('--------------------------------')
pprint.pprint(env_var['APPDATA']) 