$(document).ready(function() {
    $("#save-settings").click(function () {
        console.log("working");
        let ideal_temp = $("#temp").val();
        let ideal_humidity = $("#humidity").val();
        let daily_water = $("#water").val();
        let daily_light = $("#light").val();

        $.ajax({
            "url": "ajax/save_outputs/",
            "data": {
                "unit_id": "10101010101101",
                "daily_water": daily_water,
                "daily_light": daily_light,
                "ideal_humidity": ideal_humidity,
                "ideal_temp": ideal_temp
            },
            "dataType": "json"
        });
    });
});