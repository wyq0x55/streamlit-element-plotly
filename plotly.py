from streamlit_elements.core.frame import new_element


class Plotly:


    def __getattr__(self, element):
        return new_element("chartPlotly", element)

    def __getitem__(self, element):
        return new_element("chartPlotly", element)
