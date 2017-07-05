# Groene Poort data visualisation prototype

In this prototype I used the data from the Rijkswaterstaat API for the parameters Tide and Clorosity: 
- https://waterinfo.rws.nl/api/point/latestmeasurements?parameterid=waterhoogte-t-o-v-nap 
- https://waterinfo.rws.nl/api/point/latestmeasurements?parameterIds=(massa)Concentratie___20chloride___20in___20Oppervlaktewater___20mg___2Fl

The json data comes from the API and into the own database. From that database, the data is sent to the front-end. 

For own use:
- Download code
- Install all Django packages
- Install OpanLayers
- Set-up local PostgreSQL database with PostGIS extension
- Adjust passwords
- Run!



