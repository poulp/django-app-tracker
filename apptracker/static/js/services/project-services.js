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
        },
        getLabels: function(project_id){
            return $http({
                method: 'GET',
                url: '/tracker/api/project/'+project_id+'/labels'
            })
        },
        addLabel: function(project_id, label){
            return $http({
                method: 'POST',
                data: label,
                url: '/tracker/api/project/'+project_id+'/labels'
            })
        },
        editLabel: function(project_id, label_pk, label){
            return $http({
                method: 'PUT',
                data: label,
                url: '/tracker/api/project/'+project_id+'/labels/'+label_pk
            })
        },
        removeLabel: function(project_id, label_pk){
            return $http({
                method: 'DELETE',
                url: '/tracker/api/project/'+project_id+'/labels/'+label_pk
            })
        }
    };
});