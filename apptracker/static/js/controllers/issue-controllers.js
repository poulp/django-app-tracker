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

trackerControllers.controller("IssueDetailCtrl", function($scope, $location, $routeParams, IssueService) {

    var project_pk = $routeParams.project_pk;
    var issue_ref = $routeParams.issue_ref;

    $scope.editorTitleEnabled = false;

    IssueService.get(project_pk, issue_ref).success(function (response){
        $scope.issue = response;
    }).error(function (data, status, headers, config) {
        console.log("issue get failed !")
    });

    /* show title editor */
    $scope.enableEditorTitle = function(){
        $scope.editorTitleEnabled = true;
    };

    /* save new title */
    $scope.saveEditTitle = function(){
        $scope.editorTitleEnabled = false;
    };

    $scope.remove = function(){
        IssueService.remove(project_pk, issue_ref).success(function (response){
            $location.path('/project/'+project_pk+'/issues');
        }).error(function (data, status, headers, config){
            console.log("issue not deleted !");
        });
    };

});