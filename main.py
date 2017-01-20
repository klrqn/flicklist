import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie title
        movies = ["Castle in the Sky", "Princess Mononoke", "Spirited Away", "Your Name", "Ghost in the Shell", "Battle Royale", "The Big Lebowski"]

        # TODO: randomly choose one of the movies, and return it
        movie1 = random.choice(movies)
        return movie1

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it underneath
        anotherMovie = self.getRandomMovie()
        while anotherMovie == movie:
            anotherMovie = self.getRandomMovie()

        content += "<h1>Tommorrow's Movie</h1>"
        content += "<p>" + anotherMovie + "</p>"

        content += "random text"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
