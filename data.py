import os
import services


# This file has the responsability of construct the HTML of page to send to Client.


# This is a string with a syntax in HTML for each Movie.
movieHTML = '''
<div class="col-xs-12 col-sm-6 col-md-4">
	<center>
		<div class="movie" data-trailer-dailymotion-id="{movie_trailer}">
			<div class="moviePosterContent">
				<div class="moviePoster">
					<img class="movieImage" src="{movie_poster}" onerror="this.src='error_cover.png'">
				</div>
			</div>
			<div class="movieTitle">{movie_title}</div>
			<div class="movieDescription">{movie_description}</div>
		</div>
	</center>
</div>
'''


# This function has a responsability of construct the HTML to each movie with the string above.
def create_movie_tiles_content(movies):
	
	content = ''

	for movie in movies:

		content += movieHTML.format(
			movie_title=movie.title,
			movie_description=movie.storyline,
			movie_poster=movie.poster_image_url,
			movie_trailer=movie.movie_trailer_url
		)
		
	return content


# This function returns only the HTML to each Movie
def get_movies_HTMl(id_page):

	# Call the API service with respective id of page movies
	movies = services.downloadMovies(id_page)
	return create_movie_tiles_content(movies)


# This function returns all of content of Page to send to client.
def open_movies_page():

	# Read and past to data the template file.
	indexFile = open(r'index.html')
	data = indexFile.read()
	indexFile.close()

	# Increase to the template all Movies of page 1 of API
	data2 = data.format(movies_html=get_movies_HTMl("1"))

	# Return Full page to Client
	return data2