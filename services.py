import urllib2
import xml.etree.ElementTree as ET
import media

# This file has a function with a responsability to connect a API that i found in the internet that return a webservice in XML with information about Movies.

def downloadMovies(id_page):

	# Pass the id of page of movies to API.
	file = urllib2.urlopen('http://trailerapi.com/api/api.php?page='+id_page+'&language=en')

	# Parse XML
	data = file.read()
	file.close()
	root = ET.fromstring(data)

	# create array of movies
	array_movies = []

	# Cycle to find all Movies in XML
	for movie_info in root.findall('movie'):

		# Read title, storyline, poster and trailer of Movie
		# The trailer is housed in Daylimotion.
		# The API returns the ID of Movie (Ex:x2tyg0n) and URL to embed Video "http://www.dailymotion.com/embed/video/x2tyg0n"
		movie = media.Movie(movie_info.find('name').text.encode('utf8'),
							movie_info.find('description').text.encode('utf8'),
							movie_info.find('poster').text.encode('utf8'),
							movie_info.find('did').text.encode('utf8'))

		# Add Movie to array of Movies
		array_movies.append(movie)

	# Return array with All Movies.
	return array_movies