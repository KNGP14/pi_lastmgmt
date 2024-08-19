# pi_lastmgmt
Lastmanagement mi Raspberry Pi 2B

- Wenn 10s lang <=-1000 dann GPIO auf True für 300s
- Wenn er nach 300s weiterhin <=-50, dann weiterhin GPIO auf True
- Wenn nach 300s für weitere 300s >-10, dann GPIO Nr 10 auf False
- alles als Argument übergeben

- Wenn Timeout dann Email
- muss nur von 7-21 laufen, 21 Uhr beim beenden dann GIO auf False

- Visualisierung:
   - in file schreiben bei GPIO-Ansteerung: Zeitstempel + GPIO-Zustand (0/1)
   - in file schreiben bei GPIO-Ansteuerug: Zeitstempel + Wert P ("Gesamtleistung in W")
   - https://www.chartjs.org/docs/latest/samples/line/multi-axis.html
   - config v1 siehe unten
   - config v2: verbraucher nicht in 0-100% sondern in Watt darstellen
   - config v2.1: alle verbraucherin Watt als Stacked Bar übereinander, um die Gesamt-Verbraucher darzustellen https://www.chartjs.org/docs/latest/samples/bar/stacked.html
   - oder extra skript, dass jede minute P von LUPUS abfrage und Verbraucher-Verbrauch und schreibt weg, damit reale Werte

LUPUS json:
` { "json_values": [ { "id": "P", "value": "-25" }, ... ] } `

LUPUS-Demoumgebung
cmd: `python3 -m http.server`

Web: http://localhost:8000/values-mock.json

## Visualsierung
config
```
const config = {
  type: 'line',
  data: data,
  options: {
    responsive: true,
    interaction: {
      mode: 'index',
      intersect: false,
    },
    stacked: false,
    plugins: {
      title: {
        display: true,
        text: 'Chart.js Line Chart - Multi Axis'
      }
    },
    scales: {
      y: {
        type: 'linear',
        display: true,
        position: 'left',
        min: -200,
        max: 200
      },
      y1: {
        type: 'linear',
        display: true,
        position: 'right',
        min: -25000,
        max: 25000,

        // grid line settings
        grid: {
          drawOnChartArea: false, // only want the grid lines for one axis to show up
        },
      },
    }
  },
};
```

Setup
```
const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: -24150, max: 24150};

const labels = ['17:16 Uhr', '17:17 Uhr', '17:18 Uhr', '17:19 Uhr', '17:20 Uhr', '17:21 Uhr', '17:22 Uhr'];
const data = {
  labels: labels,
  datasets: [
    {
      label: 'Verbraucher 1',
      data: [0,0,100,0,100,100,0],
      borderColor: Utils.CHART_COLORS.red,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
      yAxisID: 'y',
      stepped: true,
    },
    {
      label: 'Gesamtleistung',
      data: Utils.numbers(NUMBER_CFG),
      borderColor: Utils.CHART_COLORS.blue,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
      yAxisID: 'y1',
    }
  ]
};
```
