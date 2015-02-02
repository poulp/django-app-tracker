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
    $scope.editorDescriptionEnabled = false;

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
        IssueService.patch(project_pk, issue_ref, {"title": $scope.issue.title}).success(function (response){
            $scope.editorTitleEnabled = false;
        }).error(function (data, status, headers, config){
            console.log("something was wrong !");
        });
    };

    /* show description editor */
    $scope.enableEditorDescription = function(){
        console.log("lol");
        $scope.editorDescriptionEnabled = true;
    };

    /* hide description editor */
    $scope.disableEditorDescription = function(){
        $scope.editorDescriptionEnabled = false;
    };

    /* save new description */
    $scope.saveEditDescription = function(){
        IssueService.patch(project_pk, issue_ref, {"description": $scope.issue.description}).success(function (response){
            $scope.disableEditorDescription();
            console.log(response);
            $scope.issue.description_html = response.description_html;
        }).error(function (data, status, headers, config){
            console.log("something was wrong !");
        });
    };

    /* delete issue */
    $scope.remove = function(){
        IssueService.remove(project_pk, issue_ref).success(function (response){
            $location.path('/project/'+project_pk+'/issues');
        }).error(function (data, status, headers, config){
            console.log("issue not deleted !");
        });
    };

    /* close issue */
    $scope.close = function(){
        IssueService.patch(project_pk, issue_ref, {"is_closed": "True"}).success(function (response){
            console.log("issue closed !");
            $scope.issue.is_closed = true;
        }).error(function (data, status, headers, config){
            console.log("issue not closed !");
        });
    };

    /* open issue */
    $scope.open = function(){
        IssueService.patch(project_pk, issue_ref, {"is_closed": "False"}).success(function (response){
            console.log("issue opened !");
            $scope.issue.is_closed = false;
        }).error(function (data, status, headers, config){
            console.log("issue not opened !");
        });
    }

});