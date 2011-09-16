


jQuery('.oc').addClass('nidden');

jQuery('ul.ocl li').click(function() {
    jQuery(this).children('span.oc').toggleClass('nidden');
});

