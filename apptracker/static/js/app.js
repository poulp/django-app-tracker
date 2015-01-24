'use strict';

var trackerApp = angular.module('trackerApp', ['trackerApp.controllers', 'trackerApp.services', 'ngRoute'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/js/views/projects.html',
                controller: 'ProjectHome'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);