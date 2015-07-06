// JavaScript file

$(document).ready(function(){

	// When page is Ready add the events to show movie trailers
	add_Events_Trailer();


	// Add Event to Load More Movies
	$('#moreMovies').on('click',function(){

		// Inform the user request
		$('#moreMoviesContent').html('Loading...');

		// Read page id from the button clicked
		var pageMovie = $(this).attr('pageMovie');

		var URL = window.location.protocol + '//' + window.location.host;


		// POST Request to load more Movies
		$.ajax({
	        url: URL,
	        type: "POST",
	        data: {"id_page":pageMovie},
	        success: function(data, textStatus, jqXHR) {


	        	// If POST request has success
				var htmlObject = document.createElement('div');
				htmlObject.innerHTML = data;



				//The API returns often repeated films and so this code is a filter to not be repeated in films DOM.

	        	var divs = htmlObject.getElementsByClassName('col-xs-12 col-sm-6 col-md-4');
	        	for (var i = 0; i < divs.length; i += 1) {
					var divMovie = divs[i].getElementsByClassName('movieTitle');
					var titleMovie = divMovie[0].innerText;


					var movieExist = 0;

					var atualDiv = document.getElementById('contentMovies');
					var atualDivs = atualDiv.getElementsByClassName('col-xs-12 col-sm-6 col-md-4');
					for (var j = 0; j < atualDivs.length; j += 1) {

						var atualdivMovie = atualDivs[j].getElementsByClassName('movieTitle');
						var atualtitleMovie = atualdivMovie[0].innerText;

						if(atualtitleMovie == titleMovie)
						{
							movieExist = 1;
						}
					}


					// IF Dom dont have the movie, add movie
					if (movieExist == 0)
					{
						$('.row').append(divs[i]);
					}
				}


				// Replace the Button
				$('#moreMoviesContent').html('More Movies');

				// Add new page ID to button
				$('#moreMovies').attr({'pageMovie':parseInt(pageMovie) + 1});

				// Re-add the events to show movie trailers
				add_Events_Trailer();

	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	            $('#moreMoviesContent').html('More Movies');
	        }
	    });
	});

	// Hide Trailer
	$('.trailer').on('click',function(){
		$('.videoFrame').empty();
		$('.trailer').hide();
	});
});


function add_Events_Trailer() {
	$('.movie').unbind('click');
	$('.movie').on('click',function(){
		// Read trailer id
		var url = $(this).attr('data-trailer-dailymotion-id');

		//Show trailer
		$('.trailer').show();
		var sourceUrl = "http://www.dailymotion.com/embed/video/"+url;
		
		$('.videoFrame').html('<iframe class="iframe" src="'+sourceUrl+'"></iframe>');
	});
}