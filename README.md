# Say-What
A WebApp that detects user's confusion using Emotion Detection and provides the definition, useful links of the word heard at the instant the user seems confused.

To run this app, there will be a server side, and a client side.
Server side files are : server.py, sound_recorder.py, speech_to_text.py, tech_words.txt, nonNoun.txt.
Make sure they all are in same folder.

Now you need to run the sound_recorder.py to start recording audio which will make audio files of 5 seconds each.
Parallely we will also be running speech_to_text.py to pick those audio files and convert them to text files using 
Google Sound Recognisition API.

We can run both these python files in background, just make sure sound_recorder.py is run before speech_to_text.py. 

After this we will run server.py which will create the server to get request from client and return them the technical words 
which speaker might have spoken at that time when confusion was trigerred.

tech_words.txt and nonNoun.txt files will be used in server.py to extract only technical words from text files.

The client side filE is: client.html
To support the webapp, you need to run a server on your machine. Do this by typing the following in the terminal - "python -m SimpleHTTPServer [port]"

To get the webapp running, open your browser and enter the address : "localhost:port/PathToFile/client.html". The rest of the functionality is self-explanatory. 
NOTE: Make sure that the IP address and Port Number in the client and server files are updated accordingly.
