'use strict';

trackerControllers.controller("IssueNewCtrl", function($scope, $location, $routeParams, IssueService) {

    var project_pk = $routeParams.project_pk;

    $scope.add = function(issue){
        IssueService.add(project_pk, issue).success(function (response){
            $location.path('/project/'+project_pk+'/issues')
        }).error(function (data, status, headers, config) {
            console.log("issue new failed !")
        });
    }
});

trackerControllers.controller("IssueDetailCtrl", function($scope, $routeParams, IssueService) {

    var project_pk = $routeParams.project_pk;
    var issue_pk = $routeParams.issue_pk;

    IssueService.get(project_pk, issue_pk).success(function (response){
        $scope.issue = response;
    }).error(function (data, status, headers, config) {
        console.log("issue get failed !")
    });

});