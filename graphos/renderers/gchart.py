from .base import BaseChart

from django.template.loader import render_to_string


class LineChart(BaseChart):
    def get_template(self):
        return "graphos/gchart/line_chart.html"

    def as_html(self):
        context = {"data": self.get_data(), "chart": self}
        return render_to_string(self.get_template(), context)