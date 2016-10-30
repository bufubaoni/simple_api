/**
 * Created by Alex on 2016/10/30.
 */
var Adduser = Vue.extend({
    template: "<div class='row'>" +
    "<div class='three wide column'>" + "<img>" + "</div>" +
    "<div class='ten wide column'>" +
    "<div>" +
    "<div class='ui segment'>" +
    "<h2>{{ loginmsg }}</h2>" +
    "<div class='ui divider'></div>" +
    "<form class='ui form'>" +
    "<div class='field'>" +
    "<label>User name:</label>" +
    "<input name='username' placeholder='User name' type='text' v-model='username'>" +
    "</div>" +
    "<div class='field'>" +
    "<label>PassWord</label>" +
    "<input name='PassWord' placeholder='PassWord' type='text' v-model='password'>" +
    "</div>" +
    "<a class='ui blue button' v-on:click='adduser'>Submit</a>" +
    "</form>" +
    "</div>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            loginmsg: "Add User",
            username: "",
            password: ""
        }
    },
    methods: {
        adduser () {
            this.$http.post("http://127.0.0.1:8001/adduser", {
                username: this.$data.username,
                passwd: this.$data.password,
                time:new Date()
            }).then((response)=> {
                    console.log(response.body.msg);
                }
            )
        }
    }
});