define([
    'jquery',
    'underscore',
    'backbone',
    'Collections/BoxCollection',
    'Game/BoxView'
], function ($, _, Backbone, BoxList, Box) {

	var GameView = Backbone.View.extend({

        collection: BoxList,

        id: 'Game',

        initialize: function() {
            this.listenTo(this.collection, 'add', this.AddOne, this);
            this.listenTo(this.collection, 'reset', this.render);
        },

        render: function() {
            this.$el.html();
            return this;
        },

        AddAll: function() {
            this.collection.each(this.AddOne, this);
        },

        AddOne: function(model) {
            var box = new Box({model: model});
            this.$el.append(box.$el);
            box.render();
        }
	});

	return GameView;
});

