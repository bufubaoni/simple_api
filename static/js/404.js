/**
 * Created by Alex on 2016/10/11.
 */
var NotFound = Vue.extend({
    template: "<div class='row'>" +
    "<div class='three wide column'>" + "<img>" + "</div>" +
    "<div class='ten wide column'>" +
    "<div>" +
    "<h1>{{ msg }}</h1>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            msg: "Not Found"
        }

    }
});