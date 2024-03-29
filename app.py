from flask import Flask

from routes import init_api_routes
from routes import init_website_routes
from routes import init_error_handlers


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret'

init_api_routes(app)
init_website_routes(app)
init_error_handlers(app)


@app.template_filter('senior_candidate')
def senior_candidate(candidates):
    result = []
    for candidate in candidates:
        for experience in candidate['experience']:
            if experience['years'] >= 5:
                result.append({
                    'first_name':candidate['first_name'],
                    'last_name':candidate['last_name'],
                    'years':experience['years'],
                    'domain':experience['domain']
                })
                break

    return result


@app.template_filter('all_candidates')
def all_candidates(candidates):
    result = []
    for candidate in candidates:
        for experience in candidate['experience']:
            result.append({
                'first_name': candidate['first_name'],
                'last_name': candidate['last_name'],
                'years': experience['years'],
                'domain': experience['domain']
            })
    return result


if __name__ == "__main__":
    app.run(debug=True)
