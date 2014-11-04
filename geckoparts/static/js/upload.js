/**
 * Created by Clive on 10/10/2014.
 */
$(document).ready(function() {

$("p").click(function() {
    //take id from element
    var $level_name = $(this).attr('id');
    var $level_array = $level_name.split(".");
    $level_name = $level_array.pop();
    //test if element below is open
    var $is_open = $("[id^=" + $level_name + "]").is(":visible");
    //if it is open, close child elements and their child elements
    if ($is_open) {
    close_item($("[id^=" + $level_name + "]"));

    }
    else {
    $("[id^=" + $level_name + "]").show();

    }

    });
function close_item(element) {
    //close child elements first
    var $level_name = $(element).attr('id');
    var $level_array = $level_name.split(".");
    $level_name = $level_array.pop();
    if ($("[id^=" + $level_name + "]").length >0){
        close_item($("[id^=" + $level_name + "]"))
    }
    //close_item($("[id^=" + $level_name + "]"));
    //once child elements are closed, close this element
    $(element).hide();
}



});