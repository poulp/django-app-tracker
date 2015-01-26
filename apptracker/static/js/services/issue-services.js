services.factory('IssueService', function($http) {

    return {
        get: function(project_pk, issue_pk){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/'+project_pk+'/issues/'+issue_pk
            })
        },
        add: function(project_id, data){
            return $http({
                method: 'POST',
                data: data,
                url: '/tracker/api/project/' + project_id + '/issues'
            })
        }
    };
});