
$(document).ready(function(){
	
	
	 //Header Search
    if($('.search-box-outer').length) {
        $('.search-box-outer').on('click', function() {
            $('body').addClass('search-active');
        });
        $('.close-search').on('click', function() {
            $('body').removeClass('search-active');
        });
    }
	// Mobile Menu
    $('.mobile-menu nav').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu",
        onePage: false,
    });
	  // to wow Jquery
		new WOW().init();
	// sticky
    var wind = $(window);
    var sticky = $('#sticky-header');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });

	$('.testimonial-slide').owlCarousel({
		loop:true,
		margin:0,
		autoplay:true,
		nav:true,
		items:4,
		dots: true,
		responsive:{
			0:{
				items:1
			},
			600:{
				items:1
			},
			768:{
				items:2
			},
			992:{
				items:2
			},
			 1920:{
				items:2
			}
		}
	});
	
	$('.blog-slide').owlCarousel({
		loop:true,
		margin:0,
		autoplay: true,
		nav:true,
		items:3,
		dots: false,
		responsive:{
			0:{
				items:1
			},
			600:{
				items:1
			},
			 768:{
				items:2
			},
			992:{
				items:3
			},
			1000:{
				items:3
			},
			1920:{
				items:3
			}
		}
	});
	
	$('.brand-slide').owlCarousel({
		loop:true,
		margin:0,
		autoplay: true,
		nav:true,
		items:3,
		dots: false,
		responsive:{
			0:{
				items:1
			},
			320:{
				items:1
			},
			600:{
				items:2
			},
			 768:{
				items:3
			},
			992:{
				items:4
			},
			1200:{
				items:5
			},
			1500:{
				items:5
			},
			
			1920:{
				items:5
			}
		}
	});
	
	
	$('.accordion > li:eq(0) a').addClass('active').next().slideDown();

		$('.accordion a').click(function(j) {
			var dropDown = $(this).closest('li').find('p');

			$(this).closest('.accordion').find('p').not(dropDown).slideUp();

			if ($(this).hasClass('active')) {
				$(this).removeClass('active');
			} else {
				$(this).closest('.accordion').find('a.active').removeClass('active');
				$(this).addClass('active');
			}

			dropDown.stop(false, true).slideToggle();

			j.preventDefault();
	});
	
    /*---- scrollUp----- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
 // Calender Jquery
        var curDate = (new Date()).getDate();
        var curMonth = (new Date()).getMonth();
        var curYear = (new Date()).getFullYear();
        var startDay = (new Date(curYear, curMonth, 1)).getDay();
        var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        var noofdays = ["31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"];
        var prevMonth = noofdays[curMonth - 1];
        if (curMonth == 11) {
        prevMonth = noofdays[0]
        } else if (curMonth == 0) {
        prevMonth = noofdays[11]
        };
        var totalDays = noofdays[curMonth];
        var counter = 0;
        var precounter = prevMonth - (startDay - 1);
        var rightbox = 6;
        var flag = true;

        jQuery('.curr-month b').text(months[curMonth]);
        for (var i = 0; i < 42; i++) {
        if (i >= startDay) {
        counter++;
        if (counter > totalDays) {
        counter = 1;
        flag = false;
        }
        if (flag == true) {
        jQuery('.all-date ul').append('<li class="monthdate">' + counter + '</li>');
        } else {
        jQuery('.all-date ul').append('<li style="opacity:.8">' + counter + '</li>');
        }
        } else {
        jQuery('.all-date ul').append('<li style="opacity:.8">' + precounter + '</li>');
        precounter++;
        }

        if (i == rightbox) {
        jQuery(jQuery('.all-date ul li')[rightbox]).addClass("b-right");
        rightbox = rightbox + 7;
        }

        if (i > 34) {
        jQuery(jQuery('.all-date ul li')[i]).addClass("b-bottom");
        }

        if ((jQuery(jQuery('.all-date ul li')[i]).text() == curDate) && (jQuery(jQuery('.all-date ul li')[i]).css('opacity') == 1)) {
        jQuery(jQuery('.all-date ul li')[i]).css({
        "background-color": "#533EFF",
        "color": "rgb(255, 255, 255)"
        });
        }
        };

	// Loder  //
	$(function () {
	 $('body').addClass('loaded');
	});

});
