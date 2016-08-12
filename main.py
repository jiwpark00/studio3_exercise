import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_titles = ['Matrix', 'Gladiator', 'Titanic','Superbad','Dumb and Dumber',
        'Jason Bourne', 'Phantom of the Opera', 'American Psycho', 'Wedding Crasher',
        'A Beautiful Mind','Spectre','Toy Story']
        # TODO: randomly choose one of the movies, and return it
        random_movie = random.choice(movie_titles)
        return random_movie

    def get(self):
        movie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tomorrow_movie = self.getRandomMovie()
        if tomorrow_movie == movie:
            tomorrow_movie = self.getRandomMovie()
        tomorrow = "<h1>Tomorrow's Movie</h1>"
        tomorrow += "<p>" + tomorrow_movie + "</p>"

        self.response.write(response)
        self.response.write(tomorrow)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
