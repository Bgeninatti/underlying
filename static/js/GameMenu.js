define([
    'jquery',
    'underscore',
    'backbone',
    'Collections/BoxCollection'
], function ($, _, Backbone, BoxList) {

	var ConfigView = Backbone.View.extend({

        collection: BoxList,

        events: {
            'click button#start': 'LoadLvl'
        },

        LoadLvl: function(e) {
            this.collection.lvl = 'simple_lvl';
            this.collection.fetch();
            offset.trigger('started');
        }
	});

	return ConfigView;
});