define([
    'jquery',
	'underscore',
    'backbone',
    'Models/Box'
], function ($, _, Backbone, Box) {

    var BoxList = Backbone.Collection.extend({

        model: Box,

        urlRoot: '/game',

        url: function() {
            var lvl = this.lvl,
                url = this.urlRoot + ( lvl != undefined ? '/' + lvl : '' );
            return url
        }
    });

    return new BoxList();

});