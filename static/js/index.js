/**
 * Created by Alex on 2016/10/3.
 */
var Index = Vue.extend({
    template: "<div><h1>{{ msg.title }}</h1><p>{{ msg.content }}</p></div>",
    data: function () {
        return {
            msg: $.ajax({
                url: "http://127.0.0.1:8001",
                dataType: "json",
                async: false
            }).done().responseJSON
        }
    }
});


