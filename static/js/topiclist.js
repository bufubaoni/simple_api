/**
 * Created by Alex on 2016/10/5.
 */
var Topiclist = Vue.extend({
        template: "<p>{{items}}</p><table class='ui celled table'><tbody> <tr v-for = 'item in items'><td><router-link :to=\"{ name: 'topic', params: { id: item.id }}\"> {{ item.title }}</router-link></td></tr></tbody></table> ",
        data: function () {
            return {
                items: []
            }
        },
        created: function () {
            this.$http.get("http://127.0.0.1:8001/topiclist").then((response)=> {
                console.log(JSON.parse(response.data));
                items = JSON.parse(response.data);
            })
        }

    })
    ;