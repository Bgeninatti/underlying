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

            permutations.on('checkGoal', this.CheckGoal, this);
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
        },
        CheckGoal: function() {
            var ok = 0;
            this.collection.each(function(box){
                if (box.get('id') == box.get('val')) {
                    ok += 1;
                }
            });
            if (ok == 16) {
                offset.trigger('winer')
            }
        }
	});

	return GameView;
});

