


jQuery('.oc').addClass('hide');



jQuery('ul.ocl li').click(function() {
    jQuery(this).children('div.oc').slideToggle(200);
});

$('.expand-trigger').click(function() {
    var trigger = $(this)
    var value = trigger.val()
    if (value === "Expand All") {
            trigger.parent('div').find('ul.ocl').children('li').each( function () {
                $(this).children('div.oc').slideDown(250);
                });
            trigger.attr("value", "Collapse All");
    }
    else {
            trigger.parent('div').find('ul.ocl').children('li').each( function () {
                $(this).children('div.oc').slideUp(100);
                });
            trigger.attr("value", "Expand All");
    }
});
