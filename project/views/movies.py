from flask import request
from flask_restx import abort, Namespace, Resource
from project.exceptions import ItemNotFound
from project.service.movie import MoviesService
from project.setupdb import db

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self):
        """Get all movies"""
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page
        }
        try:
            return MoviesService(db.session).get_all_movies(filters)
        except ItemNotFound:
            abort(404, message="Movies not found")


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
