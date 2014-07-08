require.config({
	shim: {
		underscore: {
			exports: '_'
		},
		backbone: {
			deps: [
				'underscore',
				'jquery'
			],
			exports: 'Backbone'
		}
    },
	paths: {
        jquery: "libs/jquery.min",
        underscore: "libs/underscore-amd/underscore",
        backbone: "libs/backbone-amd/backbone",
        text: "libs/requirejs-text/text"
    }
});

require([
    'jquery',
    'underscore',
    'backbone',
], function ($, _, Backbone) {

});