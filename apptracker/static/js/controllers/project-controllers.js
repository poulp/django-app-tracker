'use strict';

var trackerControllers = angular.module('trackerApp.controllers', []);

trackerControllers.controller("ProjectList", function($scope, ProjectService) {

    ProjectService.list().success(function (response) {
        $scope.projects = response;
    }).error(function (data, status, headers, config) {
        console.log("projects list failed !")
    });
});

trackerControllers.controller("ProjectNew", function($scope, $location, ProjectService) {

    $scope.add = function(project){
        ProjectService.add(project).success(function (response){
            console.log("new project added");
            $location.path('/');
        }).error(function (data, status, headers, config) {
            console.log("projects new failed !")
        });
    }
});

trackerControllers.controller("ProjectTicket", function($scope, $routeParams, ProjectService) {

    console.log($routeParams);

    ProjectService.get($routeParams.id).success(function (response){
        $scope.project = response;
    }).error(function (data, status, headers, config ){
        console.log("error get project !");
    });

});