'use strict';

trackerControllers.controller("IssueNewCtrl", function($scope, $location, $routeParams, IssueService) {

    var project_pk = $routeParams.project_pk;

    $scope.add = function(issue){
        IssueService.add(project_pk, issue).success(function (response){
            //$location.path('/project'+$routeParams.project_pk+'/issues');
            console.log("ajout ok!");
        }).error(function (data, status, headers, config) {
            console.log("issue new failed !")
        });
    }
});