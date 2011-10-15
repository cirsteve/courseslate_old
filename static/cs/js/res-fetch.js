function getResourceSet(opt){
    var value = opt.val();
    var tul = opt.parent().parent().next('ul');
    if ( value == "select-resource" ) {

        }
    else {
        value = value.toLowerCase().replace(" | ","/").replace(/\s/g, '-');
        var turl = site_url + "resources/get-json/resource-set/" + value + "/";
        $.ajax({
        url: turl,
        type: "GET",
        dataType: "json",
        success: function(data, responseStatus, jqXHR){
            tul.replaceWith(data.html);
        }
    });
    }
}

$('select#res-fetch').change(function(){
    var opt = $('select#res-fetch option:selected');
    getResourceSet(opt);
});