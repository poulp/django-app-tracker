'use strict';

var trackerApp = angular.module('trackerApp', ['trackerApp.controllers', 'trackerApp.services', 'ngRoute'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/js/views/project/projects.html',
                controller: 'ProjectList'
            })
            .when('/project/new', {
                templateUrl: '/static/js/views/project/new.html',
                controller: 'ProjectNew'
            })
            .when('/project/:id/ticket', {
                templateUrl: '/static/js/views/project/ticket-list.html',
                controller: 'ProjectTicket'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);

trackerApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);