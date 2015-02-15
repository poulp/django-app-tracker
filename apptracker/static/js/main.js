$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

/**
 * globals
 */
var MOBILE_VIEW = 992;
$(function() {
    'use strict';
    function getWidth() {
        return window.innerWidth;
    }

    var App = {
        /**
         * init
         */
        init: function () {
            this.cacheElements();
            this.bindEvents();
            this.checkViewport();
        },
        /**
         * cache elements
         */
        cacheElements: function () {
            this.$viewport = $(window);
            this.$pageWrapper = $("#page-wrapper");
            this.$toggleBtn = $("#toggle-sidebar");
        },
        /**
         * bind events to elements
         */
        bindEvents: function () {
            this.$viewport.on('resize', this.viewportResize.bind(this));
            this.$toggleBtn.on('click', this.toggleSidebar.bind(this));
        },
        /**
         * trigger checkviewport on resize
         */
        viewportResize: function () {
            this.checkViewport();
        },
        /**
         * toggles sidebar
         */
        toggleSidebar: function (e) {
            this.$pageWrapper.toggleClass('active');
            $.cookie('toggle', this.$pageWrapper.hasClass("active"));
        },
        /**
         * Checks the viewport and toggles sidebar if toggled
         */
        checkViewport: function () {

            if (getWidth() >= MOBILE_VIEW) {

                if ($.cookie('toggle') === undefined) {

                    this.$pageWrapper.addClass("active");
                } else {
                    if ($.cookie('toggle') == 'true') {
                        this.$pageWrapper.addClass("active");
                    } else {
                        this.$pageWrapper.removeClass("active");
                    }
                }
            } else {
                this.$pageWrapper.removeClass("active");
            }
        }
    };
    App.init();
});