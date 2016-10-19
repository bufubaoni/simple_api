/**
 * Created by Alex on 2016/10/19.
 */
var Login = Vue.extend({
    template: "<div class='row'>" +
    "<div class='three wide column'>" + "<img>" + "</div>" +
    "<div class='ten wide column'>" +
    "<div>" +
    "<div class='ui segment'>" +
    "<h2>{{ login }}</h2>" +
    "<div class='ui divider'></div>" +
    "<form class='ui form'>" +
    "<div class='field'>" +
    "<label>User name</label>" +
    "<input name='username' placeholder='User name' type='text'>" +
    "</div>" +
    "<div class='field'>" +
    "<label>PassWord</label>" +
    "<input name='PassWord' placeholder='PassWord' type='text'>" +
    "</div>" +
    "<button class='ui blue button' type='submit'>Submit</button>" +
    "</form>" +
    "</div>" +
    "</div>" +
    "</div>" +
    "</div>",
    data: function () {
        return {
            login: "Login"
        }
    }
});