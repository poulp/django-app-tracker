services.factory('IssueService', function($http) {

    return {
        add: function(project_id, data){
            return $http({
                method: 'POST',
                data: data,
                url: '/tracker/api/project/' + project_id + '/issues'
            })
        }
    };
});