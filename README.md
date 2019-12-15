# devx-ops
Python 3.6 is required. Also the requests and IPy libraries.
Search in hetrixtools database. In script check_hetrixtools.py we pass the arguments api key and through the spaces any number of IP or URLs we want to check. We will use the api key and enter it as a password string from Jenkins through the pipeline.
In script check_url_abuse.py protos we pass URLs arguments which we want to check through a space.

EXEMPLE
#python3 check_hetrixtools.py API_key ukr.net 80.11.158.65 carlosmartins.ca
ukr.net is listed on 0 out of 72 checked blacklists in hetrix!
80.11.158.65 is listed on 9 out of 71 checked blacklists in hetrix!
carlosmartins.ca is listed on 1 out of 70 checked blacklists in hetrix!

#python3 check_url_abuse.py ukr.net 80.11.158.65 carlosmartins.ca
In urlhouse this ukr.net was not found
In urlhouse this 80.11.158.65 was not found
carlosmartins.ca found in 1 blacklists URLhouse!
