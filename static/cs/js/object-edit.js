
$('a.ajax-edit').click(function(e){
    e.preventDefault();
    var ae = $(this);
    var tli = ae.parent().parent().parent('li');
    var aurl = ae.attr("href");
    var re = /\/topics\/[-\w]+\/[-\w]+\/[-\w]+\//;
    aurl = aurl.replace(re,'/topics/get-json/');
    $.ajax({
        url: aurl,
        type: "GET",
        dataType: "json",
        success: function(data, responseStatus, jqXHR){
            tli.replaceWith(data.html);
            $('form.ajax-form input[type="submit"]').live('click', function(e){
                 e.preventDefault();
                 var nform = $(this).parent('form');
                 $.ajax({
                     url: aurl,
                     type: "POST",
                     data: nform.serializeArray(),
                     dataType: "json",
                     success: function(data, responseStatus, jqXHR){
                         nform.replaceWith(data.html);
                        }
                 });
            });
        }
    });
});