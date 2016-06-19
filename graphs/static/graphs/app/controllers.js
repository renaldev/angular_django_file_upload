'use strict';

var graphsControllers = angular.module('graphsControllers', []);

graphsControllers.controller('formController', ['$scope', 'fileUpload', function($scope, fileUpload){

    $scope.dataReceived = false;
    $scope.currentFile = "";
    $scope.dataJson = {};
    $scope.dataExel = [];

    $scope.uploadFile = function(){
        var file = $scope.myFile;
        var uploadUrl = global_urls.post_file;

        var responseCb = function (data) {
            $scope.dataReceived = true;
            $scope.currentFile = file.name;
            $scope.dataExel = data.data;
        };
        var errorCb = function() {
            alert("Error Upload");
        }

        fileUpload.uploadFileToUrl(file, uploadUrl, responseCb, errorCb);
    };

    $scope.viewData = function() {
        $scope.dataJson = {
            type : 'line' ,
            series : [
                { values : $scope.dataExel }
            ]
        };
    }
}]);