define([
    'jquery',
    'underscore',
    'backbone',
    'text!Game/BoxTemplate.html',
    'Collections/BoxCollection'
], function ($, _, Backbone, BoxTemplate, BoxList) {

	var BoxView = Backbone.View.extend({

        template: _.template(BoxTemplate),

        className: 'box',

        events: {
            'click': 'Permutation',
            contextmenu: 'Inverse'
        },

        initialize: function() {
            this.listenTo(this.model, 'change', this.render);
            permutations.on('Permut:'+this.model.get('id'), this.Update, this);
        },

        render: function() {
            this.$el.addClass(this.model.get('class'));
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },
        Permutation: function() {
            var val = this.model.get('val');
            if( this.model.get('val') != "U") {
                this.model.set('val', val+1);
                var target = BoxList.get(this.model.get('target')),
                    target_nval = eval(this.model.get('operation').replace('{target}', target.get('val')));
                target.set('val', target_nval);
                permutations.trigger('checkGoal');
            }
        },
        Update: function(val) {
            this.model.set('value', val);
        },
        Inverse: function(e) {
            e.preventDefault();
            var val = this.model.get('val');
            if( this.model.get('val') != "U") {
                this.model.set('val', val-1);
                var target = BoxList.get(this.model.get('target')),
                    target_nval = eval(this.model.get('inverse').replace('{target}', target.get('val')));
                target.set('val', target_nval);
                permutations.trigger('checkGoal');
            }
        }
	});

	return BoxView;
});