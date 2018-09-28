import connexion

items = {
    0: {'name': 'First item'}
}

def get_items() -> list:
    return items

app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='gevent')
