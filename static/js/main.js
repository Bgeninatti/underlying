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
    'Game/GameView',
    'GameMenu',
    'Collections/BoxCollection'
], function ($, _, Backbone, GameView, GameMenu, BoxList) {

    document.ondblclick = function(evt) {
        if (window.getSelection)
            window.getSelection().removeAllRanges();
        else if (document.selection)
            document.selection.empty();
    }

    var _tripleClickTimer = 0;
    var _mouseDown = false;

    document.onmousedown = function() {
        _mouseDown = true;
    };

    document.onmouseup = function() {
        _mouseDown = false;
    };

    document.ondblclick = function DoubleClick(evt) {
        ClearSelection();
        window.clearTimeout(_tripleClickTimer);

        //handle triple click selecting whole paragraph
        document.onclick = function() {
            ClearSelection();
        };

        _tripleClickTimer = window.setTimeout(RemoveDocumentClick, 1000);
    };

    function RemoveDocumentClick() {
        if (!_mouseDown) {
            document.onclick = null;
            return true;
        }

        _tripleClickTimer = window.setTimeout(RemoveDocumentClick, 1000);
        return false;
    };

    function ClearSelection() {
        if (window.getSelection)
            window.getSelection().removeAllRanges();
        else if (document.selection)
            document.selection.empty();
    };

    permutations = {};
    _.extend(permutations, Backbone.Events);

    offset = {}
    _.extend(offset, Backbone.Events);

    game = new GameView();
    $('div.game-cont').append(game.$el);
    game.render();

    menu = new GameMenu({
        el: $('#game-menu')
    });

    offset.on('started', function(){
        $('#game-offset').fadeOut();
    });

    offset.on('stoped', function(){
        $('#game-offset').fadeIn();
    });

    BoxList.fetch();


});