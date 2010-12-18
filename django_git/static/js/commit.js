$(function(){
    $('.blob-link').bind('click', function(){
        var item = $(this).attr("id").replace("bl", "");
        var file_name = $("#f" + item).html();

        // Turn off other elements
        $('.diff').hide();
        $('.blob').hide();

        $.ajax({
           method: "GET",
           url: "blob/",
           data: "file=" + file_name,
           success: function(data){
               $("#b" + item).html(data);
               $("#b" + item).toggle();
           }
        })
    });

    $('.diff-link').bind('click', function(){
        var item = $(this).attr("id").replace("dl", "")

        // Turn off other elements
        $('.diff').hide();
        $('.blob').hide();

        $('#d' + item).show();
    });
});