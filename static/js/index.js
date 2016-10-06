/**
 * Created by Alex on 2016/10/3.
 */
var Index = Vue.extend({
        template: "<div><h1>{{ msg.title }}</h1><p>{{ msg.content }}</p></div>",
        data: function () {
            return {
                msg: "123"
            }
        },
        created: function () {
            this.$http.get("http://127.0.0.1:8001/").then((response)=> {
                console.log(response.data);
                this.msg = response.data;
                // this.$nextTick(function () {
                //     this.msg = response.data;
                // })
            })
        }
    })
    ;


