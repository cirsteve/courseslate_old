
jQuery('.oc').addClass('hide');

jQuery('div.content ul.ocl li').click(function() {
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

function applyFull(e) {
    var checkbox = e
    if (checkbox.is(':checked')){
        $('div.content div.content-list').addClass('hide');
        checkbox.parents('div.content-list').removeClass('half hide').addClass('full').fadeIn('slow');
    }
    else {
        checkbox.parents('div.content-list').removeClass('full').addClass('half');
        $('div.content div.content-list').removeClass('hide').fadeIn(400);
    }
}

function fullList() {
    $('span.view-input input[type="checkbox"]').click(function(){
        applyFull($(this));
    });
}



$(function () {
    fullList();
});

$('select.list-sort').change(function(){
    var list = $(this).next('ul.ocl');
    var items = list.children('li');
    var opt = $(this).find('option:selected').val();
    switch (opt) {
    case 'def':
        break;
    case 'Newest':
        items.tsort('span.created',{order:'desc'});
        break;
    case 'Oldest':
        items.tsort('span.created',{order:'asc'});
        break;
    case 'AZ':
        items.tsort('h5',{order:'asc'});
        break;
    case 'ZA':
        items.tsort('h5',{order:'desc'});
        break;
    }
});

jQuery('input[type="button"]').removeClass('hide');


$(function() {
    $('span.view-input input[type="checkbox"]').removeClass('hide').each(function () {
        var a = $(this).next('a');
        var str = '<p>' + a.text() + '</p>';
        a.replaceWith(str);
    });
});
