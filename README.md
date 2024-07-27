# pi_lastmgmt
Lastmanagement mi Raspberry Pi 2B

- Wenn 10s lang <=-1000 dann GPIO auf True für 300s
- Wenn er nach 300s weiterhin <=-50, dann weiterhin GPIO auf True
- Wenn nach 300s für weitere 300s >-10, dann GPIO Nr 10 auf False
- alles als Argument übergeben

- Wenn Timeout dann Email
- muss nur von 7-21 laufen, 21 Uhr beim beenden dann GIO auf False

LUPUS json:
` { "json_values": [ { "id": "P", "value": "-5" }, ... ] } `
