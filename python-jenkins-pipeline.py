"""Have Jenkins request image to deploy as user input, and store the input in a variable
Then pass the variable to Python script that deploys the image from the passed variable
User input should be choices in a list, rather than values user has to be enter
Variable has to be passed from Jenkins to Python and back (using Jenkins env variables? that Python will access with os.getenv()?)
"""


import os

choice = os.getenv("DEPLOY_ENV")

print(f"Running python script, your environment is {choice}")