var services = angular.module('trackerApp.services', []);

services.factory('ProjectService', function($http) {

    return {
        list: function(){
            return $http({
                method: 'GET',
                url: '/tracker/api/project?format=json'
            });
        },
        get: function(project_id){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/' + project_id + '?format=json'
            })
        },
        add: function(data){
            return $http({
                method: 'POST',
                data: data,
                url: '/tracker/api/project'
            })
        },
        getIssues: function(project_id){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/'+project_id+'/issues?format=json'
            })
        }
    };
});