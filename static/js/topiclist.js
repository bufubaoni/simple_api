/**
 * Created by Alex on 2016/10/5.
 */
var Topiclist = Vue.extend({
        template: "<table class='ui celled table'><tbody> <tr v-for = 'item in items'><td><router-link :to=\"{ name: 'topic', params: { id: item.id }}\"> {{ item.title }}</router-link></td></tr></tbody></table> ",
        data: function () {
            return {
                items: this.$http.get("http://127.0.0.1:8001/topiclist").then((response)=> {
                    console.log(response.body);
                    times = response.body;
                })
            }
        },

    })
    ;