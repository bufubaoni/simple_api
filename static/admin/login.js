/**
 * Created by Alex on 2016/10/19.
 */
var Login = Vue.extend({
    template: "<div class='row'>" +
    "<div class='three wide column'>" + "<img>" + "</div>" +
    "<div class='ten wide column'>" +
    "<div>" +
    "<div class='ui segment'>" +
    "<h2>{{ loginmsg }}</h2>" +
    "<div class='ui divider'></div>" +
    "<form class='ui form'>" +
    "<div class='field'>" +
    "<label>User name: {{ username }}</label>" +
    "<input name='username' placeholder='User name' type='text' v-model='username'>" +
    "</div>" +
    "<div class='field'>" +
    "<label>PassWord</label>" +
    "<input name='PassWord' placeholder='PassWord' type='text' v-model='password'>" +
    "</div>" +
    "<a class='ui blue button' v-on:click='login'>Submit</a>" +
    "</form>" +
    "</div>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            loginmsg: "Login",
            username: "666",
            password: "****"
        }
    },
    methods: {
        login: function () {
            
        }
    }
});