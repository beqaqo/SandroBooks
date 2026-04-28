from flask_restx import Resource, fields, reqparse
from src.ext import api
from src.models.project import Project

project_model = api.model('Project', {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "link": fields.String,
    "image": fields.String,
})

parser = reqparse.RequestParser()
parser.add_argument('lang', required=False, type=str, choices=['ka', 'en', 'it'], default='ka')


def serialize_project(p, lang='ka'):
    return {
        "id": p.id,
        "title": p.get_title(lang),
        "description": p.get_description(lang),
        "link": p.link,
        "image": p.image,
    }


@api.route("/projects")
class ProjectsApi(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        lang = args["lang"] or 'ka'
        projects = Project.query.all()
        return [serialize_project(p, lang) for p in projects]


@api.route("/project/<int:id>")
class ProjectApi(Resource):
    @api.expect(parser)
    def get(self, id):
        args = parser.parse_args()
        lang = args["lang"] or 'ka'
        project = Project.query.get_or_404(id)
        return serialize_project(project, lang)