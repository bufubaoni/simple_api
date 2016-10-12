/**
 * Created by Alex on 2016/10/3.
 */
var Index = Vue.extend({
        template: "<div class='row'>" +
        "<div class='three wide column'>" + "<img>" + "</div>" +
        "<div class='ten wide column'>" +
        "<div>" +
        "<h1>{{ msg.content }}</h1>" +
        "</div>" +
        "</div>" +
        "</div>",
        data: function () {
            return {
                msg: "123"
            }
        },
        created: function () {
            this.$http.get("http://127.0.0.1:8001/").then((response)=> {
                console.log(response.data);
                this.msg = response.data;
            })
        }
    })
    ;


