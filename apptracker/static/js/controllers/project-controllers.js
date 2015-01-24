'use strict';

var trackerControllers = angular.module('trackerApp.controllers', []);

trackerControllers.controller("ProjectHome", function($scope, Projects) {
    console.log("lolilol");

    Projects.list().success(function (response) {
        //Dig into the responde to get the relevant data
        console.log("hello");
        console.log(response);
    }).error(function (data, status, headers, config) {
        console.log("projects list failed !")
    });

    Projects.get(2).success(function (response) {
        //Dig into the responde to get the relevant data
        console.log("hello");
        console.log(response);
    }).error(function (data, status, headers, config) {
        console.log("projects list failed !")
    });
});