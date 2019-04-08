from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .generated.VuetifyWidget import VuetifyWidget


class Html(VuetifyWidget):

    _model_name = Unicode('HtmlModel').tag(sync=True)

    tag = Unicode().tag(sync=True)

    attributes = Dict(None, allow_none=True).tag(sync=True)

__all__ = ['Html']