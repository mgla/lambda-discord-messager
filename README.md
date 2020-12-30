# lambda-discord-messager
Sends a single message to a single discord channel once, then disconnects.
* To be deployed as a lambda function with an up to date python environment.
* Use venv directory and name it 'venv'

Needs some environment variables to work:

* CHANNEL_ID discord channel id, get using Discord developer mode
* USER_TOKEN your user token. Please note that this token can be used to to everything with your account. Also, using this to automate messages probably violates Discords terms and services. I did not check
* MESSAGE: The message you want to send to the channel above.


This is just a proof-of-concept to have stuff like this running in lambda. Better not use it as a best practice
