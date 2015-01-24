var services = angular.module('trackerApp.services', []);

services.factory('Projects', function($http) {

    return {
        list: function(){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/?format=json'
            });
        },
        get: function(project_id){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/' + project_id + '?format=json'
            })
        }
    };

});