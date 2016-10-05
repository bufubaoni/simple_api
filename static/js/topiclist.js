/**
 * Created by Alex on 2016/10/5.
 */
var Topiclist = Vue.extend({
    template: "<table class='ui celled table'><tbody> <tr v-for = 'item in items'><td><a href = '' > {{ item.title }}</a > </td></tr></tbody></table> ",
data: function () {
    return {
        items: $.ajax({
            url: "http://127.0.0.1:8001/topiclist",
            dataType: "json",
            async: false
        }).done().responseJSON
    }
}
});