define([
    'jquery',
    'underscore',
    'backbone',
    'Collections/BoxCollection'
], function ($, _, Backbone, BoxList) {

	var ConfigView = Backbone.View.extend({

        collection: BoxList,

        events: {
            'click button': 'LoadLvl'
        },

        LoadLvl: function(e) {
            e.preventDefault();
            var lvl = this.$el.find('input').val();

            this.collection.lvl = lvl;
            this.collection.fetch();
        }
	});

	return ConfigView;
});

