/**
 * Created by Alex on 2016/10/5.
 */
var Topic = Vue.extend({
    template: "<div><h1>{{ topic.topic }}</h1></div>",
    data: function () {
        return {
            topic: $.ajax({
                url: "http://127.0.0.1:8001/topic/"+this.$route.params.id,
                dataType: "json",
                async: false
            }).done().responseJSON
        }
    }
});