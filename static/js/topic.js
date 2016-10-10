/**
 * Created by Alex on 2016/10/5.
 */
var Topic = Vue.extend({
    template: "<div class='row'>" +
    "<div class='three wide column'>" + "<img>" + "</div>" +
    "<div class='ten wide column'>" +
    "<div>" +
    "<h1>{{ topic.title }}</h1>" +
    "<div class='ui divider'></div>" +
    "<p>{{topic.topic}}</p>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            topic: $.ajax({
                url: "http://127.0.0.1:8001/topic/" + this.$route.params.id,
                dataType: "json",
                async: false
            }).done().responseJSON
        }
    }
});