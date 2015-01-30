services.factory('IssueService', function($http) {

    return {
        get: function(project_pk, issue_reference){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/'+project_pk+'/issues/' + issue_reference
            })
        },
        add: function(project_pk, data){
            return $http({
                method: 'POST',
                data: data,
                url: '/tracker/api/project/' + project_pk + '/issues'
            })
        },
        patch: function(project_pk, issue_reference, data){
            return $http({
                method: 'PATCH',
                data: data,
                url: '/tracker/api/project/' + project_pk + '/issues/' + issue_reference
            })
        },
        remove: function(project_pk, issue_reference){
            return $http({
                method: 'DELETE',
                url: '/tracker/api/project/' + project_pk + '/issues/' + issue_reference
            })
        }
    };
});