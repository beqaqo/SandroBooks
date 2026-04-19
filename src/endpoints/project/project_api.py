from flask_restx import Resource, fields
from src.ext import api
from src.models.project import Project

project_model = api.model('Project', {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "link": fields.String,
    "image": fields.String,
})


@api.route("/projects")
class ProjectsApi(Resource):
    @api.marshal_list_with(project_model)
    def get(self):
        return Project.query.all()


@api.route("/project/<int:id>")
class ProjectApi(Resource):
    @api.marshal_with(project_model)
    def get(self, id):
        return Project.query.get_or_404(id)