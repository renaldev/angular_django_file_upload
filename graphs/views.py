from django.http import JsonResponse
from django.views.generic import CreateView, DetailView
from .models import GraphData


class GraphDataCreateView(CreateView):

    model = GraphData
    fields = ['file']


class GraphDataView(DetailView):

    model = GraphData
    with_file_contents = False

    def get_context_data(self, **kwargs):
        context = {}
        context["file"] = self.object.file.name

        if self.with_file_contents:
            """
            This block of code should be moved
            to a another module for validation
            Exel-file. But here it was made
            for simplicity.
            """
            try:
                from xlrd import open_workbook
                s = open_workbook(self.object.file.path).sheet_by_index(0)
                data = []
                for row in range(s.nrows):
                    values = []
                    for col in range(s.ncols):
                        values.append(s.cell(row,col).value)
                    data.append(values)
                    context["data"] = data
            except:
                context["data"] = []

        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)