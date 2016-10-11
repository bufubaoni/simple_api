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
    "<div v-html='topic.topic'></div>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            topic: "1233333"
        }
    },
    created: function () {
        this.$http.get("http://127.0.0.1:8001/topic/" + this.$route.params.id).then((response)=> {
            console.log(response.data);
            this.topic = response.data;
        })
    }
});