'use strict';

var graphsServices = angular.module('graphsServices', []);

graphsServices.service('fileUpload', ['$http', '$cookies', function ($http, $cookies) {
    this.uploadFileToUrl = function(file, uploadUrl, successCb, errorCb){

        var fd = new FormData();
        fd.append('file', file);

        $http({
            url: uploadUrl,
            method: 'POST',
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined},
            data: fd
        })
        .success(function(response){
            successCb(response);
        })
        .error(function(){
            errorCb();
        });
    }
}]);