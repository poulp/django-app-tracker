'use strict';

var trackerControllers = angular.module('trackerApp.controllers', []);

trackerControllers.controller("ProjectListCtrl", function($scope, ProjectService) {

    ProjectService.list().success(function (response) {
        $scope.projects = response;
    }).error(function (data, status, headers, config) {
        console.log("projects list failed !")
    });
});

trackerControllers.controller("ProjectNewCtrl", function($scope, $location, ProjectService) {

    $scope.add = function(project){
        ProjectService.add(project).success(function (response){
            $location.path('/');
        }).error(function (data, status, headers, config) {
            console.log("projects new failed !")
        });
    }
});

trackerControllers.controller("ProjectIssuesCtrl", function($scope, $routeParams, ProjectService) {

    ProjectService.getIssues($routeParams.id).success(function (response){
        $scope.project = response;
    }).error(function (data, status, headers, config ){
        console.log("error get project !");
    });

});

trackerControllers.controller("ProjectSettingsCtrl", function($scope, $routeParams, ProjectService) {

    ProjectService.getLabels($routeParams.id).success(function (response){
        $scope.labels = response;
    }).error(function (data, status, headers, config ){
        console.log("error get labels !");
    });

    /* add a new label */
    $scope.addNewLabel = function(label){
       ProjectService.addLabel($routeParams.id, label).success(function (response){
            $scope.labels = response;
            $scope.label = null;
        }).error(function (data, status, headers, config){
            console.log("error !!!");
        })
    };

});