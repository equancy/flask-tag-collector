import io
import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route('/equancy', methods=['GET'])
def tag():
    try:
        if request.args:
            with io.open('media/equancy_tag.log', 'a') as f:
                f.write(u"date:{1};{0}\n".format(";".join(["{0}:{1}".format(key, value) for key, value in request.args.items()]), datetime.datetime.now()))
        return 'OK'
    except Exception, e:
        return 'KO'


@app.route('/equancy/read/<page>', methods=['GET'])
@app.route('/equancy/read', methods=['GET'])
def tag_read(page=30):
    try:
        with io.open('media/equancy_tag.log', 'r') as f:
            lines = f.readlines()
        return "<br/>".join(lines[-int(page)::])
    except Exception, e:
        raise
        return 'KO'


if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')
    app.run()
