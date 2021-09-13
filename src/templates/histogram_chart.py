import math

chart_template = """
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['x_tag', 'y_tag'],
          xy_values

        var options = {
          title: 'title_tag',
          legend: { position: 'none' },
        };

        var chart = new google.visualization.Histogram(document.getElementById('chart_div_tag'));
        chart.draw(data, options);
      }
    </script>
"""


def fill_chart(x_name, y_name, title, div_name, values):
    global chart_template
    chart_template = chart_template.replace("x_tag", x_name) \
        .replace("y_tag", y_name) \
        .replace("title_tag", title) \
        .replace("chart_div_tag", div_name)
    xy = ""
    for i in range(10):
        xy = xy + "['" + str(i) + "', " + str(math.sqrt(i)) + "],\n"
    xy = xy + ']);'

    chart_template = chart_template.replace("xy_values", xy)
    return chart_template


def chart():
    start = "<html><head>"
    end = '</head><body><div id="div_chart" style="width: 900px; height: 500px;"></div></body></html>'
    return start + fill_chart("x", "y", "Tytul", "div_chart", []) + end
