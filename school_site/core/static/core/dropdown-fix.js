jQuery(function($) {
	  if ($(window).width() > 769) {
	    $('.navbar .dropdown').hover(function() {
	      $(this).find('.dropdown-menu').first().stop(true, true).delay(250).slideDown();

	    }, function() {
	      $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideUp();

	    });

	    $('.navbar .dropdown > a').click(function() {
	      location.href = this.href;
	    });

	  }
	  /*if ($(window).width() < 769) {
		$('.nav-link > span').click(function() {
		  $('.navbar > li').removeClass("dropdown");
		  $('.navbar .dropdown > a').removeAttr('data-toggle');
	  	}
	  }*/
	});

jQuery('.dropdown-icon-fix').on('click', function (e) {
  $(this).next().toggle();
});
/*jQuery('.dropdown-menu.keep-open').on('click', function (e) {
  e.stopPropagation();
});*/

/*if(1) {
  $('body').attr('tabindex', '0');
}
else {
  alertify.confirm().set({'reverseButtons': true});
  alertify.prompt().set({'reverseButtons': true});
}*/
