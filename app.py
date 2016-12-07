from chalice import Chalice

app = Chalice(app_name='gochefit-webhooks')


@app.route('/build/master', methods=['GET'], api_key_required=True)
def build_master():
    return {'hello': 'master'}


@app.route('/build/prod', methods=['GET'], api_key_required=True)
def build_prod():
    return {'hello': 'prod'}
