/**
 * Created by Alex on 2016/10/19.
 */
var Login = Vue.extend({
    template: "<div class='row'>" +
    "<div class='three wide column'>" + "<img>" + "</div>" +
    "<div class='ten wide column'>" +
    "<div>" +
    "<h1>{{ topic }}</h1>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            topic: "1233333"
        }
    }
});