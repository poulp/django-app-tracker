'use strict';

var trackerApp = angular.module('trackerApp', [
    'trackerApp.controllers',
    'trackerApp.services',
    'ngRoute',
    'ui.bootstrap',
    'smart-table',
    'ngSanitize',
    'colorpicker.module'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/js/views/project/projects.html',
                controller: 'ProjectListCtrl'
            })
        /**
         * Projects
         **/
            .when('/project/new', {
                templateUrl: '/static/js/views/project/new.html',
                controller: 'ProjectNewCtrl'
            })
            .when('/project/:id/issues', {
                templateUrl: '/static/js/views/project/project-issues.html',
                controller: 'ProjectIssuesCtrl'
            })
            .when('/project/:id/settings', {
                templateUrl: '/static/js/views/project/project-settings.html',
                controller: 'ProjectSettingsCtrl'
            })
        /**
         * Issues
         **/
            .when('/project/:project_pk/issue/:issue_ref', {
                templateUrl: '/static/js/views/issue/detail.html',
                controller: 'IssueDetailCtrl'
            })
            .when('/project/:project_pk/issues/new', {
                templateUrl: '/static/js/views/project/add-issue.html',
                controller: 'IssueNewCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);

/**
 * csrf token
 **/
trackerApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);