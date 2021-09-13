import flask

from prometheus_flask_exporter import PrometheusMetrics


app = flask.Flask(__name__)
app.config["DEBUG"] = False
PrometheusMetrics(app, group_by='endpoint')


@app.route('/api/echo', methods=['POST'])
def echo():
    data = flask.request.get_json()

    # We only return the echoed item if it either doesn't currently exist
    # or is not already true.
    if 'echoed' not in data or data['echoed'] is not True:
        # Apparently it's quite hard to test whether a payload is valid JSON.
        # This seems the easiest way to address that particular case, neither
        # the is_json attribute nor checking the object type catch this issue
        # for some reason.
        try:
            data['echoed'] = True
        except TypeError:
            return('Bad request data', 400)
    # If the echoed item already exists and is true, return a 400.
    else:
        return('Bad request data', 400)

    return data


if __name__ == '__main__':
    app.run('0.0.0.0', 3000)
