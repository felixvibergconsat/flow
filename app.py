import dash

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
        __name__,
        meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
        )

#app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True

