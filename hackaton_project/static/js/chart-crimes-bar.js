// Bar Chart Example
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
var ctx = document.getElementById("totalesChart");
console.log(ctx)
var data = ctx.getAttribute("data-data")

datos = JSON.parse(data);

var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    datasets: [{
      label: "Crímenes",
      backgroundColor: "rgba(90,34,139,1)",
      borderColor:  "rgba(90,34,139,1)",
      data: datos
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'actividad'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
