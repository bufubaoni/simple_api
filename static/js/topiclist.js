/**
 * Created by Alex on 2016/10/5.
 */
var Topiclist = Vue.extend({
        template: "<div class='row'>" +
        "<div class='three wide column'>" + "<img>" + "</div>" +
        "<div class='ten wide column'>" +
        "<table class='ui celled table'><tbody> " +
        "<tr v-for = 'item in items'>" +
        "<td><router-link :to=\"{ name: 'topic', params: { id: item.id }}\"> {{ item.title }}</router-link></td>" +
        "</tr></tbody></table>" +
        "</div> </div>>",
        data: function () {
            return {
                items: "12333"
            }
        },
        created: function () {
            this.$http.get("http://127.0.0.1:8001/topiclist").then((response)=> {
                console.log(response.data);
                this.items = response.data;
            })
        }

    })
    ;