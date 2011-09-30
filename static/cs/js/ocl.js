


jQuery('.oc').addClass('hide');

jQuery('ul.ocl li').click(function() {
    jQuery(this).children('span.oc').toggleClass('hide');
});

jQuery('ul.ocl li').click(function() {
    jQuery(this).children('div.oc').toggleClass('hide');
});

