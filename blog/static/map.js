$('.part').click (
	function() {
		$('.description').html($(this).attr('description-data'));
		$('.description').fadeIn();
	}
)